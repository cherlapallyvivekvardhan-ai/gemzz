@echo off
echo ===============================================================
echo Starting SalaryScope India - Tech Market Intelligence Web App
echo ===============================================================
python -m streamlit run app.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Trying local user Python path...
    "%LOCALAPPDATA%\Python\bin\python.exe" -m streamlit run app.py
)
pause
