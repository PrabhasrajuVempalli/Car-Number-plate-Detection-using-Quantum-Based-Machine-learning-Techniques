@echo off
echo =======================================
echo   Starting Indian ANPR System
echo =======================================

echo.
echo [1/3] Starting Backend Server...
start "ANPR Backend" cmd /k ".venv\Scripts\activate && python -m backend.main"

echo Waiting 20 seconds for AI Models to load...
timeout /t 20 /nobreak > nul

echo.
echo [2/3] Starting Frontend Server...
start "ANPR Frontend" cmd /k ".venv\Scripts\activate && python -m http.server 3000 --directory frontend"

echo.
echo [3/3] Opening Dashboard in browser...
timeout /t 2 > nul
start http://localhost:3000

echo.
echo Done! Both servers are running in separate windows.
echo You can close this window now.
pause
