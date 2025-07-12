import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Encryption key for secure credential storage
    ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY', Fernet.generate_key())
    
    # Website URLs
    LOGIN_URL = "https://www.musalist.com:442/mainpage/business/account/member_login.asp"
    MAIN_PAGE_URL = "https://www.musalist.com:442/mainpage/business/index.asp"
    
    # Account credentials (encrypted)
    POWER_LISTINGS_EMAIL = "jptrading2014@gmail.com"
    POWER_LISTINGS_PASSWORD = "car4989"
    PERSONAL_LISTINGS_EMAIL = "parksunghwak@gmail.com"
    PERSONAL_LISTINGS_PASSWORD = "car4989"
    
    # Automation settings
    SCAN_INTERVAL = 300  # 5 minutes
    MAX_POWER_ADS = 5
    MAX_PERSONAL_ADS = 1
    MAX_PERSONAL_ADS_PER_DAY = 1
    
    # Competitor detection keywords
    COMPETITOR_KEYWORDS = [
        "car", "vehicle", "automobile", "trading", "import", "export",
        "dealer", "wholesale", "retail", "price", "discount"
    ]
    
    # UI Settings
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 800
    THEME_COLOR = "#2c3e50"
    ACCENT_COLOR = "#3498db"
    SUCCESS_COLOR = "#27ae60"
    WARNING_COLOR = "#f39c12"
    ERROR_COLOR = "#e74c3c"
    
    # Advertisement templates
    DEFAULT_AD_TEMPLATES = {
        "power_listings": {
            "title": "Professional Vehicle Trading Services",
            "content": "High-quality vehicles available for wholesale and retail. Competitive prices and excellent service.",
            "price_range": "$10,000 - $50,000"
        },
        "personal_listings": {
            "title": "Personal Vehicle Sales",
            "content": "Quality vehicles for personal use. Great deals and reliable service.",
            "price_range": "$5,000 - $25,000"
        }
    } 