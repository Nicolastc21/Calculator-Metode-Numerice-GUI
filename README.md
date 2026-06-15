# Calculator Metode Numerice - GUI

O aplicație desktop dezvoltată în Python folosind PyQt5 pentru interfața grafică, care permite rezolvarea ecuațiilor neliniare utilizând diverse metode numerice. Aplicația validează condițiile matematice, calculează rădăcina și generează un grafic interactiv.

## 🚀 Caracteristici
* **Metode implementate:**
    * Metoda bisecției
    * Metoda coardei 
    * Metoda tangentei (Newton-Raphson)
    * Principiul contracțiilor
* **Validări în timp real:** Verifică automat dacă funcția schimbă semnul pe intervalul dat sau dacă derivata se anulează, afișând avertismente.
* **Grafice integrate:** Folosește `matplotlib` pentru a desena funcția, capetele intervalului și rădăcina aproximativă.
* **Statistici:** Afișează numărul de pași, eroarea absolută, eroarea relativă (comparată cu `scipy.optimize.fsolve`) și timpul de execuție.

## 🛠️ Cerințe și Instalare

Pentru a rula acest proiect, ai nevoie de Python instalat. Poți instala dependențele necesare rulând următoarea comandă în terminal:

```bash
pip install PyQt5 numpy sympy scipy matplotlib
