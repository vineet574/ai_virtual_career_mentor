from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profile', methods=['POST'])
def profile():
    skills = request.form['skills']
    interests = request.form['interests']
    
    # Get career recommendations based on skills and interests
    recommendations = get_career_recommendations(skills, interests)
    
    # Fetch real-time job opportunities from API
    job_opportunities = fetch_jobs_from_api()
    
    # Pass both recommendations and job opportunities to the template
    return render_template('profile.html', recommendations=recommendations, jobs=job_opportunities)

def get_career_recommendations(skills, interests):
    jobs = {
        "data science": ["Data Scientist", "Data Analyst"],
        "software development": ["Software Developer", "Frontend Developer", "Backend Developer"],
        "ai": ["Machine Learning Engineer", "AI Researcher"],
    }

    recommendations = []
    for interest in interests.split(","):
        interest = interest.strip().lower()
        if interest in jobs:
            recommendations.extend(jobs[interest])

    return recommendations

# Function to fetch job data from an API
def fetch_jobs_from_api():
    # Load API credentials from environment variables
    app_id = os.getenv("APP_ID")  # Your Application ID from .env
    app_key = os.getenv("APP_KEY")  # Your Application Key from .env

    # Example API URL (Adzuna API used here, adjust it based on the API you are using)
    url = f"https://api.adzuna.com/v1/api/jobs/us/search/1?app_id={app_id}&app_key={app_key}&results_per_page=5&what=developer&where=remote"

    response = requests.get(url)

    if response.status_code == 200:
        jobs_data = response.json()  # Extract job data from the JSON response
        # Extracting the job titles, companies, and locations
        jobs = []
        for job in jobs_data.get('results', []):
            title = job.get('title')
            company = job.get('company', {}).get('display_name', 'Unknown Company')
            location = ", ".join(job.get('location', {}).get('area', [])) or 'Unknown Location'
            jobs.append({"title": title, "company": company, "location": location})
        return jobs
    else:
        return []  # Return an empty list if the API request fails

if __name__ == "__main__":
    app.run(debug=True)

