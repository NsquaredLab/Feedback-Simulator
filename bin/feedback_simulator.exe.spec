# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['..\\test\\main.py'],
    pathex=[],
    binaries=[],
    datas=[('c:\\Users\\Domi\\Documents\\Projects\\feedback_simulator\\.venv\\Lib\\site-packages\\vispy\\glsl', 'vispy\\glsl'), ('c:\\Users\\Domi\\Documents\\Projects\\feedback_simulator\\.venv\\Lib\\site-packages\\vispy\\io\\_data', 'vispy\\io\\_data'), ('c:\\Users\\Domi\\Documents\\Projects\\feedback_simulator\\.venv\\Lib\\site-packages\\distributed', 'distributed')],
    hiddenimports=['vispy.ext._bundled.six', 'vispy.app.backends._pyside6'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='feedback_simulator.exe',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
