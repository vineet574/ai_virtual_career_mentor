AI-Powered Career Mentor
Welcome to AI-Powered Career Mentor, a Flask-based web application designed to provide personalized career recommendations and real-time job opportunities based on users' skills and interests. The project integrates with job listing APIs and leverages Flask for the backend.

Features
Career Recommendations: Users input their skills and interests to receive relevant career suggestions.
Real-Time Job Listings: Fetches real-time job opportunities from external APIs (e.g., Adzuna API).
User Session Management: Users can log in and their recommendations are stored during the session.
Secure API Integration: Sensitive API keys are managed through environment variables for secure usage.
Simple User Interface: Intuitive forms and responsive display for career paths and job listings.

Technology Stack
Backend: Python 3.x, Flask
Frontend: HTML, CSS
API: Job Listings via Adzuna API (or any external job API)
Session Management: Flask-Session
Environment Management: python-dotenv for securely managing environment variables
Setup and Installation
Follow these steps to set up and run the AI-Powered Career Mentor project locally:

Prerequisites
Python 3.x installed
A job listing API key (e.g., from Adzuna)
Installation
Clone the Repository

Open your terminal and clone this repository:

bash
Copy code
git clone https://github.com/<your-username>/AI-Powered-Career-Mentor.git
Navigate to the Project Directory

bash
Copy code
cd AI-Powered-Career-Mentor
Install Dependencies

Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Set Up Environment Variables

Create a .env file in the project root directory and add your API credentials:

plaintext
Copy code
APP_ID=your_actual_app_id_here
APP_KEY=your_actual_app_key_here
Run the Application

Start the Flask server:

bash
Copy code
python app.py
Access the Application

Open your web browser and navigate to:

plaintext
Copy code
http://127.0.0.1:5000
The app will be running locally, and you can now interact with it.

API Integration
The application integrates with the Adzuna API (or another job API). To fetch real-time job opportunities, ensure you have registered for an API key and stored it in your .env file:

APP_ID: Your API application ID
APP_KEY: Your API application key
Without valid API credentials, the app won't be able to fetch job listings.

Usage
Login: Use the default credentials provided (e.g., admin/password123) to log in.
Input Skills and Interests: After logging in, enter your skills (e.g., Python, JavaScript) and your interests (e.g., AI, Web Development).
View Career Recommendations: Based on the input, career suggestions will be displayed.
Job Listings: The application will fetch and display job opportunities in real time based on the skills you input.
Project Structure
plaintext
Copy code
.
├── app.py                  # Main Flask application
├── .env                    # Environment variables (not included in repo)
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── templates/              # HTML templates
│   ├── index.html          # Home page for skills and interests input
│   ├── login.html          # User login page
│   └── profile.html        # Display career recommendations and job listings
└── static/
    └── style.css           # CSS styling for frontend
