@echo off

echo 
set /p FILES_PATH=directory path: 
set /p ARCHIVE_PATH=archive path: 

echo %path%

if exist %path% (
    echo directory is found
    set "SEVENZIP=C:\Program Files\7-Zip\7z.exe"
    %SEVENZIP%" a -t7z "%FILES_PATH%\backup_%ARCHIVE_PATH:~0,2%.%ARCHIVE_PATH:~3,2%.%ARCHIVE_PATH:~-4%.7z" "%FILES_PATH%" -mx5
) else (
    echo directory is not found
)


timeout /t 2


pause
