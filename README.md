# ☀️ Good Morning App (Καλημέρα App)

Μια μοντέρνα, κομψή εφαρμογή επιφάνειας εργασίας (Desktop Application) γραμμένη σε **Python** με τη χρήση της βιβλιοθήκης **Tkinter**, η οποία εμφανίζει ένα πανέμορφο μήνυμα καλημέρας και κλείνει με το πάτημα ενός κουμπιού ή πλήκτρου.

---

## ✨ Χαρακτηριστικά / Features

* 🎨 **Premium Modern Design:** Σχεδιασμένο με ένα πανέμορφο σκούρο θέμα (Dark Theme) εμπνευσμένο από την παλέτα Catppuccin Mocha.
* ☀️ **Vibrant UI:** Φωτεινό emoji ήλιου και καθαρή, κομψή τυπογραφία (Helvetica).
* 🖱️ **Interactive Button:** Προσαρμοσμένο κουμπί "OK" με εφέ αλλαγής χρώματος κατά το πέρασμα του ποντικιού (hover transitions).
* ⌨️ **Keyboard Shortcuts:** Κλείσιμο της εφαρμογής άμεσα με το πάτημα του κουμπιού **OK**, του πλήκτρου **Enter** ή του **Escape**.
* 📦 **Windows Executable (.exe):** Έτοιμο αυτόνομο αρχείο για εκτέλεση σε Windows χωρίς ανάγκη εγκατάστασης της Python.

---

## 🚀 Πώς να το τρέξετε / How to Run

### 🐧 Στο Linux
Για να τρέξετε τον πηγαίο κώδικα απευθείας:
```bash
python3 good_morning.py
```

### 🪟 Στα Windows
Μπορείτε να εκτελέσετε απευθείας το αρχείο `good_morning.exe` με διπλό κλικ! 

Αν θέλετε να το χτίσετε ξανά μόνοι σας από τον πηγαίο κώδικα στα Windows:
1. Εγκαταστήστε τον PyInstaller:
   ```cmd
   pip install pyinstaller
   ```
2. Δημιουργήστε το `.exe` αρχείο:
   ```cmd
   pyinstaller --onefile --noconsole good_morning.py
   ```
   Το εκτελέσιμο θα βρίσκεται στον φάκελο `dist/`.

---

## 🛠️ Τεχνολογίες / Tech Stack
* **Language:** Python 3
* **GUI Library:** Tkinter (Tcl/Tk)
* **Packaging:** PyInstaller
