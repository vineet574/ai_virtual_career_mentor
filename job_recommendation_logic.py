import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the job dataset
def load_jobs():
    jobs_df = pd.read_csv('job_data.csv')
    return jobs_df

# Recommend jobs based on skills and interests
def get_career_recommendations(skills, interests):
    jobs_df = load_jobs()
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(jobs_df['skills'])

    # Combine skills and interests input for matching
    input_skills = skills + " " + interests
    input_vector = vectorizer.transform([input_skills])

    # Compute similarity between input and job roles
    similarity_scores = cosine_similarity(input_vector, tfidf_matrix)
    sorted_indices = similarity_scores.argsort()[0][::-1]

    recommendations = []
    for index in sorted_indices[:5]:
        recommendations.append(jobs_df['job_title'].iloc[index])

    return recommendations

