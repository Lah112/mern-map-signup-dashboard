from flask import Flask, request, jsonify
from pymongo import MongoClient
from sklearn.cluster import KMeans
import numpy as np

app = Flask(__name__)
client = MongoClient("mongodb+srv://it22076816:RfT8jg5IwXoXj9xC@ml.u9xhg.mongodb.net/?retryWrites=true&w=majority&appName=ML")
db = client["fullstack_ml"]
users = db["users"]

@app.route("/cluster", methods=["GET"])
def cluster_users():
    data = list(users.find({}, {"_id": 0, "location": 1}))
    locations = np.array([[d["location"]["lat"], d["location"]["lng"]] for d in data if "location" in d])

    kmeans = KMeans(n_clusters=3)
    clusters = kmeans.fit_predict(locations)

    return jsonify({"clusters": clusters.tolist()})

if __name__ == "__main__":
    app.run(debug=True)
