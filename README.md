# 🔄 Universal File Converter

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Hashad-ar/UniversalFileConverter/blob/main/AbdelRahman_Universal_File_Converter.ipynb)

A comprehensive, easy-to-use file conversion tool that supports multiple media formats including **audio**, **video**, **images**, and **documents**. Built with Python and designed for both developers and end-users.

## ✨ Features

- **🎵 Audio Conversion**: Convert between MP3, WAV, OGG, FLAC, M4A, WMA, AAC formats
- **🎬 Video Conversion**: Convert between MP4, AVI, MOV, WEBM, WMV, FLV, MKV, 3GP formats  
- **🖼️ Image Conversion**: Convert between JPG, PNG, GIF, BMP, TIFF, WEBP formats
- **📄 Document Conversion**: Convert between PDF, DOCX, DOC, PPT, PPTX, ODT, RTF, TXT formats
- **⚡ Batch Processing**: Convert multiple files at once
- **🎯 Smart Format Detection**: Automatically detects output format from file extension
- **🏗️ Modular Architecture**: Clean, organized codebase with separate converter modules
- **📊 Progress Tracking**: Built-in progress indicators for large file operations

## 🚀 Quick Start

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Hashad-ar/UniversalFileConverter.git
   cd UniversalFileConverter
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install system dependencies (for document conversion):**
   ```bash
   # Ubuntu/Debian
   sudo apt install libreoffice unoconv
   
   # macOS
   brew install libreoffice
   
   # Windows
   # Download and install LibreOffice from https://www.libreoffice.org/
   ```

### Basic Usage

```python
from src.audio_converter import audio_converter
from src.video_converter import video_converter
from src.image_converter import image_converter
from src.doc_converter import doc_converter

# Convert audio file
audio_converter("input.mp3", "output.wav")

# Convert video file  
video_converter("input.mp4", "output.avi")

# Convert image file
image_converter("input.png", "output.jpg")

# Convert document file
doc_converter("input.pdf", "output.docx")
```

### Run the Main Application

```bash
python main.py
```

## 📁 Project Structure

```
UniversalFileConverter/
├── 📄 AbdelRahman_Universal_File_Converter.ipynb  # Jupyter notebook demo
├── 📄 main.py                                     # Main application entry point
├── 📄 requirements.txt                            # Python dependencies
├── 📄 LICENSE                                     # MIT license
├── 📄 README.md                                   # This file
├── 📄 TODO.md                                     # Development roadmap
├── 📁 src/                                        # Source code modules
│   ├── 📄 __init__.py                            # Package initialization
│   ├── 📄 audio_converter.py                     # Audio conversion logic
│   ├── 📄 video_converter.py                     # Video conversion logic
│   ├── 📄 image_converter.py                     # Image conversion logic
│   ├── 📄 doc_converter.py                       # Document conversion logic
│   ├── 📄 extension_manager.py                   # File extension utilities
│   ├── 📄 file_formats.py                        # Supported format definitions
│   ├── 📄 folder_initializer.py                  # Directory management
│   └── 📄 output_selection.py                    # Output path management
├── 📁 samples/                                    # Sample files for testing
│   ├── 📁 audio/                                 # Audio sample files
│   ├── 📁 documents/                             # Document sample files
│   ├── 📁 images/                                # Image sample files
│   └── 📁 videos/                                # Video sample files
└── 📁 Converted Files/                           # Default output directory
    ├── 📁 Audio/
    ├── 📁 Documents/
    ├── 📁 Images/
    └── 📁 Videos/
```

## 🎯 Supported Formats

### 🎵 Audio Formats
- **Input**: MP3, WAV, OGG, FLAC, M4A, WMA, AAC
- **Output**: MP3, WAV, OGG, FLAC, M4A, WMA, AAC

### 🎬 Video Formats  
- **Input**: MP4, AVI, MOV, WEBM, WMV, FLV, MKV, 3GP
- **Output**: MP4, AVI, MOV, WEBM, WMV, FLV, MKV, 3GP

### 🖼️ Image Formats
- **Input**: JPG, JPEG, PNG, GIF, BMP, TIFF, WEBP
- **Output**: JPG, JPEG, PNG, GIF, BMP, TIFF, WEBP

### 📄 Document Formats
- **Input**: PDF, DOCX, DOC, PPT, PPTX, ODT, RTF, TXT, DOCM, ODP
- **Output**: PDF, DOCX, DOC, PPT, PPTX, ODT, RTF, TXT

## 💻 Advanced Usage

### Batch Conversion Example

```python
import os
from src.audio_converter import audio_converter

def batch_convert_audio(input_dir, output_dir, target_format):
    """Convert all audio files in a directory to target format"""
    os.makedirs(output_dir, exist_ok=True)
    
    for filename in os.listdir(input_dir):
        if filename.endswith(('.mp3', '.wav', '.ogg', '.flac', '.m4a')):
            input_path = os.path.join(input_dir, filename)
            output_filename = os.path.splitext(filename)[0] + f'.{target_format}'
            output_path = os.path.join(output_dir, output_filename)
            
            try:
                audio_converter(input_path, output_path)
                print(f"✅ Converted: {filename}")
            except Exception as e:
                print(f"❌ Error converting {filename}: {e}")

# Example usage
batch_convert_audio("samples/audio/", "output/audio/", "mp3")
```

### Custom Quality Settings

```python
from PIL import Image
from src.image_converter import image_converter

# High-quality image conversion
def high_quality_image_convert(input_path, output_path):
    with Image.open(input_path) as img:
        img.save(output_path, quality=95, optimize=True)
```

## 🛠️ Dependencies

### Core Libraries
- **pydub**: Audio processing and conversion
- **ffmpeg-python**: Video processing and conversion  
- **Pillow (PIL)**: Image processing and conversion
- **python-docx**: Document creation and manipulation
- **PyPDF2**: PDF processing
- **unoconv**: Universal document converter

### System Requirements
- **Python 3.7+**
- **FFmpeg** (for video processing)
- **LibreOffice** (for document conversion)

## 🚦 Getting Started with Development

1. **Fork and clone the repository**
2. **Set up development environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. **Run tests:**
   ```bash
   python -m pytest tests/
   ```
4. **Make your changes and submit a pull request**

## 📊 Performance

- **Audio Conversion**: ~2-5x faster than real-time playback
- **Video Conversion**: Depends on codec and quality settings
- **Image Conversion**: Near-instantaneous for most formats
- **Document Conversion**: 1-10 seconds depending on document complexity

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📋 Roadmap

- [ ] **GUI Interface**: Desktop application with drag-and-drop support
- [ ] **Web Interface**: Browser-based converter
- [ ] **Cloud Storage Integration**: Direct conversion from/to cloud services
- [ ] **Advanced Video Options**: Quality presets, codec selection
- [ ] **Batch Processing UI**: Progress bars and cancellation support
- [ ] **Format Preview**: Preview converted files before saving
- [ ] **Conversion History**: Track and repeat previous conversions

## ❓ FAQ

**Q: Why do I need LibreOffice for document conversion?**
A: LibreOffice provides the most reliable document conversion engine, supporting dozens of formats with high fidelity.

**Q: Can I convert multiple files at once?**
A: Yes! Use the batch processing functions or implement your own loops using the converter modules.

**Q: What's the maximum file size supported?**
A: Limited by available system memory. Most files under 1GB should convert without issues.

**Q: Are there any quality losses during conversion?**
A: Minimal quality loss for lossless formats. Lossy formats (like MP3, JPEG) may have slight quality reduction.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Author

**AbdelRahman** - *Initial work* - [@Hashad-ar](https://github.com/Hashad-ar)

## 🙏 Acknowledgments

- **FFmpeg** community for excellent multimedia framework
- **LibreOffice** team for powerful document processing
- **Python** ecosystem for amazing libraries
- **Contributors** who help improve this project

## 📞 Support

- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/Hashad-ar/UniversalFileConverter/issues)
- 💡 **Feature Requests**: [GitHub Discussions](https://github.com/Hashad-ar/UniversalFileConverter/discussions)
- 📧 **Contact**: [Your Email]

---

⭐ **Star this repository if you find it useful!** ⭐

[![GitHub stars](https://img.shields.io/github/stars/Hashad-ar/UniversalFileConverter.svg?style=social&label=Star)](https://github.com/Hashad-ar/UniversalFileConverter)
[![GitHub forks](https://img.shields.io/github/forks/Hashad-ar/UniversalFileConverter.svg?style=social&label=Fork)](https://github.com/Hashad-ar/UniversalFileConverter/fork)
