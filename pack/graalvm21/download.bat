@echo off
chcp 65001 >nul
SET URL=https://download.oracle.com/graalvm/21/latest/graalvm-jdk-21_windows-x64_bin.zip
SET FILENAME=graalvm-jdk-21_windows-x64_bin.zip
SET FOLDER=graalvm-unzipped

echo 正在下载GraalVM JDK...
curl -L %URL% -o %FILENAME%

echo 正在解压文件...
PowerShell -Command "$ProgressPreference = 'SilentlyContinue'; Expand-Archive -LiteralPath '%FILENAME%' -DestinationPath '%FOLDER%' -Force"

echo 正在移动文件...
PowerShell -Command "Get-ChildItem -Path '.\%FOLDER%\*' -Recurse | Move-Item -Destination '.' -Force"

echo 正在清理临时文件...
del %FILENAME%
if exist %FOLDER% rmdir /S /Q %FOLDER%

echo 安装完成!
pause