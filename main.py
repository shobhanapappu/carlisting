#!/usr/bin/env python3
"""
Musalist Advertisement Automation System
Main entry point for the application
"""

import sys
import os
import asyncio
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def main():
    """Main entry point for the application"""
    try:
        # Import and run the GUI
        from gui.main_window import MainWindow
        
        # Create and run the main window
        app = MainWindow()
        app.run()
        
    except ImportError as e:
        print(f"Import error: {e}")
        print("Please make sure all dependencies are installed:")
        print("pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        print(f"Application error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
