# <div align='center'> 🇬🇧 
# <div align='center'>📚 Book\_Scraper

> Fully-featured Python script to automatically scrape books from [Books to Scrape](http://books.toscrape.com/), export data to CSV by category, and download cover images.

## <div align='center'>🚀 Features

* ✅ Scrapes **all book categories**
* ✅ Extracts **titles, price, availability, rating, description, image**
* ✅ Exports **CSV** files by category into the `output_data/` folder
* ✅ Downloads **cover images** into optional subfolders
* ✅ Automatically navigates through pages (pagination)

---

## <div align='center'>🛠️ Installation

```bash
git clone https://github.com/dim-gggl/Book_Scraper.git
cd Book_Scraper
```

Then, create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

And install the dependencies:

```bash
pip install -r requirements.txt
```

---

## <div align='center'>🧑‍💻 Usage

```bash
source venv/bin/activate
python3 main.py
```

Follow the instructions in the terminal menu.

📝 CSV files and images are automatically generated inside the `scripts/output_data` folder.

---

## <div align='center'>📂 Simplified Structure

```
Book_Scraper/
├── scripts/
│   ├── __init__.py
│   ├── phase_1.py
│   ├── phase_2.py
│   ├── phase_3.py
│   ├── phase_4.py
│   ├── utils.py
│   └── output_data/
│       ├── book1.csv
│       └── ...
├── __init__.py
├── main.py
├── README.md
└── requirements.txt
```

---

## <div align='center'>📌 Sample Data

| universal\_product\_code | title              | price\_including\_tax | price\_excluding\_tax | number\_available       | category           | review\_rating |
| ------------------------ | ------------------ | --------------------- | --------------------- | ----------------------- | ------------------ | -------------- |
| 90fa61229261140a         | Tipping the Velvet | £ 53.74               | £ 53.74               | In stock (20 available) | Historical Fiction | 1/5            |

---

## <div align='center'>🎯 Learning Goals

* Learn HTML scraping with `BeautifulSoup`
* Automate data collection/export/processing
* Prepare for more advanced projects like APIs or database interactions

---

## <div align='center'>📌 To Improve

* [ ] Consider refactoring into an OOP (Object-Oriented Programming) approach
* [ ] Improve the architecture to make it more modular
* [ ] Add a simple web interface using Flask
* [ ] Implement unit tests
* [ ] Add logging or a verbose mode

---

## <div align='center'>🧠 Author

👤 **Dimitri Gaggioli**

Python Developer

[dim-gggl](https://github.com/dim-gggl)

---

## <div align='center'>🌍 Stack</div>
  

* Python 3.12+
* BeautifulSoup
* Requests
* CSV, OS, re, urllib

---

## <div align='center'>🌍 License

MIT — Use it wisely.
---

# <div align='center'>🇫🇷
# <div align='center'> 📚 Book\_Scraper

> Script Python complet pour scraper automatiquement les livres du site [Books to Scrape](http://books.toscrape.com/), exporter les données en CSV par catégorie et télécharger les images des couvertures.

## <div align='center'>🚀 Fonctionnalités

* ✅ Scraping de **toutes les catégories** de livres
* ✅ Récupération des **titres, prix, stock, note, description, image**
* ✅ Export **CSV** par catégorie dans un dossier `output_data/`
* ✅ Téléchargement des **images de couverture** dans des sous-dossiers en option
* ✅ Navigation automatique entre les pages (pagination)

---

## <div align='center'>🛠️ Installation

```bash
git clone https://github.com/dim-gggl/Book_Scraper.git
cd Book_Scraper
```

Puis installation d'un environnement virtuel :

```bash
python3 -m venv venv
source venv/bin/activate
```

Et installation des dépendances:

```bash
pip install -r requirements.txt
```

---

## <div align='center'>🧑‍💻 Utilisation


```bash
source venv/bin/activate
python3 main.py
```

Et laisse-toi guider par le menu du terminal.

📝 Les fichiers CSV et les images sont générés automatiquement dans le dossier `scripts/output_data`.

---

## <div align='center'>📂 Arborescence simplifiée

```
Book_Scraper/
├── scripts/
│   ├── __init__.py
│   ├── phase_1.py
│   ├── phase_2.py
│   ├── phase_3.py
│   ├── phase_4.py
│   ├── utils.py
│   └── output_data/
│       ├── book1.csv
│       └── ...
├── __init__.py
├── main.py
├── README.md
└── requirements.txt
```

---

## <div align='center'>📌 Extrait de données

| universal_product_code   | title    | price_including_tax  | price_excluding_tax | number_available | category | review_rating |
| ------------------------ | --------- | ------------------- | -------------------- | ---------------- | -------- | -------------- |
| 90fa61229261140a | Tipping the Velvet | £ 53.74 | £ 53.74 | In stock (20 available) | Historical Fiction | 1/5 |

---

## <div align='center'>🎯 Objectifs pédagogiques

* Apprentissage du scraping HTML avec `BeautifulSoup`
* Automatisation de collecte/export/traitement de données
* Préparation à des projets plus ambitieux de type API ou intéractions avec des databases

---

## <div align='center'>📌 À améliorer

* [ ] Envisager une refactorisation en P.O.O
* [ ] Améliorer l'architecture, plus modulaire
* [ ] Interface web simple (Flask)
* [ ] Ajout de tests unitaires
* [ ] Ajout de logs ou d’un mode `verbose`

---

## <div align='center'>🧠 Auteur

👤 **Dimitri Gaggioli**

Développeur Python ·

[dim-gggl](https://github.com/dim-gggl)

---

## <div align='center'><div align='center'>🌍 Stack

* Python 3.12+
* BeautifulSoup
* Requests
* CSV, OS, re, urllib

---

## <div align='center'>🌍 Licence

MIT — Faites-en bon usage.
