import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Function to set up Selenium WebDriver
def get_driver():
    service = Service(ChromeDriverManager().install())  # Auto-install ChromeDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in background (optional)
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# Function to download images
def download_images(query, folder, num_images=100):
    driver = get_driver()
    search_url = f"https://www.google.com/search?q={query}&tbm=isch"
    driver.get(search_url)

    os.makedirs(folder, exist_ok=True)
    image_urls = set()
    count = 0

    # Scroll to load more images
    for _ in range(5):  
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(2)

    images = driver.find_elements(By.TAG_NAME, "img")

    for img in images:
        src = img.get_attribute("src")
        if src and "http" in src:
            image_urls.add(src)

    # Download images
    for i, url in enumerate(image_urls):
        try:
            img_data = requests.get(url).content
            with open(os.path.join(folder, f"{i+1}.jpg"), "wb") as f:
                f.write(img_data)
            count += 1
            print(f"Downloaded {count} images: {url}")
            if count >= num_images:
                break
        except Exception as e:
            print(f"Error downloading {url}: {e}")
            continue

    driver.quit()
    print(f"✅ {count} images downloaded in {folder}")

# Download images for sunrise and sunset
download_images("sunrise landscape", "dataset/sunrise", 100)
download_images("sunset landscape", "dataset/sunset", 100)

