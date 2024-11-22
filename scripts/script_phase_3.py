import requests
from bs4 import BeautifulSoup
from script_phase_1 import (root, product_data_headers, output_file_rep)
from script_phase_2 import (scrape_category, save_category_datas)


def scrape_all_categories(root, keep_images=False):
    """
    Scrape all the categories
    :param root: the homepage url
    :param keep_images: False : extract each book details for every category
    :param keep_images: True : extract only the image of each book
    :return:
    """
    if keep_images:
        print("We are gonna keep the images on  next script")
    else:
        response = requests.get(root)
        soup = BeautifulSoup(response.text, 'html.parser')
        print("requests et soup ok")

        category_tags = soup.find('ul', class_="nav nav-list").find_all('a')[1:]

        for tag in category_tags:
            relative_url = tag['href']
            category_url = root + relative_url
            category_name = tag.text.strip()


            print(f"Scraping category : {category_name}")
            category_books_data = scrape_category(category_url)

            if category_books_data:
                save_category_datas(product_data_headers, output_file_rep, category_name, category_books_data)
                print(f"{category_name} book details has been saved successfully.")
            else:
                print(f"Error : impossible to scrape the {category_name} pages")


if __name__ == '__main__':
    scrape_all_categories(root, keep_images=False)
    print("All categories scraped!")