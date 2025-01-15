import os
import sys

def setup_environment():
    """Set up runtime environment for the application."""
    if getattr(sys, 'frozen', False):
        # Running in PyInstaller bundle
        base_dir = sys._MEIPASS
        
        # Add FFmpeg to PATH
        ffmpeg_path = os.path.join(base_dir, 'ffmpeg', 'bin')
        if os.path.exists(ffmpeg_path):
            os.environ['PATH'] = ffmpeg_path + os.pathsep + os.environ.get('PATH', '')
        
        # Ensure models directory exists
        models_dir = os.path.join(base_dir, 'models')
        os.makedirs(models_dir, exist_ok=True)

setup_environment()
