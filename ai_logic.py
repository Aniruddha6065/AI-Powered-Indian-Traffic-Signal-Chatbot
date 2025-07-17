import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load FAQ data
with open(os.path.join(os.path.dirname(__file__), 'faq_data.json'), 'r', encoding='utf-8') as f:
    faq_data = json.load(f)

questions = [item['Question'] for item in faq_data]
answers = [item['Answer'] for item in faq_data]

vectorizer = TfidfVectorizer().fit(questions)
question_vectors = vectorizer.transform(questions)

SIMILARITY_THRESHOLD = 0.3  # 30%

def get_bot_response(user_input):
    user_vec = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_vec, question_vectors).flatten()
    max_idx = similarities.argmax()
    if similarities[max_idx] >= SIMILARITY_THRESHOLD:
        return answers[max_idx]
    else:
        return "Sorry, I couldn't understand your question. Please try rephrasing." 