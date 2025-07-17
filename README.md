# AI-Powered Indian Traffic Signal Chatbot

## Overview
This project is an AI-powered chatbot designed to help users access information about Indian traffic rules, fines, and road safety. It uses Natural Language Processing (NLP) to match user queries with a curated FAQ dataset, providing quick and accurate answers about traffic signals, lane rules, helmet laws, updated fines, and road signage norms.

## Features
- Answers user questions about Indian traffic rules and fines
- Uses TF-IDF + Cosine Similarity for keyword-based matching
- Can be upgraded to use Sentence Transformers (MiniLM) for semantic understanding
- Easy-to-use web interface built with Flask
- Expandable FAQ dataset for continuous improvement

## Setup
1. **Clone the repository:**
   ```sh
   git clone https://github.com/Aniruddha6065/AI-Powered-Indian-Traffic-Signal-Chatbot.git
   cd AI-Powered-Indian-Traffic-Signal-Chatbot
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the application:**
   ```sh
   python app.py
   ```
4. **Access the chatbot:**
   Open your browser and go to `http://localhost:5000`

## Deployment
- The app can be deployed on any server supporting Python and Flask (e.g., Heroku, PythonAnywhere, AWS EC2, or a local server).
- For production, use a WSGI server like Gunicorn and set up environment variables as needed.

## Usage
- Enter your traffic rule question in the chat interface.
- The bot will respond with the most relevant answer from the FAQ dataset.

**Example:**
- User: "Is helmet required for pillion passenger?"
- Bot: "Yes, helmets are mandatory for both riders and pillions."

## Results
- High accuracy for direct and rephrased queries
- Fast response time
- Improved accessibility to traffic rule information

## Future Scope
- **API Integration:** Connect with government APIs for real-time updates on traffic rules and fines.
- **AI Assistant:** Add voice-enabled AI assistant for hands-free interaction.
- **Image Support:** Allow users to upload images (e.g., road signs) for identification and explanation using image recognition.

**Example:**
A user uploads a photo of a road sign, and the chatbot identifies and explains its meaning.

## References
- [Project GitHub Repository](https://github.com/Aniruddha6065/AI-Powered-Indian-Traffic-Signal-Chatbot)
- [Indian Government Traffic Rules PDF](https://morth.nic.in/sites/default/files/notifications_document/CMVR1989.pdf)
- [Traffic Signs and Symbols in India (PDF)](https://morth.nic.in/sites/default/files/notifications_document/TrafficSigns.pdf)
- [Parivahan Sewa – Government of India](https://parivahan.gov.in/)

---

Feel free to contribute or raise issues to help improve the project! 