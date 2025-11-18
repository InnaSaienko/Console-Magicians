@echo off
REM Setup script for development environment (Windows)

echo.
echo Setting up development environment...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install Python first.
    pause
    exit /b 1
)

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo Failed to create virtual environment.
        pause
        exit /b 1
    )
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip --quiet

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt --quiet

if errorlevel 1 (
    echo Failed to install dependencies.
    pause
    exit /b 1
)

REM Install pre-commit hooks
echo.
echo Installing pre-commit hooks...
pre-commit install

if errorlevel 1 (
    echo Failed to install pre-commit hooks.
    pause
    exit /b 1
)

REM Run pre-commit on all files
echo.
echo Testing pre-commit hooks on all files...
pre-commit run --all-files

echo.
echo Setup complete!
echo.
echo To activate the virtual environment, run:
echo   venv\Scripts\activate.bat
echo.
pause
