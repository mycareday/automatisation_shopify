import requests
from bs4 import BeautifulSoup

def scrape_tiktok_trends():
    url = "https://www.tiktok.com/trending"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    trending_products = []
    for item in soup.find_all("div", class_="trend-item"):
        product_name = item.find("span", class_="product-name").text
        product_url = item.find("a", href=True)['href']
        trending_products.append((product_name, product_url))
    
    # Save to database or file
    with open('trending_products.txt', 'w') as file:
        for product in trending_products:
            file.write(f"{product[0]} - {product[1]}\n")
    
    print(f"Found {len(trending_products)} trending products.")
