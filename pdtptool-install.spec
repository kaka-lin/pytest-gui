# -*- mode: python -*-

import os
pwd = os.getcwd()
test_files = pwd + '/testcases'

# 請將這行改成你 python packages 位置
pythonEnv_path = pwd + 'venv/lib/python3.6/site-packages'

block_cipher = None

added_files = [(test_files, 'testcases')]

a = Analysis(['pdtptool.py'],
             pathex=[pythonEnv_path, pwd],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='pdtptool',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='pdtptool')
