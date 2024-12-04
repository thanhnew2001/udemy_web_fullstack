
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

tasks = [{"id": 1, "name": "Cleaning"}, {"id": 2, "name": "Shopping"}]

# Route to get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    new_task = {"id": len(tasks)+1 , "name": data["name"]}
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    global tasks
    tasks = [t for t in tasks if t['id']!=id]
    return jsonify({"message": f"Task {id} deleted"})

app.run()
