# Musalist Advertisement Automation System

A comprehensive automation system for managing advertisements on the Musalist platform. This system provides automatic competitor detection, advertisement management, and dual account support.

## Features

### Core Functionality
- **Dual Account Management**: Simultaneous management of Power Listings and Personal Listings accounts
- **Competitor Detection**: Automatic detection of competitor advertisements using keyword analysis
- **Automated Advertisement Management**: 
  - Power Listings: Up to 5 advertisements
  - Personal Listings: 1 advertisement per day
- **Secure Credential Storage**: Encrypted storage of account credentials
- **Responsive GUI**: Modern, multi-device responsive interface

### Automation Features
- **Automatic Login**: Seamless login to both accounts
- **Competitor Alert System**: Real-time detection and alerts
- **Automatic Deletion**: Remove existing advertisements based on account limits
- **New Advertisement Registration**: Create new ads with custom content and images
- **Settings Management**: Modify advertisement templates and automation settings

## Installation

### Prerequisites
- Python 3.8 or higher
- Windows 10/11 (tested on Windows 10)

### Setup Instructions

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd PROJECT_3_1
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Playwright browsers**
   ```bash
   playwright install
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

## Configuration

### Account Setup
The system comes pre-configured with the following accounts:

**Power Listings Account:**
- Email: jptrading2014@gmail.com
- Password: car4989

**Personal Listings Account:**
- Email: parksunghwak@gmail.com
- Password: car4989

### Customization
You can modify account credentials and settings through the GUI:
1. Go to the "Account Management" tab
2. Update email and password fields
3. Click "Save Credentials"

## Usage

### Starting Automation
1. Launch the application: `python main.py`
2. Navigate to the "Control Panel" tab
3. Click "Start Automation"
4. The system will automatically:
   - Login to both accounts
   - Begin monitoring for competitor advertisements
   - Manage advertisements according to account limits

### Monitoring
- **Status Display**: Real-time status of both accounts
- **Statistics**: Track competitors detected, ads deleted, and ads created
- **Logs**: Detailed logs of all automation activities

### Settings Management
- **Advertisement Templates**: Customize ad content for both accounts
- **Automation Settings**: Adjust scanning intervals and limits
- **Competitor Keywords**: Modify detection keywords

## Project Structure

```
PROJECT_3_1/
├── main.py                 # Main application entry point
├── requirements.txt        # Python dependencies
├── config.py              # Configuration settings
├── README.md              # This file
├── automation/
│   └── musalist_automation.py  # Core automation logic
├── gui/
│   └── main_window.py     # GUI implementation
└── utils/
    └── encryption.py      # Secure credential management
```

## Technical Details

### Technology Stack
- **Python 3.8+**: Core programming language
- **Playwright**: Web automation and browser control
- **Tkinter**: GUI framework
- **Cryptography**: Secure credential encryption
- **Pillow**: Image processing support

### Security Features
- **Encrypted Credentials**: All account credentials are encrypted using Fernet
- **Secure Storage**: Credentials stored in encrypted files
- **Session Management**: Separate browser contexts for each account

### Automation Logic
1. **Competitor Detection**: Scans for advertisements containing predefined keywords
2. **Account Separation**: Maintains separate sessions for each account
3. **Advertisement Limits**: Enforces account-specific advertisement limits
4. **Error Handling**: Robust error handling and logging

## Troubleshooting

### Common Issues

**1. Browser Installation Issues**
```bash
# Reinstall Playwright browsers
playwright install --force
```

**2. Login Failures**
- Verify account credentials in the "Account Management" tab
- Check internet connection
- Ensure the target website is accessible

**3. Automation Not Starting**
- Check the logs tab for error messages
- Verify all dependencies are installed
- Ensure browser is properly installed

### Log Files
- **automation.log**: Detailed automation logs
- **credentials.enc**: Encrypted credential storage

## Development

### Adding New Features
1. **Competitor Keywords**: Modify `Config.COMPETITOR_KEYWORDS`
2. **Advertisement Templates**: Update `Config.DEFAULT_AD_TEMPLATES`
3. **Automation Settings**: Adjust `Config.SCAN_INTERVAL` and limits

### Testing
- Test individual components before full automation
- Monitor logs for debugging
- Use the GUI for manual testing

## Support

For issues or questions:
1. Check the logs tab for error messages
2. Review the troubleshooting section
3. Ensure all dependencies are properly installed

## License

This project is developed for educational and business automation purposes.

---

**Note**: This system is designed for legitimate business automation. Please ensure compliance with the target website's terms of service and applicable laws. #   c a r l i s t i n g  
 