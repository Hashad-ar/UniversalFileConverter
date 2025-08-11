#!/usr/bin/env python3
"""
Universal File Converter - Main Entry Point
Author: AbdelRahman

This is the main entry point for the Universal File Converter application.
Import and use the various converter modules from the src directory.
"""

import sys
import os

# Add src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src import audio_converter
from src import video_converter
from src import image_converter
from src import doc_converter
from src import file_formats
from src import output_selection
from src import folder_initializer
from src import extension_manager

def main():
    """
    Main function to run the Universal File Converter
    """
    print("Universal File Converter")
    print("=" * 50)
    print("Available converters:")
    print("1. Audio Converter")
    print("2. Video Converter") 
    print("3. Image Converter")
    print("4. Document Converter")
    print("=" * 50)
    
    # Add your main application logic here
    pass

if __name__ == "__main__":
    main()
