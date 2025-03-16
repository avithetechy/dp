import time
import random
import google.generativeai as genai
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Configure Google Gemini API
genai.configure(api_key="AIzaSyClP0lYfgl9G3LTxkvL8ViRVQ_hNj4ddyo")
model = genai.GenerativeModel('gemini-1.5-flash')

# Initialize Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (no UI)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def fetch_amazon_product(search_query):
    """Fetch product name and price from Amazon"""
    base_url = "https://www.amazon.in/s?k="
    driver.get(base_url + search_query.replace(" ", "+"))
    time.sleep(3)

    # Extract page source and parse with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")
    product = soup.find("div", {"class": "s-main-slot"}).find("div", {"data-component-type": "s-search-result"})

    if product:
        try:
            name = product.find("span", {"class": "a-size-medium"}).text.strip()
            price = product.find("span", {"class": "a-price-whole"}).text.strip()
            return name, f"₹{price}"
        except:
            return "amaz", "80"
    return None, None

def fetch_flipkart_product(search_query):
    """Fetch product name and price from Flipkart"""
    base_url = "https://www.flipkart.com/search?q="
    driver.get(base_url + search_query.replace(" ", "+"))
    time.sleep(3)

    # Extract page source and parse with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")
    product = soup.find("div", {"class": "_1AtVbE"})

    if product:
        try:
            name = product.find("a", {"class": "IRpwTa"}).text.strip()
            price = product.find("div", {"class": "_30jeq3"}).text.strip()
            return name, price
        except:
            return "flip", "90"
    return None, None

def clean_with_gemini(product_name, price):
    """Use Gemini to clean and structure product details"""
    prompt = f"""
    Format the following product details into structured data:
    Product Name: {product_name}
    Price: {price}
    
    Return output only in this format:
    Product Name: <Formatted Product Name>
    Price: <Formatted Price>
    """
    response = model.generate_content(prompt)
    
    if response.candidates and response.candidates[0].content:
        text_output = response.candidates[0].content.parts[0].text.strip()
        lines = text_output.split('\n')
        name, price = None, None
        for line in lines:
            if "Product Name:" in line:
                name = line.split("Product Name:")[1].strip()
            elif "Price:" in line:
                price = line.split("Price:")[1].strip()
        return name, price
    return None, None

# Example Product Search List
products = ["Samsung Galaxy A35 5G", "Apple iPhone 15 Pro", "OnePlus Nord CE 3 Lite"]

# Store extracted details in prolst
prolst = []
for product in products:
    amazon_name, amazon_price = fetch_amazon_product(product)
    flipkart_name, flipkart_price = fetch_flipkart_product(product)

    # Clean response using Gemini
    amazon_name, amazon_price = clean_with_gemini(amazon_name, amazon_price) if amazon_name and amazon_price else (None, None)
    flipkart_name, flipkart_price = clean_with_gemini(flipkart_name, flipkart_price) if flipkart_name and flipkart_price else (None, None)

    if amazon_name and amazon_price:
        prolst.append((amazon_name, amazon_price))
    if flipkart_name and flipkart_price:
        prolst.append((flipkart_name, flipkart_price))

# Close Selenium WebDriver
driver.quit()

# Display the extracted product list
print(prolst)
