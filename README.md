# my-flask-app/my-flask-app/README.md

# Lip-Sync Studio

Lip-Sync Studio is a modern, responsive web application that allows users to upload an image and an audio file to generate a lip-synced video. The application is built using Flask for the backend and a dark-themed, AI-tech inspired frontend.

## Project Structure

```
my-flask-app
├── app
│   ├── __init__.py        # Initializes the Flask application
│   ├── routes.py          # Defines application routes
│   ├── static             # Contains static files (CSS, JS, images)
│   │   ├── css            # CSS files
│   │   ├── js             # JavaScript files
│   │   └── images         # Image files
│   └── templates          # HTML templates
│       ├── base.html      # Base template
│       └── index.html     # Main index page template
├── venv                    # Virtual environment
├── .gitignore              # Git ignore file
├── config.py              # Configuration settings
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd my-flask-app
   ```

3. Create a virtual environment:
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the application, use the following command:
```
flask run
```

The application will be accessible at `http://127.0.0.1:5000`.

## License

This project is licensed under the MIT License.