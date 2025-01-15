@echo off
echo Installing Deep Live Cam dependencies...
python -m pip install -r requirements.txt

echo Downloading model files...
python scripts/download_models.py

echo Setting up FFmpeg...
python scripts/download_ffmpeg.py

echo Setup complete! Run the application with:
echo python run.py
pause
