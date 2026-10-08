# Launch Script for PowerShell
Write-Host "===============================================================" -ForegroundColor Cyan
Write-Host "Starting SalaryScope India - Tech Market Intelligence Web App" -ForegroundColor Green
Write-Host "===============================================================" -ForegroundColor Cyan

$pythonCmd = (Get-Command python -ErrorAction SilentlyContinue)
if ($pythonCmd) {
    python -m streamlit run app.py
} else {
    $localPy = "$env:LOCALAPPDATA\Python\bin\python.exe"
    if (Test-Path $localPy) {
        & $localPy -m streamlit run app.py
    } else {
        Write-Error "Python executable not found. Please ensure Python is in your PATH."
    }
}
