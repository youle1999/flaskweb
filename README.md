# Clone the repository
git clone 
cd flaskweb

# Set up a virtual environment
python -m venv venv
# Activate the virtual environment
source venv/bin/activate  # On MacOS/Linux
# venv\Scripts\activate  # On Windows

# Install Flask (and other dependencies if requirements.txt is present)
pip install -r requirements.txt || pip install Flask

# Run the Flask application
python app.py
