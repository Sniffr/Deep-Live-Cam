import os
import sys
from typing import List, Dict, Any

def get_base_dir() -> str:
    """Get the base directory for the application, handling both PyInstaller and regular execution."""
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        # Running in PyInstaller bundle
        return sys._MEIPASS
    else:
        # Running in normal Python environment
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = get_base_dir()
MODELS_DIR = os.path.join(BASE_DIR, "models")
WORKFLOW_DIR = os.path.join(ROOT_DIR, "workflow")

file_types = [
    ("Image", ("*.png", "*.jpg", "*.jpeg", "*.gif", "*.bmp")),
    ("Video", ("*.mp4", "*.mkv")),
]

souce_target_map = []
simple_map = {}

source_path = None
target_path = None
output_path = None
frame_processors: List[str] = []
keep_fps = True
keep_audio = True
keep_frames = False
many_faces = False
map_faces = False
color_correction = False  # New global variable for color correction toggle
nsfw_filter = False
video_encoder = None
video_quality = None
live_mirror = False
live_resizable = True
max_memory = None
execution_providers: List[str] = []
execution_threads = None
headless = None
log_level = "error"
fp_ui: Dict[str, bool] = {"face_enhancer": False}
camera_input_combobox = None
webcam_preview_running = False
show_fps = False
mouth_mask = False
show_mouth_mask_box = False
mask_feather_ratio = 8
mask_down_size = 0.50
mask_size = 1
