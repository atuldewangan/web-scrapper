import traceback
from typing import List
import requests
import time
from bs4 import BeautifulSoup
from app.constant import FILE_PATH, WEBSITE_TO_SCRAP


class Scraper:
    def __init__(self, proxy: str = None):
        self.proxy = {"http": proxy, "https": proxy} if proxy else None

    def scrape(self, num_pages: int) -> List[dict]:
        # Function to scrape the target website
        # Returns a list of dictionaries containing product information
        scraped_data = []
        for page_num in range(1, num_pages + 1):
            url = f"{WEBSITE_TO_SCRAP}/{page_num}/"
            try:
                response = requests.get(url, proxies=self.proxy)
                if response.status_code == 200:
                    # Extract product information from the page
                    soup = BeautifulSoup(response.content, 'html.parser')
                    for index, row in enumerate(soup.select('ul.products.columns-4 li')):
                        try: 
                            title_element = row.find('h2', class_='woo-loop-product__title')
                            product_title = title_element.text.strip()
                            price_element = row.find('span', class_='woocommerce-Price-amount amount')
                            product_price = price_element.text[1:]
                            a= row.find('div', class_='mf-product-thumbnail').find('a')
                            b= a.find('noscript')
                            c= b.find('img')
                            d= c['src']
                            image_element = row.find('div', class_='mf-product-thumbnail').find('a').find('noscript').find('img')

                            image_url = image_element['src']

                            imageResponse = requests.get(image_url)
                            image_data = imageResponse.content
                            save_path =  FILE_PATH + product_title + '.jpg'
                            with open(save_path, 'wb') as f:
                                f.write(image_data)

                            scraped_data.extend([{"product_title": product_title, "product_price": product_price, "path_to_image": save_path}])
                       
                        except Exception as e:
                            print(f"Failed to scrape page {page_num}. row number: {index} Error: {str(e)}")


                else:
                    print(f"Failed to scrape page {page_num}. Status code: {response.status_code}")
            except Exception as e:
                traceback.print_exc(e)
                print(f"Failed to scrape page {page_num}. Error: {str(e)}")
            time.sleep(1)  # Adding a delay before making another request (rate limiting)
        return scraped_data
