import requests
from bs4 import BeautifulSoup
import os
from phase_1 import (ROOT, OUTPUT_FILE_PATH)
from phase_2 import (scrape_category, save_category_datas)
from utils import get_categories_urls


def download_images(
    image_url: str,
    category_name: str,
    book_title: str
    ) -> None:
    """
    Download and save an image its category named repertory
    :param image_url : string with the image url
    :param category_name: string with the category name
    :param book_title: string with the book title to name the image after it
    :return: None
    """
    image_output_dir = os.path.join(
        OUTPUT_FILE_PATH,
        "Categories",
        category_name,
        "Images"
        )
    image_name = f"{book_title.replace("/", "_")}.jpg"
    save_path = os.path.join(
        image_output_dir, image_name
        )

    try:
        response = requests.get(
            image_url,
            stream=True
            )

        os.makedirs(
            image_output_dir,
            exist_ok=True
            )

        with open(
            save_path,
            "wb"
            ) as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)

    except Exception as e:
        print(f"Error while downloading image {image_url}: {e}")


def scrape_all_categories(keep_images=False):
    """
    Scrape all the categories
    :param root: the homepage url
    :param keep_images: False : extract each book details for every category
    :param keep_images: True : extract only the image of each book
    :return:
    """
    categories_urls = get_categories_urls()

    for k, v in categories_urls.items():
            category_url = v
            category_name = k

            category_output_dir = os.path.join(
                OUTPUT_FILE_PATH,
                "Categories",
                category_name
                )

            os.makedirs(
                category_output_dir,
                exist_ok=True
                )

            print(
                f"Scraping category : {category_name}"
                )

            category_name_extracted, category_books_data = scrape_category(category_url)

            if category_books_data:
                output_file = os.path.join(
                    category_output_dir,
                    f"{category_name}_product_details.csv"
                    )

                save_category_datas(
                    category_name_extracted,
                    category_books_data,
                    output_file
                    )

                if keep_images:
                    print(
                        f"Downloading images from {category_name} category"
                        )
                    for book in category_books_data:
                        image_url = book[-1]
                        book_title = book[2]
                        download_images(
                            image_url,
                            category_name_extracted,
                            book_title
                            )

                print(
                    f"{category_name} book details has been saved successfully."
                    )
            else:
                print(
                    f"Error : impossible to scrape the {category_name} pages"
                    )


if __name__ == '__main__':
    scrape_all_categories(keep_images=False)
    print("All categories scraped!")
