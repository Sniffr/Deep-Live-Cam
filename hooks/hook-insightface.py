from PyInstaller.utils.hooks import collect_data_files, collect_submodules

# Collect all submodules
hiddenimports = collect_submodules('insightface')

# Collect data files
datas = collect_data_files('insightface')
