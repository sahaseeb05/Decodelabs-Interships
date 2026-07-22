from flask import Flask, render_template, request, jsonify
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Sample Dataset
ITEMS = [
    {"id": 1, "title": "Machine Learning & Neural Networks Fundamentals", "tags": "python machine-learning deep-learning neural-networks optimization tensors"},
    {"id": 2, "title": "Full-Stack Web Development Bootcamp", "tags": "html css javascript react nodejs frontend backend software-development code"},
    {"id": 3, "title": "AI & Data Engineering Pipeline", "tags": "python automation data-science cloud-computing machine-learning vector-mapping"},
    {"id": 4, "title": "Cloud Infrastructure & DevOps Mastery", "tags": "cloud automation devops aws docker kubernetes infrastructure"},
    {"id": 5, "title": "Algorithmic Trading & Quantitative Python", "tags": "python algorithms finance data-analysis statistics optimization code"}
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    user_choices = data.get("preferences", [])

    if len(user_choices) < 3:
        return jsonify({"error": "At least 3 preferences are required."}), 400

    user_profile = " ".join(user_choices)
    corpus = [item["tags"] for item in ITEMS] + [user_profile]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)

    item_vectors = tfidf_matrix[:-1]
    user_vector = tfidf_matrix[-1]

    scores = cosine_similarity(user_vector, item_vectors).flatten()
    top_indices = np.argsort(scores)[::-1][:3]

    results = []
    for idx in top_indices:
        results.append({
            "title": ITEMS[idx]["title"],
            "score": round(float(scores[idx]) * 100, 1)
        })

    return jsonify({"recommendations": results})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
