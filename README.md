# Google Cloud Tech Day 2025 Website

A 1-day technical conference informational site built with Flask.

## Features
- **Event Schedule**: View the full day's agenda, including 8 talks and a lunch break.
- **Search**: Filter talks by Title, Speaker Name, or Category.
- **Responsive Design**: Optimized for desktop and mobile viewing.
- **Speaker Info**: Links to speakers' LinkedIn profiles.

## Tech Stack
- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)

## Setup & Run

1.  **Prerequisites**: Ensure you have Python installed.
2.  **Install Dependencies**:
    ```bash
    pip install flask
    ```
3.  **Run the Application**:
    ```bash
    python app.py
    ```
4.  **Access the Site**: Open your browser and navigate to `http://127.0.0.1:5000`.

## Project Structure
- `app.py`: Main Flask application file.
- `data.py`: Contains dummy data for events and speakers.
- `templates/index.html`: Main HTML template.
- `static/style.css`: CSS styles.
- `static/script.js`: JavaScript for search functionality.
