import os
import sys
import platform
import urllib.request
import zipfile
from tqdm import tqdm

FFMPEG_URL = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip"

if platform.system().lower() != 'windows':
    print("Running in development mode (non-Windows environment)")
    if not os.environ.get('ALLOW_NON_WINDOWS_BUILD'):
        print("Set ALLOW_NON_WINDOWS_BUILD=1 to proceed with development build")
        sys.exit(1)
    # Create dummy FFmpeg directory for development
    os.makedirs("ffmpeg/bin", exist_ok=True)
    print("Created dummy FFmpeg directory for development build")
    sys.exit(0)  # Exit successfully for development builds

def download_ffmpeg():
    if not os.path.exists("ffmpeg/bin"):
        os.makedirs("ffmpeg/bin", exist_ok=True)
        
        print(f"Downloading FFmpeg from {FFMPEG_URL}")
        with urllib.request.urlopen(FFMPEG_URL) as response:
            total_size = int(response.headers.get('content-length', 0))
            
            with open("ffmpeg.zip", "wb") as f, tqdm(
                total=total_size,
                unit='iB',
                unit_scale=True,
                unit_divisor=1024,
            ) as pbar:
                while True:
                    data = response.read(8192)
                    if not data:
                        break
                    size = f.write(data)
                    pbar.update(size)
        
        print("Extracting FFmpeg...")
        with zipfile.ZipFile("ffmpeg.zip", 'r') as zip_ref:
            for file in zip_ref.namelist():
                if file.endswith(('.exe', '.dll')):
                    zip_ref.extract(file, "ffmpeg_temp")
        
        # Move executables to bin directory
        for root, _, files in os.walk("ffmpeg_temp"):
            for file in files:
                if file.endswith(('.exe', '.dll')):
                    src = os.path.join(root, file)
                    dst = os.path.join("ffmpeg/bin", file)
                    os.rename(src, dst)
        
        # Cleanup
        os.remove("ffmpeg.zip")
        import shutil
        shutil.rmtree("ffmpeg_temp")
        print("FFmpeg setup complete!")

if __name__ == "__main__":
    download_ffmpeg()
