#!/bin/bash
set -e

echo "Starting Deep Live Cam build process..."

# Ensure we're in the project root
cd "$(dirname "$0")"

# Download dependencies
if [ ! -f "7zSD.sfx" ]; then
    echo "Downloading 7zSD.sfx..."
    curl -L -o 7zSD.sfx "https://raw.githubusercontent.com/mcmilk/7-Zip-zstd/master/C/Util/7z/7zSD.sfx"
fi

# Download FFmpeg
echo "Setting up FFmpeg..."
python scripts/download_ffmpeg.py

# Build with PyInstaller
echo "Building with PyInstaller..."
python build_windows.py

# Create temporary directory for distribution
echo "Preparing distribution..."
mkdir -p dist_temp
cp -r dist/DeepLiveCam/* dist_temp/
cp -r models dist_temp/

# Create 7z archive
echo "Creating 7z archive..."
7z a -r DeepLiveCam.7z ./dist_temp/*

# Create self-extracting archive
echo "Creating self-extracting archive..."
cat 7zSD.sfx config.txt DeepLiveCam.7z > DeepLiveCamSetup.exe

# Cleanup
echo "Cleaning up..."
rm -rf dist_temp DeepLiveCam.7z

echo "Build complete! DeepLiveCamSetup.exe created."
