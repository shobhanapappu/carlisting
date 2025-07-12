import os
import pandas as pd
import requests
import uuid
from datetime import datetime
from bs4 import BeautifulSoup

# Load the HTML file
html_file = "POWER_EDIT_PAGE_1_20250710_205804.html"  # Path to your HTML file

# Read the HTML file content
with open(html_file, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Create images folder if it doesn't exist
images_folder = "images"
if not os.path.exists(images_folder):
    os.makedirs(images_folder)

# Extract title
title_element = soup.find('input', {'name': 'txtTitle'})
title = title_element['value'] if title_element else ''

# Extract author and account type
name_td = soup.find('img', {'alt': '이름'}).find_parent('td').find_next_sibling('td', {'class': 'default_14', 'style': 'padding-left:30px;'})
author = name_td.get_text(strip=True).replace('파워딜러', '').strip() if name_td else ''
account_type_element = name_td.find('span', {'class': 'dealer_nu'}) if name_td else None
account_type = account_type_element.get_text(strip=True) if account_type_element else ''

# Extract location (state and city)
state_element = soup.find('select', {'name': 'state'}).find('option', selected=True)
state = state_element.get_text(strip=True) if state_element else ''
city_element = soup.find('input', {'name': 'city'})
city = city_element['value'] if city_element else ''
location = f"{city}, {state}" if city and state else ''

# Extract year
year_element = soup.find('input', {'name': 'vyear'})
year = year_element['value'] if year_element else ''

# Extract price
price_element = soup.find('input', {'name': 'txtPrice'})
price = price_element['value'] if price_element else ''

# Extract mileage
mileage_element = soup.find('input', {'name': 'mileage'})
mileage = mileage_element['value'] if mileage_element else ''

# Get current date
date = datetime.now().strftime('%Y-%m-%d')

# Extract description and clean it
description_element = soup.find('textarea', {'name': 'txtText'})
description_raw = description_element.get_text(strip=True) if description_element else ''
description_soup = BeautifulSoup(description_raw, 'html.parser')
description = description_soup.get_text(separator=" ", strip=True).replace('\xa0', ' ')

# Extract image URL and Ad_IDX from oimgname for Photo 1
image_path_element = soup.find('input', {'name': 'oimgname', 'value': lambda x: x and x != ''})
image_path = image_path_element['value'] if image_path_element else ''
image_url = f"https://www.musalist.com:442{image_path}" if image_path else ''
ad_idx = ''
# if image_path:
#     path_parts = image_path.split('/')
#     if len(path_parts) > 3:  # Ensure path has enough segments
#         ad_idx = path_parts[-2]  # Extract '20257' from path

# Download image
image_local_path = ''
if image_url:
    image_filename = image_path.split('/')[-1]
    image_local_path = os.path.join(images_folder, f"{uuid.uuid4()}_{image_filename}")
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(image_local_path, 'wb') as f:
            f.write(response.content)
    else:
        image_local_path = "Failed to download"

# Prepare data for Excel
data = {
    'Title': [title],
    'Location': [location],
    'Mileage': [mileage],
    'Year': [year],
    'Author': [author],
    'Price': [price],
    'Date': [date],
    'Description': [description],
    'Image_URL': [image_url],
    'Local_Image_Path': [image_local_path],
    'Account_Type': [account_type],
    'Ad_IDX': [ad_idx]
}

# Create DataFrame and save to Excel
df = pd.DataFrame(data)
excel_path = "output.xlsx"
df.to_excel(excel_path, index=False)

print(f"Data extracted and saved to {excel_path}")