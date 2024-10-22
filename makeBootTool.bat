@echo off

mkdir __pycache__
cd __pycache__
c:\programme\python37-32\scripts\pyinstaller --onefile --clean --add-data ..\Drivers\FX00B_Simos3Driver.bin;Drivers --add-data ..\Drivers\FX00Bx_Driver.bin;Drivers --add-data ..\Drivers\gremlindriver.bin;Drivers  --add-data ..\Drivers\SSC_93_Driver.bin;Drivers --add-data ..\Drivers\ST10XDriver.bin;Drivers  --add-data ..\Drivers\24C0xDriver.bin;Drivers --add-data ..\Minimon\LOADK.bin;Minimon --add-data ..\Minimon\MINIMONK.bin;Minimon ..\ME7BootTool.py
cd..
::attrib -r -s .\build
::attrib -r -s .\__pycache__
::attrib -r -s .\dist

move .\__pycache__\dist\*.* .\
del .\\__pycache__\dist\*.* /F /S /q
rem .\\__pycache__\dist
del .\__pycache__\build\*.* /F /S /q
rem .\__pycache__\build
del .\__pycache__\*.* /F /S /q
rem .\__pycache__
pause