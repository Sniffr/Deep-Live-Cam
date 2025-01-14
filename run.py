#!/usr/bin/env python3

import os
import sys
import platform

def setup_environment():
    """Set up runtime environment including PATH for ffmpeg"""
    # Get the base directory (either PyInstaller temp or script location)
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        base_dir = sys._MEIPASS
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Add ffmpeg to PATH
    ffmpeg_path = os.path.join(base_dir, 'ffmpeg', 'bin')
    if os.path.exists(ffmpeg_path):
        if platform.system().lower() == 'windows':
            os.environ['PATH'] = ffmpeg_path + os.pathsep + os.environ.get('PATH', '')
    
    # Ensure models directory exists
    models_dir = os.path.join(base_dir, 'models')
    os.makedirs(models_dir, exist_ok=True)

if __name__ == '__main__':
    setup_environment()
    from modules import core
    core.run()
