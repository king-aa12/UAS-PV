import sys
import os
import sqlite3
import re

def resource_path(relative_path):
    """
    Mendapatkan path absolut ke resource,
    bekerja untuk mode development dan PyInstaller
    """
    try:
        # PyInstaller membuat folder temp di _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

from datetime import datetime

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit,
    QComboBox, QPushButton, QTableWidget, QTableWidgetItem,
    QMessageBox, QVBoxLayout, QTabWidget, QHeaderView, QSizePolicy
)
from PyQt5.QtGui import QIcon, QColor, QBrush, QPainter, QFont, QFontDatabase
from PyQt5.QtCore import Qt, QTimer

from PyQt5.QtChart import (
    QChart, QChartView, QBarSet, QBarSeries, QBarCategoryAxis, QValueAxis
)

# =========================
# DATABASE
# =========================
class Database:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        self.db_path = os.path.join(base_dir, "pulsa.db")
        self.conn = sqlite3.connect(self.db_path)
        self.create_table()
        self.upgrade_table()

    def create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS transaksi (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                provider TEXT,
                no_hp TEXT,
                nominal INTEGER,
                harga INTEGER,
                keuntungan INTEGER,
                tanggal TEXT
            )
        """)
        self.conn.commit()

    def upgrade_table(self):
        cur = self.conn.cursor()
        cur.execute("PRAGMA table_info(transaksi)")
        kolom = [c[1] for c in cur.fetchall()]
        if "keuntungan" not in kolom:
            self.conn.execute(
                "ALTER TABLE transaksi ADD COLUMN keuntungan INTEGER DEFAULT 0"
            )
            self.conn.commit()

    def insert_data(self, provider, no_hp, nominal):
        harga = nominal + 3000
        keuntungan = 3000
        tanggal = datetime.now().strftime("%d-%m-%Y %H:%M")

        self.conn.execute("""
            INSERT INTO transaksi
            (provider, no_hp, nominal, harga, keuntungan, tanggal)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (provider, no_hp, nominal, harga, keuntungan, tanggal))
        self.conn.commit()

    def get_all(self):
        return self.conn.execute("""
            SELECT provider, no_hp, nominal, harga, tanggal
            FROM transaksi
            ORDER BY id DESC
        """).fetchall()

    def laporan_per_provider(self):
        return self.conn.execute("""
            SELECT provider,
                   COUNT(*) AS total_transaksi,
                   SUM(keuntungan) AS total_keuntungan
            FROM transaksi
            GROUP BY provider
        """).fetchall()

    def total_keuntungan(self):
        return self.conn.execute(
            "SELECT IFNULL(SUM(keuntungan),0) FROM transaksi"
        ).fetchone()[0]


# =========================
# MAIN APP
# =========================
class PulsaApp(QMainWindow):

    PROVIDER_COLORS = {
        "Telkomsel": "#E53935",
        "Indosat": "#FBC02D",
        "XL": "#1E88E5",
        "Axis": "#8E24AA",
        "Three": "#FB8C00",
        "Smartfren": "#43A047"
    }

    def __init__(self):
        super().__init__()
        self.db = Database()

        self.setWindowTitle("Aplikasi Penjualan Pulsa")
        # Set minimum size agar tidak terlalu kecil
        self.setMinimumSize(1024, 768)
        self.setWindowIcon(QIcon("app_icon.ico"))
        
        # Load font yang lebih baik
        self.setup_fonts()
        
        self.tabs = QTabWidget()
        self.tabs.setFont(self.font_regular)
        self.setCentralWidget(self.tabs)

        self.init_transaksi_tab()
        self.init_data_tab()
        self.init_laporan_tab()

        self.update_theme()
        
        # Timer untuk update font berdasarkan resize
        QTimer.singleShot(100, self.adjust_font_sizes)

    def setup_fonts(self):
        """Setup font untuk aplikasi"""
        # Coba load font Inter jika ada, atau gunakan default
        font_id = QFontDatabase.addApplicationFont("Inter-Regular.ttf")
        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            self.font_title = QFont(font_family, 16, QFont.Bold)
            self.font_subtitle = QFont(font_family, 14, QFont.Bold)
            self.font_regular = QFont(font_family, 11)
            self.font_small = QFont(font_family, 10)
        else:
            # Fallback ke font default
            self.font_title = QFont("Segoe UI", 16, QFont.Bold)
            self.font_subtitle = QFont("Segoe UI", 14, QFont.Bold)
            self.font_regular = QFont("Segoe UI", 11)
            self.font_small = QFont("Segoe UI", 10)
        
        # Set font default untuk aplikasi
        QApplication.setFont(self.font_regular)

    def resizeEvent(self, event):
        """Event saat window di-resize"""
        super().resizeEvent(event)
        QTimer.singleShot(50, self.adjust_font_sizes)

    def adjust_font_sizes(self):
        """Adjust font size berdasarkan ukuran window"""
        width = self.width()
        height = self.height()
        
        # Adjust berdasarkan lebar window
        if width < 1200:
            scale_factor = width / 1200
            base_size = max(10, int(11 * scale_factor))
            self.font_regular.setPointSize(base_size)
            self.font_small.setPointSize(max(9, int(10 * scale_factor)))
        else:
            self.font_regular.setPointSize(11)
            self.font_small.setPointSize(10)
            
        # Update font untuk semua widget
        self.update_widget_fonts()

    def update_widget_fonts(self):
        """Update font untuk semua widget"""
        self.tabs.setFont(self.font_regular)
        
        # Tab Transaksi
        self.lbl_judul.setFont(self.font_title)
        self.cmb_provider.setFont(self.font_regular)
        self.txt_hp.setFont(self.font_regular)
        self.cmb_nominal.setFont(self.font_regular)
        self.lbl_harga.setFont(self.font_subtitle)
        self.btn_proses.setFont(self.font_subtitle)
        
        # Tab Data Transaksi
        self.table.setFont(self.font_small)
        header = self.table.horizontalHeader()
        header.setFont(self.font_subtitle)
        
        # Tab Laporan
        self.lbl_keuntungan.setFont(self.font_subtitle)
        self.chart.setTitleFont(self.font_subtitle)

    # =========================
    # TAB TRANSAKSI
    # =========================
    def init_transaksi_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.lbl_judul = QLabel("TRANSAKSI PULSA")
        self.lbl_judul.setAlignment(Qt.AlignCenter)

        self.cmb_provider = QComboBox()
        self.cmb_provider.addItems(self.PROVIDER_COLORS.keys())
        self.cmb_provider.currentIndexChanged.connect(self.update_theme)

        self.txt_hp = QLineEdit()
        self.txt_hp.setPlaceholderText("Masukkan nomor HP (10–13 digit)")

        self.cmb_nominal = QComboBox()
        self.cmb_nominal.addItems(["5000", "10000", "20000", "30000", "50000", "100000"])
        self.cmb_nominal.currentIndexChanged.connect(self.update_harga)

        self.lbl_harga = QLabel("Harga: Rp 0")
        self.lbl_harga.setAlignment(Qt.AlignCenter)

        self.btn_proses = QPushButton("PROSES TRANSAKSI")
        self.btn_proses.clicked.connect(self.proses_transaksi)

        layout.addWidget(self.lbl_judul)
        layout.addWidget(QLabel("Provider"))
        layout.addWidget(self.cmb_provider)
        layout.addWidget(QLabel("Nomor HP"))
        layout.addWidget(self.txt_hp)
        layout.addWidget(QLabel("Nominal Pulsa"))
        layout.addWidget(self.cmb_nominal)
        layout.addWidget(self.lbl_harga)
        layout.addWidget(self.btn_proses)

        tab.setLayout(layout)
        self.tabs.addTab(tab, "Transaksi")

        self.update_harga()

    # =========================
    # TAB DATA TRANSAKSI
    # =========================
    def init_data_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)

        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels(
            ["Provider", "No HP", "Nominal", "Harga", "Tanggal"]
        )
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        
        # Set font dan style untuk tabel
        self.table.setFont(self.font_small)
        header = self.table.horizontalHeader()
        header.setFont(self.font_subtitle)
        header.setDefaultAlignment(Qt.AlignCenter)
        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setMinimumHeight(40)
        
        # Set row height
        self.table.verticalHeader().setDefaultSectionSize(35)
        
        # Enable word wrap untuk cell yang panjang
        self.table.setWordWrap(True)
        
        # Set selection behavior
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setAlternatingRowColors(True)
        
        layout.addWidget(self.table)
        tab.setLayout(layout)
        self.tabs.addTab(tab, "Data Transaksi")

        self.load_data()


    # =========================
    # TAB LAPORAN
    # =========================
    def init_laporan_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.lbl_keuntungan = QLabel()
        self.lbl_keuntungan.setAlignment(Qt.AlignCenter)
        self.lbl_keuntungan.setStyleSheet(
            "font-size:20px;font-weight:bold;padding:15px"
        )

        self.chart = QChart()
        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        layout.addWidget(self.lbl_keuntungan)
        layout.addWidget(self.chart_view)

        tab.setLayout(layout)
        self.tabs.addTab(tab, "Laporan")

        self.update_laporan()

    # =========================
    # LOGIC
    # =========================
    def update_theme(self):
        color = self.PROVIDER_COLORS.get(
            self.cmb_provider.currentText(), "#1565C0"
        )

        self.lbl_judul.setStyleSheet(f"""
            background-color:{color};
            color:white;
            font-size:18px;
            font-weight:bold;
            padding:12px;
            border-radius:8px;
        """)

        self.lbl_harga.setStyleSheet(f"""
            background-color:{color};
            color:white;
            font-weight:bold;
            padding:10px;
            border-radius:6px;
        """)

        self.btn_proses.setStyleSheet(f"""
            QPushButton {{
                background-color:{color};
                color:white;
                padding:10px;
                border-radius:6px;
                font-weight:bold;
            }}
            QPushButton:hover {{
                background-color:#333;
            }}
        """)

    def update_harga(self):
        nominal = int(self.cmb_nominal.currentText())
        harga = nominal + 3000
        self.lbl_harga.setText(f"Harga: Rp {harga:,}".replace(",", "."))

    def proses_transaksi(self):
        hp = self.txt_hp.text()

        if not re.fullmatch(r"\d{10,13}", hp):
            QMessageBox.warning(self, "Validasi", "Nomor HP tidak valid")
            return

        if QMessageBox.question(
            self, "Konfirmasi", "Lanjutkan transaksi?",
            QMessageBox.Yes | QMessageBox.No
        ) == QMessageBox.Yes:
            self.db.insert_data(
                self.cmb_provider.currentText(),
                hp,
                int(self.cmb_nominal.currentText())
            )
            QMessageBox.information(self, "Sukses", "Transaksi berhasil")
            self.txt_hp.clear()
            self.load_data()
            self.update_laporan()

    def load_data(self):
        data = self.db.get_all()
        self.table.setRowCount(len(data))
        for r, row in enumerate(data):
            for c, val in enumerate(row):
                item = QTableWidgetItem(str(val))
                item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(r, c, item)

    def update_laporan(self):
        self.chart.removeAllSeries()

        series = QBarSeries()
        info = "Keuntungan per Provider:\n\n"

        for provider, total_trx, total_untung in self.db.laporan_per_provider():
            bar = QBarSet(provider)
            bar << total_trx
            bar.setBrush(QBrush(QColor(self.PROVIDER_COLORS.get(provider, "#555"))))
            series.append(bar)

            info += f"{provider} : Rp {total_untung:,}\n".replace(",", ".")

        self.chart.addSeries(series)

        axisX = QBarCategoryAxis()
        axisX.append(["Transaksi"])
        self.chart.setAxisX(axisX, series)

        self.chart.setTitle("Grafik Penjualan per Provider")
        self.chart.legend().setVisible(True)

        total = self.db.total_keuntungan()
        self.lbl_keuntungan.setText(
            f"TOTAL KEUNTUNGAN : Rp {total:,}\n\n{info}".replace(",", ".")
        )


# =========================
# RUN
# =========================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PulsaApp()
    window.show()
    sys.exit(app.exec_())
