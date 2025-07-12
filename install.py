#!/usr/bin/env python3
"""
Installation script for Musalist Advertisement Automation System
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n{description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def main():
    """Main installation function"""
    print("=" * 60)
    print("Musalist Advertisement Automation System - Installation")
    print("=" * 60)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("✗ Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    
    print(f"✓ Python version: {sys.version.split()[0]}")
    
    # Install Python dependencies
    if not run_command("pip install -r requirements.txt", "Installing Python dependencies"):
        print("\nFailed to install dependencies. Please try:")
        print("1. Ensure pip is installed and up to date")
        print("2. Check your internet connection")
        print("3. Try running: pip install --upgrade pip")
        sys.exit(1)
    
    # Install Playwright browsers
    if not run_command("playwright install", "Installing Playwright browsers"):
        print("\nFailed to install Playwright browsers. Please try:")
        print("1. Ensure you have sufficient disk space")
        print("2. Check your internet connection")
        print("3. Try running: playwright install --force")
        sys.exit(1)
    
    # Create necessary directories if they don't exist
    directories = ['automation', 'gui', 'utils']
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
    
    print("\n" + "=" * 60)
    print("✓ Installation completed successfully!")
    print("=" * 60)
    print("\nTo start the application, run:")
    print("python main.py")
    print("\nFor more information, see README.md")

if __name__ == "__main__":
    main() 