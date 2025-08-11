"""
Universal File Converter Package

This package provides various file conversion utilities:
- Audio conversion
- Video conversion  
- Image conversion
- Document conversion

Author: AbdelRahman
"""

__version__ = "1.0.0"
__author__ = "AbdelRahman"

# Import main modules for easy access
from . import audio_converter
from . import video_converter
from . import image_converter
from . import doc_converter
from . import file_formats
from . import output_selection
from . import folder_initializer
from . import extension_manager

__all__ = [
    'audio_converter',
    'video_converter', 
    'image_converter',
    'doc_converter',
    'file_formats',
    'output_selection',
    'folder_initializer',
    'extension_manager'
]
