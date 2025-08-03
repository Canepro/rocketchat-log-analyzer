# Script to clean up temporary files and directories

# Set colors for output
$Green = "`e[32m"
$Yellow = "`e[33m"
$Reset = "`e[0m"

Write-Host "${Yellow}Cleaning project directories...${Reset}"

# Remove Python cache files
Get-ChildItem -Path . -Recurse -Name "__pycache__" -Directory | ForEach-Object { Remove-Item -Path $_ -Recurse -Force }
Get-ChildItem -Path . -Recurse -Name ".pytest_cache" -Directory | ForEach-Object { Remove-Item -Path $_ -Recurse -Force }
Get-ChildItem -Path . -Recurse -Name ".mypy_cache" -Directory | ForEach-Object { Remove-Item -Path $_ -Recurse -Force }
Get-ChildItem -Path . -Recurse -Name "*.pyc" -File | Remove-Item -Force
Get-ChildItem -Path . -Recurse -Name "*.pyo" -File | Remove-Item -Force
Get-ChildItem -Path . -Recurse -Name "*.pyd" -File | Remove-Item -Force
Get-ChildItem -Path . -Recurse -Name ".coverage" -File | Remove-Item -Force
Get-ChildItem -Path . -Recurse -Name "coverage.xml" -File | Remove-Item -Force
Get-ChildItem -Path . -Recurse -Name "htmlcov" -Directory | ForEach-Object { Remove-Item -Path $_ -Recurse -Force }

Write-Host "${Green}✓ Python cache files removed${Reset}"

# Remove temporary upload directories
if (Test-Path "temp_uploads") {
    Remove-Item -Path "temp_uploads" -Recurse -Force
    Write-Host "${Green}✓ Temporary upload directory removed${Reset}"
}

# Remove test artifacts
if (Test-Path "tests\.pytest_cache") {
    Remove-Item -Path "tests\.pytest_cache" -Recurse -Force
    Write-Host "${Green}✓ Test cache removed${Reset}"
}

# Remove Node.js build artifacts (for future frontend)
if (Test-Path "frontend") {
    if (Test-Path "frontend\node_modules\.cache") {
        Remove-Item -Path "frontend\node_modules\.cache" -Recurse -Force
    }
    if (Test-Path "frontend\.next") {
        Remove-Item -Path "frontend\.next" -Recurse -Force
    }
    if (Test-Path "frontend\out") {
        Remove-Item -Path "frontend\out" -Recurse -Force
    }
    Write-Host "${Green}✓ Frontend build cache removed${Reset}"
}

# Remove environment-specific files (but keep .env.example)
Get-ChildItem -Path . -Name ".env.local" -File | Where-Object { $_ -ne ".env.local.example" } | Remove-Item -Force

Write-Host "${Green}✓ Local environment files removed${Reset}"

# Remove log files
Get-ChildItem -Path . -Recurse -Name "*.log" -File | Remove-Item -Force

Write-Host "${Green}All temporary files cleaned!${Reset}"
