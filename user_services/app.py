from flask import Flask, jsonify

app = Flask(__name__)

# Let's simulate a database that stores users credentials

users = {
    "user1": {
        "name": "John Doe",
        "email": "john@doe.com"
    },
    "user2": {
        "name": "Jane Doe",
        "email": "jane@doe.com"
    }
}

# This route returns the user information as a JSON file so that it can be used by other endpoints.
@app.route("/user/<username>", methods=["GET"])
def get_user(username):
    if username in users:
        return jsonify(users[username]), 200
    else:
        return jsonify({"message": "User not found"}), 404


if __name__ == "__main__":
    app.run(port=5001)