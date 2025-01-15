import os
import urllib.request
import zipfile
from tqdm import tqdm

FFMPEG_URL = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip"

def download_ffmpeg():
    if not os.path.exists("ffmpeg/bin"):
        os.makedirs("ffmpeg/bin", exist_ok=True)
        
    zip_path = "ffmpeg-master-latest-win64-gpl.zip"
    print("Downloading FFmpeg...")
    
    request = urllib.request.urlopen(FFMPEG_URL)
    total = int(request.headers.get("Content-Length", 0))
    
    with tqdm(total=total, unit='B', unit_scale=True) as progress:
        urllib.request.urlretrieve(
            FFMPEG_URL,
            zip_path,
            lambda count, block_size, total_size: progress.update(block_size)
        )
    
    print("Extracting FFmpeg...")
    with zipfile.ZipFile(zip_path) as zf:
        for member in zf.namelist():
            if member.endswith(('.exe', '.dll')) and '/bin/' in member:
                filename = os.path.basename(member)
                with zf.open(member) as source, \
                     open(f"ffmpeg/bin/{filename}", "wb") as target:
                    target.write(source.read())
    
    os.remove(zip_path)
    print("FFmpeg setup complete!")

if __name__ == "__main__":
    download_ffmpeg()
