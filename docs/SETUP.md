# Development Environment Setup

## Prerequisites

- Python 3.12 or higher
- Node.js 18 or higher (for future frontend)
- Docker and Docker Compose
- Git
- Visual Studio Code

## Initial Setup

### 1. Clone the repository

```bash
git clone https://github.com/Canepro/rocketchat-log-analyzer.git
cd rocketchat-log-analyzer
```

### 2. Install VSCode Extensions

Open the project in Visual Studio Code and install recommended extensions:

1. Click on the Extensions icon in the Activity Bar
2. Look for "Recommended" section
3. Install all recommended extensions

Alternatively, you can use the VSCode command palette (Ctrl+Shift+P):

```
Extensions: Show Recommended Extensions
```

### 3. Backend Setup

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the project root:

```env
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=your-secret-key-here
UPLOAD_FOLDER=temp_uploads
MAX_UPLOAD_SIZE=100
MAX_EXTRACTED_SIZE=500
```

### 5. Run the Application

#### Using VS Code Launch Configurations

1. Press F5 or select "Run and Debug" from the Activity Bar
2. Choose "Python: Flask" from the dropdown

#### Manual Start

```bash
# From project root, with virtual environment activated
python app.py
```

## Docker Development

To run the application in Docker:

```bash
docker build -t rocketchat-analyzer .
docker run -p 5000:5000 rocketchat-analyzer
```

## Common Issues

### Port Conflicts

If you encounter port conflicts, you can change the port in the `.env` file:

```env
PORT=5001
```

### Python Virtual Environment Issues

If you encounter issues with the virtual environment:

```bash
# Remove existing virtual environment
rm -rf venv

# Create new virtual environment
python -m venv venv

# Activate and install dependencies
venv\Scripts\activate
pip install -r requirements.txt
```

## Development Tools

### Running Tests

```bash
pytest tests/ -v
```

### Code Formatting

```bash
black .
```

### Linting

```bash
flake8 .
```

### Cleaning Temporary Files

```bash
# Windows PowerShell
.\scripts\clean.ps1

# Linux/macOS
./scripts/clean.sh
```
