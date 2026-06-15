import sys
import numpy as np
import sympy as sp
from scipy.optimize import fsolve
import time

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PyQt5.QtWidgets import (QApplication, QComboBox, QFormLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QStatusBar, QVBoxLayout, QWidget, QMessageBox)

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 650)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        
        self.horizontalLayout = QVBoxLayout(self.centralwidget) 
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.label)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_6)
        self.input_a = QLineEdit(self.centralwidget)
        self.input_a.setObjectName(u"input_a")
        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.input_a)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_7)
        self.input_b = QLineEdit(self.centralwidget)
        self.input_b.setObjectName(u"input_b")
        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.input_b)
        self.verticalLayout_2.addLayout(self.formLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.input_functie = QLineEdit(self.centralwidget)
        self.input_functie.setObjectName(u"input_functie")
        self.verticalLayout.addWidget(self.input_functie)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.comboMetoda = QComboBox(self.centralwidget)
        self.comboMetoda.addItem("")
        self.comboMetoda.addItem("")
        self.comboMetoda.addItem("")
        self.comboMetoda.addItem("")
        self.comboMetoda.setObjectName(u"comboMetoda")
        self.verticalLayout.addWidget(self.comboMetoda)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.input_nrpasi = QLineEdit(self.centralwidget)
        self.input_nrpasi.setObjectName(u"input_nrpasi")
        self.verticalLayout.addWidget(self.input_nrpasi)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.input_eroare = QLineEdit(self.centralwidget)
        self.input_eroare.setObjectName(u"input_eroare")
        self.verticalLayout.addWidget(self.input_eroare)

        self.lbl_checks = QLabel(self.centralwidget)
        self.lbl_checks.setObjectName(u"lbl_checks")
        self.lbl_checks.setStyleSheet("font-weight: bold; margin-top: 10px;")
        self.verticalLayout.addWidget(self.lbl_checks)

        self.btn_calculeaza = QPushButton(self.centralwidget)
        self.btn_calculeaza.setObjectName(u"btn_calculeaza")
        self.btn_calculeaza.setStyleSheet("padding: 8px; background-color: #4CAF50; color: white; font-weight: bold;")
        self.verticalLayout.addWidget(self.btn_calculeaza)
        
        self.lb_1aprox = QLabel(self.centralwidget)
        self.lb_1aprox.setObjectName(u"lb_1aprox")
        self.verticalLayout.addWidget(self.lb_1aprox)
        self.lb1_abs = QLabel(self.centralwidget)
        self.lb1_abs.setObjectName(u"lb1_abs")
        self.verticalLayout.addWidget(self.lb1_abs)
        self.lb1_rel = QLabel(self.centralwidget)
        self.lb1_rel.setObjectName(u"lb1_rel")
        self.verticalLayout.addWidget(self.lb1_rel)
        self.lb1_timp = QLabel(self.centralwidget)
        self.lb1_timp.setObjectName(u"lb1_timp")
        self.verticalLayout.addWidget(self.lb1_timp)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(450, 450) 
        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 850, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Metode Numerice", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Interval", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"a=", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"b=", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Functie", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Metoda", None))
        self.comboMetoda.setItemText(0, QCoreApplication.translate("MainWindow", u"Metoda coardei", None))
        self.comboMetoda.setItemText(1, QCoreApplication.translate("MainWindow", u"Metoda bisectiei", None))
        self.comboMetoda.setItemText(2, QCoreApplication.translate("MainWindow", u"Principiul contractiilor", None))
        self.comboMetoda.setItemText(3, QCoreApplication.translate("MainWindow", u"Metoda tangentei", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Numarul de pasi", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Eroare", None))
        self.lbl_checks.setText(QCoreApplication.translate("MainWindow", u"Verificări: ...", None))
        self.btn_calculeaza.setText(QCoreApplication.translate("MainWindow", u"Calculeaza", None))
        self.lb_1aprox.setText(QCoreApplication.translate("MainWindow", u"Valoare aprox: -", None))
        self.lb1_abs.setText(QCoreApplication.translate("MainWindow", u"Eroare absolută: -", None))
        self.lb1_rel.setText(QCoreApplication.translate("MainWindow", u"Eroare relativă: -", None))
        self.lb1_timp.setText(QCoreApplication.translate("MainWindow", u"Timp execuție: -", None))

class MetodeNumericeApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self.fig)
        
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.widget.setLayout(layout)
        
        self.input_functie.setText("x**3 - x - 2")
        self.input_a.setText("1")
        self.input_b.setText("2")
        self.input_eroare.setText("1e-5")
        self.input_nrpasi.setText("100")
        self.comboMetoda.setCurrentIndex(1) 

        self.btn_calculeaza.clicked.connect(self.calculeaza)
        self.comboMetoda.currentIndexChanged.connect(self.calculeaza)

        self.input_functie.textChanged.connect(self.verifica_conditii)
        self.input_a.textChanged.connect(self.verifica_conditii)
        self.input_b.textChanged.connect(self.verifica_conditii)
        self.comboMetoda.currentIndexChanged.connect(self.verifica_conditii)

        self.verifica_conditii()

    def verifica_conditii(self):
        str_func = self.input_functie.text().strip()
        
        try:
            a = float(self.input_a.text())
            b = float(self.input_b.text())
        except ValueError:
            self.lbl_checks.setText("Aștept date valide pt interval...")
            self.lbl_checks.setStyleSheet("color: orange;")
            return
            
        if a >= b:
            self.lbl_checks.setText("❌ Eroare: 'a' trebuie să fie mai mic ca 'b'")
            self.lbl_checks.setStyleSheet("color: red;")
            return

        try:
            x_sym = sp.Symbol('x')
            expr = sp.sympify(str_func)
            f = sp.lambdify(x_sym, expr, 'numpy')
            expr_derivata = sp.diff(expr, x_sym)
            df = sp.lambdify(x_sym, expr_derivata, 'numpy')
        except Exception:
            self.lbl_checks.setText("❌ Funcție invalidă!")
            self.lbl_checks.setStyleSheet("color: red;")
            return

        metoda = self.comboMetoda.currentText()
        mesaj = f"Verificări matematice:\n"
        este_valid = True

        try:
            val_a, val_b = f(a), f(b)
            if val_a * val_b < 0:
                mesaj += "✅ f(a) * f(b) < 0 (Schimbă semnul)\n"
            elif val_a * val_b == 0:
                mesaj += "✅ Rădăcina e chiar pe capăt de interval!\n"
            else:
                mesaj += "❌ f(a) * f(b) > 0 (Rădăcina nu e garantată)\n"
                if metoda in ["Metoda bisectiei", "Metoda coardei"]:
                    este_valid = False
        except Exception:
            self.lbl_checks.setText("❌ Eroare la evaluarea funcției")
            return

        if metoda in ["Metoda tangentei", "Principiul contractiilor"]:
            x_mijloc = (a + b) / 2.0
            if df(x_mijloc) != 0:
                mesaj += "✅ f'(x0) ≠ 0 (Derivata nenulă)"
            else:
                mesaj += "❌ f'(x0) = 0 (Metoda poate crăpa!)"
                este_valid = False

        self.lbl_checks.setText(mesaj.strip())

        if este_valid:
            self.lbl_checks.setStyleSheet("color: green;")
        else:
            self.lbl_checks.setStyleSheet("color: red;")


    def calculeaza(self):
        str_func = self.input_functie.text().strip()
        if not str_func: return

        try:
            a = float(self.input_a.text())
            b = float(self.input_b.text())
            epsilon = float(self.input_eroare.text())
            pasi = int(self.input_nrpasi.text()) 
        except ValueError:
            return

        if a >= b: return

        try:
            x_sym = sp.Symbol('x')
            expr = sp.sympify(str_func)
            f = sp.lambdify(x_sym, expr, 'numpy')
            expr_derivata = sp.diff(expr, x_sym)
            df = sp.lambdify(x_sym, expr_derivata, 'numpy')
        except Exception:
            return

        metoda = self.comboMetoda.currentText()

        start_time = time.perf_counter()
        x_aprox = 0
        iteratii = 0
        
        try:
            if metoda == "Metoda bisectiei":
                al, bl = a, b
                while (bl - al) / 2.0 > epsilon and iteratii < pasi:
                    c = (al + bl) / 2.0
                    if f(c) == 0:
                        break
                    elif f(al) * f(c) < 0:
                        bl = c
                    else:
                        al = c
                    iteratii += 1
                x_aprox = (al + bl) / 2.0

            elif metoda == "Metoda coardei":
                al, bl = a, b
                x_vechi = al
                c = al
                while iteratii < pasi:
                    if f(bl) - f(al) == 0: break 
                    c = (al * f(bl) - bl * f(al)) / (f(bl) - f(al))
                    if abs(c - x_vechi) < epsilon or f(c) == 0: break
                    if f(al) * f(c) < 0:
                        bl = c
                    else:
                        al = c
                    x_vechi = c
                    iteratii += 1
                x_aprox = c

            elif metoda == "Metoda tangentei":
                x_n = (a + b) / 2.0 
                while iteratii < pasi:
                    df_val = df(x_n)
                    if df_val == 0: break
                    x_n_plus_1 = x_n - f(x_n) / df_val
                    if abs(x_n_plus_1 - x_n) < epsilon:
                        x_n = x_n_plus_1
                        break
                    x_n = x_n_plus_1
                    iteratii += 1
                x_aprox = x_n

            elif metoda == "Principiul contractiilor":
                x_n = (a + b) / 2.0
                df_val0 = df(x_n)
                if df_val0 != 0:
                    lmbda = 1.0 / df_val0
                    while iteratii < pasi:
                        x_n_plus_1 = x_n - lmbda * f(x_n)
                        if abs(x_n_plus_1 - x_n) < epsilon:
                            x_n = x_n_plus_1
                            break
                        x_n = x_n_plus_1
                        iteratii += 1
                    x_aprox = x_n
        except Exception:
            pass 

        end_time = time.perf_counter()
        timp_executie = end_time - start_time

        x0_guess = (a + b) / 2.0
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            x_exact_arr = fsolve(f, x0_guess)
        x_exact = x_exact_arr[0]

        eroare_abs = abs(x_exact - x_aprox)
        eroare_rel = (eroare_abs / abs(x_exact)) if x_exact != 0 else 0

        self.lb_1aprox.setText(f"Valoare aprox: {x_aprox:.6f} (în {iteratii} pași)")
        self.lb1_abs.setText(f"Eroare absolută: {eroare_abs:.2e}")
        self.lb1_rel.setText(f"Eroare relativă: {eroare_rel:.2e}")
        self.lb1_timp.setText(f"Timp execuție: {timp_executie:.6f} s")

        self.ax.clear()
        x_vals = np.linspace(a - 0.5, b + 0.5, 400)
        y_vals = f(x_vals)
        
        self.ax.plot(x_vals, y_vals, 'b-', label=f"f(x)={str_func}")
        self.ax.axhline(0, color='black', linewidth=1) 
        
        self.ax.axvline(a, color='gray', linestyle='--', alpha=0.6, label="Capăt a")
        self.ax.axvline(b, color='gray', linestyle='--', alpha=0.6, label="Capăt b")
        
        self.ax.plot(x_aprox, f(x_aprox), 'ro', markersize=8, label="Rădăcina aprox")
        
        self.ax.set_title(f"Grafic - {metoda}")
        self.ax.grid(True)
        self.ax.legend()
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MetodeNumericeApp()
    window.show()
    sys.exit(app.exec_())