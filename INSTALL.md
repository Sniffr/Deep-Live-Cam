# Installation Instructions

## Prerequisites
1. Python 3.10 or later
2. NVIDIA GPU with CUDA support (recommended)
3. Windows 10/11 64-bit

## Quick Start
1. Download and extract DeepLiveCam-v1.0.0-beta.zip
2. Run `install.bat` to set up dependencies
3. Launch the application with `python run.py`

## Manual Installation
If the automatic installation fails:

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Download required models:
```bash
python scripts/download_models.py
```

3. Set up FFmpeg:
```bash
python scripts/download_ffmpeg.py
```

4. Run the application:
```bash
python run.py
```

## Troubleshooting
- If you encounter CUDA errors, the application will fall back to CPU mode
- Make sure you have Visual C++ Redistributable installed
- Check the models/ directory contains required model files
