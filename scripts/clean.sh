#!/bin/bash
# Script to clean up temporary files and directories

# Set colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Cleaning project directories...${NC}"

# Remove Python cache files
find . -type d -name __pycache__ -exec rm -rf {} +
find . -type d -name .pytest_cache -exec rm -rf {} +
find . -type d -name .mypy_cache -exec rm -rf {} +
find . -type f -name "*.pyc" -delete
find . -type f -name "*.pyo" -delete
find . -type f -name "*.pyd" -delete
find . -type f -name ".coverage" -delete
find . -type f -name "coverage.xml" -delete
find . -type d -name htmlcov -exec rm -rf {} +

echo -e "${GREEN}✓ Python cache files removed${NC}"

# Remove temporary upload directories
if [ -d "temp_uploads" ]; then
    rm -rf temp_uploads
    echo -e "${GREEN}✓ Temporary upload directory removed${NC}"
fi

# Remove Node.js build artifacts (for future frontend)
if [ -d "frontend" ]; then
    rm -rf frontend/node_modules/.cache
    rm -rf frontend/.next
    rm -rf frontend/out
    echo -e "${GREEN}✓ Frontend build cache removed${NC}"
fi

# Remove environment-specific files
find . -type f -name ".env.local" -not -path "./frontend/.env.local.example" -delete
echo -e "${GREEN}✓ Local environment files removed${NC}"

# Remove log files
find . -type f -name "*.log" -delete

echo -e "${GREEN}All temporary files cleaned!${NC}"
