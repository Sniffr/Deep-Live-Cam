import os
import urllib.request
from tqdm import tqdm

MODEL_URLS = {
    "GFPGANv1.4.pth": "https://github.com/TencentARC/GFPGAN/releases/download/v1.3.4/GFPGANv1.4.pth",
    "inswapper_128_fp16.onnx": "https://huggingface.co/hacksider/deep-live-cam/resolve/main/inswapper_128_fp16.onnx"
}

def download_models():
    os.makedirs("models", exist_ok=True)
    
    for model_name, url in MODEL_URLS.items():
        model_path = os.path.join("models", model_name)
        if not os.path.exists(model_path):
            print(f"Downloading {model_name}...")
            
            request = urllib.request.urlopen(url)
            total = int(request.headers.get("Content-Length", 0))
            
            with tqdm(total=total, unit='B', unit_scale=True) as progress:
                urllib.request.urlretrieve(
                    url,
                    model_path,
                    lambda count, block_size, total_size: progress.update(block_size)
                )
    
    print("Model downloads complete!")

if __name__ == "__main__":
    download_models()
