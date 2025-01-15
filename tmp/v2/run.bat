@echo off
if "%1"=="" (
    echo Usage: %0 {install|remove}
    exit /b 1
)

if "%1"=="install" (
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r req.txt
    echo Virtual environment created. Please run ".\venv\Scripts\activate" to activate it.
) else if "%1"=="remove" (
    rmdir /s /q venv
    echo Virtual environment removed.
) else (
    echo Opsi tidak valid. Gunakan install atau remove.
    exit /b 1
)
