@echo off
SETLOCAL EnableDelayedExpansion

SET "SCRIPT_NAME=%~nx0"

REM 清理根目录中除了当前脚本以外的所有文件和文件夹
for %%i in (*) do (
    if /I "%%i" neq "!SCRIPT_NAME!" (
        del "%%i"
    )
)

for /D %%i in (*) do (
    if /I "%%i" neq "!SCRIPT_NAME!" (
        rmdir /S /Q "%%i"
    )
)

REM 下载并解压缩文件
SET URL=https://proxy.qianfuv.fun/proxy/https://github.com/WaxingMoonStudio/Miracles-Journey-I18n/archive/refs/heads/main.zip
SET FILENAME=Miracles-Journey-i18n.zip
SET FOLDER=Miracles-Journey-i18n-unzipped

curl -L %URL% -o %FILENAME%

PowerShell -Command "Expand-Archive -LiteralPath '%FILENAME%' -DestinationPath '%FOLDER%'"

PowerShell -Command "Get-ChildItem -Path '.\%FOLDER%\*' -Recurse | Move-Item -Destination '.'"

del %FILENAME%
if exist %FOLDER% rmdir /S /Q %FOLDER%

pause
ENDLOCAL