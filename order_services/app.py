from flask import Flask, jsonify
import requests

app = Flask(__name__)
USER_SERVICES_URL = "http://localhost:5001/user/"

@app.route("/order/<username>", methods=["GET"])
def create_new_order(username):
    # Get the user's info from the User microservice
    user_response = requests.get(USER_SERVICES_URL + username)

    if user_response.status_code == 200:
        user_data = user_response.json()
        order = {
            "username": username,
            "product_name": "The Art of War",
            "user_details": user_data
        }
        return jsonify(order), 200
    else:
        return jsonify({"message": "User can't be found"}), 400


if __name__ == "__main__":
    app.run(port=5002)