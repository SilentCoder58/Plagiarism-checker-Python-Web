import os
from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Function to vectorize the text content
def vectorize(texts):
    return TfidfVectorizer().fit_transform(texts).toarray()

# Function to calculate cosine similarity between two vectors
def calculate_similarity(doc1, doc2):
    return cosine_similarity([doc1, doc2])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check_plagiarism', methods=['POST'])
def check_plagiarism():
    # Get the text from the form
    sample1_text = request.form['sample1']
    sample2_text = request.form['sample2']

    if not sample1_text or not sample2_text:
        return jsonify({"error": "Both samples must be provided."}), 400

    # Vectorize the samples
    vectors = vectorize([sample1_text, sample2_text])
    similarity_score = calculate_similarity(vectors[0], vectors[1])[0][1]
    similarity_percentage = round(similarity_score * 100, 2)

    return jsonify({"similarity_percentage": f"{similarity_percentage}%"})

if __name__ == '__main__':
    app.run(debug=True)
