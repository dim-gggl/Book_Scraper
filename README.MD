# 📚 Book\_Scraper

> Script Python complet pour scraper automatiquement les livres du site [Books to Scrape](http://books.toscrape.com/), exporter les données en CSV par catégorie et télécharger les images des couvertures.

## 🚀 Fonctionnalités

* ✅ Scraping de **toutes les catégories** de livres
* ✅ Récupération des **titres, prix, stock, note, description, image**
* ✅ Export **CSV** par catégorie dans un dossier `output_data/`
* ✅ Téléchargement des **images de couverture** dans des sous-dossiers en option
* ✅ Navigation automatique entre les pages (pagination)

---

## 🛠️ Installation

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

## 🧑‍💻 Utilisation


```bash
source venv/bin/activate
python3 main.py
```

Et laisse-toi guider par le menu du terminal.

📝 Les fichiers CSV et les images sont générés automatiquement dans le dossier `scripts/output_data`.

---

## 📂 Arborescence simplifiée

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

## 📌 Extrait de données

| universal_product_code   | title    | price_including_tax  | price_excluding_tax | number_available | category | review_rating |
| ------------------------ | --------- | ------------------- | -------------------- | ---------------- | -------- | -------------- |
| 90fa61229261140a | Tipping the Velvet | £ 53.74 | £ 53.74 | In stock (20 available) | Historical Fiction | 1/5 |

---

## 🎯 Objectifs pédagogiques

* Apprentissage du scraping HTML avec `BeautifulSoup`
* Automatisation de collecte/export/traitement de données
* Préparation à des projets plus ambitieux de type API ou intéractions avec des databases

---

## 📌 À améliorer

* [ ] Envisager une refactorisation en P.O.O
* [ ] Améliorer l'architecture, plus modulaire
* [ ] Interface web simple (Flask)
* [ ] Ajout de tests unitaires
* [ ] Ajout de logs ou d’un mode `verbose`

---

## 🧠 Auteur

👤 **Dimitri Gaggioli**
Développeur Python · [dim-gggl](https://github.com/dim-gggl)

---

## 🌍 Stack

* Python 3.12+
* BeautifulSoup
* Requests
* CSV, OS, re, urllib

---

## 🌍 Licence

MIT — Faites-en bon usage.
