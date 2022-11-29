# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['widget.py', 'utils.py', 'RSA/RSA1.py', 'RSA/RSA2.py', 'RSA/RSA3.py', 'RSA/RSA4.py', 'RSA/RSA5.py', 'RSA/RSA6.py', 'RSA/RSA7.py', 'RSA/RSA8.py', 'RSA/RSA_.py', 'XOR/bruteforce.py', 'XOR/repeating_key.py'],
    pathex=[],
    binaries=[],
    datas=[('form.ui', '.')],
    hiddenimports=[],
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
    name='ZCryptUI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
