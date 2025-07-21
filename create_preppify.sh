#!/bin/bash

# Create root project directory
mkdir -p Preppify/{routers,services,data}

# Create main app file
touch Preppify/main.py

# Create router files
touch Preppify/routers/{upload.py,preprocess.py,visualize.py}

# Create service files
touch Preppify/services/{file_manager.py,preprocessing.py,visualization.py}

# Create utility file
touch Preppify/utils.py

# Create requirements file
touch Preppify/requirements.txt

# Optional: Add a README
echo "# Preppify - FastAPI Data Preprocessing and Visualization Tool" > Preppify/README.md

# Confirm structure
echo "Preppify project structure created:"
tree Preppify
