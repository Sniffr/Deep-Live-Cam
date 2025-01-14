import os
import sys
import platform
import PyInstaller.__main__

# Get the absolute path of the project root directory
project_root = os.path.dirname(os.path.abspath(__file__))

# Define data files to include
datas = [
    ('modules', 'modules'),  # Include all Python modules
    ('models', 'models'),    # Include model files
]

# Define all hidden imports
hidden_imports = [
    'torch', 'torch.nn', 'torch.optim', 'torch.cuda',
    'onnxruntime', 'tensorflow', 'insightface',
    'customtkinter', 'tkinterdnd2', 'cv2_enumerate_cameras',
    'gfpgan', 'numpy', 'opencv-python', 'pillow',
    'psutil', 'tqdm', 'opennsfw2', 'protobuf'
]

# Platform-specific imports
if platform.system().lower() == 'windows':
    hidden_imports.extend(['torch.cuda', 'onnxruntime-gpu'])
else:
    hidden_imports.extend(['onnxruntime-cpu'])

# PyInstaller configuration
PyInstaller.__main__.run([
    'run.py',
    '--name', 'DeepLiveCam',
    '--onefile',
    '--windowed',  # For GUI applications
    '--clean',
    '--noconfirm',
    '--additional-hooks-dir', 'hooks',
    # Add all hidden imports
    *[f'--hidden-import={imp}' for imp in hidden_imports],
    # Add data files
    *[f'--add-data={src}{os.pathsep}{dst}' for src, dst in datas],
    # Add binary dependencies
    '--add-binary', f'models{os.pathsep}models',
    '--add-binary', f'ffmpeg/bin/*{os.pathsep}ffmpeg/bin',
    # Exclude unnecessary packages to reduce size
    '--exclude-module', 'matplotlib',
    '--exclude-module', 'PyQt5',
    '--exclude-module', 'PySide2',
    '--exclude-module', 'IPython'
])
