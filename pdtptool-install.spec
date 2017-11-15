# -*- mode: python -*-

import os
pwd = os.getcwd()
test_files = pwd + '/testcases'

block_cipher = None

added_files = [(test_files, 'testcases')]

a = Analysis(['pdtptool.py'],
             pathex=['/Users/kakalin/Project/production-test-ptool/venv/lib/python3.6/site-packages', '/Users/kakalin/Project/production-test-ptool'],
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
