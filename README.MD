# Web Scraper pour Books to Scrape

## **Description**
Ce projet Python scrape le site [Books to Scrape](http://books.toscrape.com/) pour collecter des informations sur les livres : prix, descriptions, catégories, évaluations, et images des couvertures. Les scripts sont conçus pour être modulaires et faciles à personnaliser, permettant aux utilisateurs de :
- Extraire les informations d'un seul livre.
- Parcourir et scraper une catégorie complète.
- Automatiser le scraping de toutes les catégories.
- Télécharger les images des livres.

Chaque fichier CSV sera stocké dans un dossier dédié à sa catégorie en compagnie d'un sous-dossier où se trouveront les images portant le titre du livre dont elles sont la couverture.

---

## **Prérequis**
- Python 3.8 ou version ultérieure.
- Bibliothèques nécessaires :
  - `requests`
  - `BeautifulSoup4`
  - `csv`

> **Recommandé :
>** Utiliser un environnement virtuel pour isoler les dépendances :
```bash
python -m venv venv
source venv/bin/activate  # Sous Windows : venv\Scripts\activate
pip install -r requirements.txt
```
---

## Installation

### **Étape 1 : Cloner le projet**
```bash
git clone https://github.com/dim-gggl/1_Analyse_de_marche_Python.git
cd 1_Analyse_de_marche_Python
```

### **Étape 2 : Installer les dépendances**

#### **Copiez le code :**
```bash
pip install -r requirements.txt
```

---

## Utilisation

### **Exécuter les scripts**

Il est recommandé d'exécuter les `scripts` directement depuis leur dossier parent car ils sont configurés pour enregistrer les données extraites suivat le chemin relatif `./output_data`
qui est contenu dans la variable `OUTPUT_FILE_PATH`.

**Sinon vous pouvez personnaliser le chemin de sortie de vos fichiers en modifiant ``OUTPUT_FILE_PATH`` dans `phase_1.py`**
#### **Script 1 : Scraper un livre unique**
- **Commande :**
    ```bash
    python phase_1.py
    ```

- **Modification possible :**
    - Localisez cette ligne dans `phase_1.py` :
        ```python
        url = f'{ROOT}catalogue/the-boys-in-the-boat-nine-americans-and-their-epic-quest-for-gold-at-the-1936-berlin-olympics_992/index.html'
        ```
    - Remplacez l'URL après `ROOT` par celle d'un autre livre. Exemple :
        ```python
        url = f'{ROOT}catalogue/a-light-in-the-attic_1000/index.html'
        ```
    - **Attention :** L'URL doit inclure le chemin relatif du livre (ne pas modifier `ROOT`). 
    - Et, **évidemment**, le livre doit provenir du site.

---

### **Script 2 : Scraper une catégorie complète**
- **Commande :**
    ```bash
    python phase_2.py
    ```

- **Modification possible :**
    - Localisez cette ligne dans `script_phase_2.py` :
        ```python
        category_url = f'{ROOT}catalogue/category/books/historical-fiction_4/'
        ```
    - Remplacez l'URL de catégorie par celle de votre choix. Exemple pour la catégorie "Science" :
        ```python
        category_url = f'{ROOT}catalogue/category/books/science_22/'
        ```
    - **Astuce :** Les noms de catégories sont visibles sur la page d'accueil de *Books to Scrape*.

---

### **Script 3 : Scraper toutes les catégories**
- **Commande :**
    ```bash
    python phase_3.py
    ```

- **Option : Télécharger les images de couvertures dans des dossiers par catégorie et nommées d'après le livre qu'elles représentent**
    - Activez l'option `keep_images=True` dans la fonction `scrape_all_categories`.

---

### **Script 4 : Automatiser toutes les phases**
- **Commande :**
    ```bash
    python phase_4.py
    ```