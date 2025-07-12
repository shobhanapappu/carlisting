from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import os
from config import Config


# --- LOGIN LOGIC ---
def login(driver):
    try:
        driver.get(Config.LOGIN_URL)
        time.sleep(2)  # Wait 5 seconds after navigating to login URL

        driver.find_element(By.NAME, "bus_id").send_keys(Config.POWER_LISTINGS_EMAIL)
        time.sleep(2)  # Wait 5 seconds after filling email

        driver.find_element(By.NAME, "password").send_keys(Config.POWER_LISTINGS_PASSWORD)
        time.sleep(2)  # Wait 5 seconds after filling password

        driver.find_element(By.XPATH, "//input[@type='image']").click()
        time.sleep(2)  # Wait 5 seconds after clicking login button

        # Check login success (look for logout or user menu, or check URL)
        current_url = driver.current_url
        if "index.asp" in current_url or "mainpage" in current_url:
            print("Successfully logged in to POWER account.")
            return True
        else:
            print("Login failed. Current URL:", current_url)
            return False
    except Exception as e:
        print(f"Login error: {e}")
        return False


# Read data directly from output.xlsx file
try:
    df = pd.read_excel("output.xlsx")
    if len(df) > 0:
        # Get the first row
        row = df.iloc[0]
        title = row.get('Title', 'N/A')
        location = row.get('Location', 'N/A')
        mileage = row.get('Mileage', 'N/A')
        year = row.get('Year', 'N/A')
        price = row.get('Price', 'N/A')
        image_path = row.get('Local_Image_Path', 'N/A')
        description = row.get('Description', 'N/A')

        print(f"Loaded data from output.xlsx:")
        print(f"Title: {title}")
        print(f"Location: {location}")
        print(f"Mileage: {mileage}")
        print(f"Year: {year}")
        print(f"Price: {price}")
        print(f"Image Path: {image_path}")
        print(f"Description: {description[:100]}...")  # Show first 100 chars
    else:
        print("output.xlsx file is empty. Using default values.")
        title = "7월 손님이 원하는가격! ◈ 저렴한 리스 ◈ 스페셜/리스리턴/중고차량 최고가격 매입/시간상관없이 연락주세요 562-760-6295 대니입니다!"
        location = "[Fullerton / CA]"
        mileage = "1Miles"
        year = "2025년식"
        price = "$50"
        image_path = "Image/power_0_20250710_170941.jpg"
        description = "안녕하세요! PEOPLE & MOTORS 의 자동차 전문가 대니입니다. 오렌지 카운티 플러튼 은혜 한인 교회 옆에 위치하며 캘리포니아 DMV 정식허가 된 딜러로써 책임감을 갖고 고객님이 원하는 차량을 최적의 조건으로 알려드립니다. 다른곳 보다 무조건 저렴하게 알려드릴께요! ✨ 오렌지카운티 & 로스엔젤레스 판매 1등 딜러 ✨ 가장 많이 판매하는 회사로써 손님들이 원하는 가격으로 최대한 저렴하게 안내할수 있도록 최선을 다하겠습니다. 감사합니다! ☎️ DANNY 대니 562-760-6295"
except Exception as e:
    print(f"Error reading output.xlsx: {e}")
    print("Using default values.")
    title = "7월 손님이 원하는가격! ◈ 저렴한 리스 ◈ 스페셜/리스리턴/중고차량 최고가격 매입/시간상관없이 연락주세요 562-760-6295 대니입니다!"
    location = "[Fullerton / CA]"
    mileage = "1Miles"
    year = "2025년식"
    price = "$50"
    image_path = "Image/power_0_20250710_170941.jpg"
    description = "안녕하세요! PEOPLE & MOTORS 의 자동차 전문가 대니입니다. 오렌지 카운티 플러튼 은혜 한인 교회 옆에 위치하며 캘리포니아 DMV 정식허가 된 딜러로써 책임감을 갖고 고객님이 원하는 차량을 최적의 조건으로 알려드립니다. 다른곳 보다 무조건 저렴하게 알려드릴께요! ✨ 오렌지카운티 & 로스엔젤레스 판매 1등 딜러 ✨ 가장 많이 판매하는 회사로써 손님들이 원하는 가격으로 최대한 저렴하게 안내할수 있도록 최선을 다하겠습니다. 감사합니다! ☎️ DANNY 대니 562-760-6295"

# Use description directly
d = description

# Set up Selenium WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Perform login before posting
if not login(driver):
    driver.quit()
    exit()

driver.get(
    "https://www.musalist.com:442/mainpage/business/cars/cars_write.asp?id=busi2")  # Replace with actual URL if different
time.sleep(2)  # Wait 5 seconds after navigating to form page


# Function to fill form fields with try-except and sleep
def fill_field(field_name, value, by_method=By.NAME, element_type="input"):
    try:
        if element_type == "select":
            element = Select(driver.find_element(by_method, field_name))
            element.select_by_visible_text(value)
        else:
            element = driver.find_element(by_method, field_name)
            # Scroll to element first
            driver.execute_script("arguments[0].scrollIntoView();", element)
            time.sleep(2)  # Wait 5 seconds after scrolling to field

            element.clear()
            time.sleep(2)  # Wait 5 seconds after clearing field

            element.send_keys(value)
            time.sleep(2)  # Wait 5 seconds after filling field

        print(f"Successfully filled {field_name} with {value}")
    except Exception as e:
        print(f"Error filling {field_name}: {e}")
    time.sleep(2)


# Fill form fields
# Title
fill_field("txtTitle", title)

# Parse location (assuming format "City, State")
if location != 'N/A':
    try:
        # Handle different location formats
        if ", " in location:
            # Format: "City, State" (e.g., "Fullerton, California")
            city, state_full_name = location.split(", ", 1)
        elif " / " in location:
            # Format: "[City / State]" (e.g., "[Fullerton / CA]")
            city, state_abbr = location.strip("[]").split(" / ")

            # Convert state abbreviation to full name
            state_mapping = {
                "AK": "Alaska", "AL": "Alabama", "AR": "Arkansas", "AZ": "Arizona",
                "CA": "California", "CO": "Colorado", "CT": "Connecticut",
                "DC": "District of Columbia", "DE": "Delaware", "FL": "Florida",
                "GA": "Georgia", "HI": "Hawaii", "IA": "Iowa", "ID": "Idaho",
                "IL": "Illinois", "IN": "Indiana", "KS": "Kansas", "KY": "Kentucky",
                "LA": "Louisiana", "MA": "Massachusetts", "MD": "Maryland",
                "ME": "Maine", "MI": "Michigan", "MN": "Minnesota", "MO": "Missouri",
                "MS": "Mississippi", "MT": "Montana", "NC": "North Carolina",
                "ND": "North Dakota", "NE": "Nebraska", "NH": "New Hampshire",
                "NJ": "New Jersey", "NM": "New Mexico", "NV": "Nevada",
                "NY": "New York", "OH": "Ohio", "OK": "Oklahoma", "OR": "Oregon",
                "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina",
                "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas", "UT": "Utah",
                "VA": "Virginia", "VT": "Vermont", "WA": "Washington",
                "WI": "Wisconsin", "WV": "West Virginia", "WY": "Wyoming"
            }
            state_full_name = state_mapping.get(state_abbr, state_abbr)
        else:
            # Single value, assume it's the city
            city = location
            state_full_name = "California"  # Default state

        print(f"Parsed location - City: {city}, State: {state_full_name}")

        # State
        fill_field("state", state_full_name, element_type="select")
        # City
        fill_field("city", city)

    except Exception as e:
        print(f"Error parsing location '{location}': {e}")
        print("Using default location values")
        fill_field("state", "California", element_type="select")
        fill_field("city", "Fullerton")
else:
    print("Location data is N/A, skipping location fields")

# Year (remove "년식" from year)
if year != 'N/A':
    year_clean = year.replace("년식", "")
    fill_field("vyear", year_clean)
else:
    print("Year data is N/A, skipping year field")

# Price (remove "$" from price)
if price != 'N/A':
    price_clean = price.replace("$", "")
    fill_field("txtPrice", price_clean)
else:
    print("Price data is N/A, skipping price field")

# Mileage (remove "Miles" from mileage)
if mileage != 'N/A':
    mileage_clean = mileage.replace("Miles", "")
    fill_field("mileage", mileage_clean)
else:
    print("Mileage data is N/A, skipping mileage field")

# Optional: Add more fields as needed (e.g., carkind, maker, model, etc.)
# Example for car kind (assuming a default value since not in Excel)
fill_field("carkind", "Sedans", element_type="select")

# Handle image upload using the local image path
if image_path != 'N/A' and os.path.exists(image_path):
    try:
        image_input = driver.find_element(By.ID, "txtAttachImage1")
        # Scroll to image input
        driver.execute_script("arguments[0].scrollIntoView();", image_input)
        time.sleep(2)  # Wait 5 seconds after scrolling to image input

        # Convert path to absolute path for Selenium
        absolute_image_path = os.path.abspath(image_path)
        image_input.send_keys(absolute_image_path)
        time.sleep(2)  # Wait 5 seconds after uploading image

        print(f"Successfully uploaded image: {absolute_image_path}")
    except Exception as e:
        print(f"Error uploading image: {e}")
else:
    print(f"Image not found at path: {image_path}")
time.sleep(2)

try:
    # Switch to the iframe using its id
    driver.switch_to.frame("editCtrl")

    # Locate the body element and clear its existing content
    body = driver.find_element(By.TAG_NAME, "body")
    body.clear()

    # Send the description text to the body
    body.send_keys(d)

    # Switch back to the main document
    driver.switch_to.default_content()

except Exception as e:
    print(f"The description is not entered {e}")

# Optional: Submit the form (uncomment to submit)
try:
    submit_button = driver.find_element(By.XPATH, "//img[@alt='등록하기']")
    # Scroll to submit button
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)
    time.sleep(2)  # Wait 5 seconds after scrolling to submit button

    submit_button.click()
    time.sleep(2)  # Wait 5 seconds after clicking submit button

    print("Form submitted successfully")
except Exception as e:
    print(f"Error submitting form: {e}")
time.sleep(2)

# Close the browser
# driver.quit()
