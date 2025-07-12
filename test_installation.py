#!/usr/bin/env python3
"""
Test script to verify Musalist Automation System installation
"""

import sys
import importlib
from pathlib import Path

def test_import(module_name, description):
    """Test if a module can be imported"""
    try:
        importlib.import_module(module_name)
        print(f"✓ {description}")
        return True
    except ImportError as e:
        print(f"✗ {description}: {e}")
        return False

def test_file_exists(file_path, description):
    """Test if a file exists"""
    if Path(file_path).exists():
        print(f"✓ {description}")
        return True
    else:
        print(f"✗ {description}: File not found")
        return False

def main():
    """Main test function"""
    print("=" * 60)
    print("Musalist Automation System - Installation Test")
    print("=" * 60)
    
    tests_passed = 0
    total_tests = 0
    
    # Test Python version
    total_tests += 1
    if sys.version_info >= (3, 8):
        print(f"✓ Python version: {sys.version.split()[0]}")
        tests_passed += 1
    else:
        print(f"✗ Python version: {sys.version.split()[0]} (3.8+ required)")
    
    # Test required modules
    required_modules = [
        ("playwright", "Playwright web automation"),
        ("cryptography", "Cryptography for secure storage"),
        ("PIL", "Pillow for image processing"),
        ("requests", "Requests for HTTP operations"),
        ("dotenv", "Python-dotenv for environment variables"),
    ]
    
    for module, description in required_modules:
        total_tests += 1
        if test_import(module, description):
            tests_passed += 1
    
    # Test project files
    required_files = [
        ("main.py", "Main application entry point"),
        ("config.py", "Configuration file"),
        ("requirements.txt", "Dependencies file"),
        ("automation/musalist_automation.py", "Automation module"),
        ("gui/main_window.py", "GUI module"),
        ("utils/encryption.py", "Encryption utilities"),
    ]
    
    for file_path, description in required_files:
        total_tests += 1
        if test_file_exists(file_path, description):
            tests_passed += 1
    
    # Test project imports
    try:
        from config import Config
        print("✓ Project configuration loaded")
        tests_passed += 1
        total_tests += 1
    except Exception as e:
        print(f"✗ Project configuration: {e}")
        total_tests += 1
    
    # Summary
    print("\n" + "=" * 60)
    print(f"Test Results: {tests_passed}/{total_tests} tests passed")
    print("=" * 60)
    
    if tests_passed == total_tests:
        print("✓ All tests passed! Installation is complete.")
        print("\nYou can now run the application with:")
        print("python main.py")
    else:
        print("✗ Some tests failed. Please check the errors above.")
        print("\nTo fix installation issues:")
        print("1. Run: python install.py")
        print("2. Or manually install dependencies: pip install -r requirements.txt")
        print("3. Install Playwright browsers: playwright install")
    
    return tests_passed == total_tests

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 