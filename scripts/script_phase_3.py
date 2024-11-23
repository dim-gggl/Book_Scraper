import requests
from bs4 import BeautifulSoup
import os
from script_phase_1 import (ROOT, HEADERS, OUTPUT_FILE_PATH)
from script_phase_2 import (scrape_category, save_category_datas)


def download_images(image_url, category_name, book_title):
    """
    Download and save an image its category named repertory
    :param image_url : string with the image url
    :param category_name: string with the category name
    :param book_title: string with the book title to name the image after it
    :return: None
    """
    image_output_dir = os.path.join(OUTPUT_FILE_PATH, "images", category_name)
    image_name = f"{book_title}.jpg"
    save_path = os.path.join(image_output_dir, image_name)

    try:
        response = requests.get(image_url, stream=True)

        os.makedirs(image_output_dir, exist_ok=True)

        with open(save_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)

    except Exception as e:
        print(f"Error while downloading image {image_url}: {e}")


def scrape_all_categories(ROOT, keep_images=False):
    """
    Scrape all the categories
    :param root: the homepage url
    :param keep_images: False : extract each book details for every category
    :param keep_images: True : extract only the image of each book
    :return:
    """
    response = requests.get(ROOT)
    soup = BeautifulSoup(response.text, 'html.parser')

    category_tags = soup.find('ul', class_="nav nav-list").find_all('a')[1:]
    for tag in category_tags:
            relative_url = tag['href']
            category_url = ROOT + relative_url
            category_name = tag.text.strip()

            print(f"Scraping category : {category_name}")
            category_books_data = scrape_category(category_url)

            if category_books_data:
                save_category_datas(HEADERS, OUTPUT_FILE_PATH, category_name, category_books_data)

                if keep_images:
                    print(f"Downloading images from {category_name} category")
                    for book in category_books_data:
                        image_url = book[-1]
                        book_title = book[2]
                        download_images(image_url, category_name, book_title)

                print(f"{category_name} book details has been saved successfully.")
            else:
                print(f"Error : impossible to scrape the {category_name} pages")


if __name__ == '__main__':
    scrape_all_categories(ROOT, keep_images=False)
    print("All categories scraped!")