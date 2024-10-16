from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {
        "done": true,
        "label": "Sample Todo 1"
    },
    {
        "done": true,
        "label": "Sample Todo 2"
    }
];

@app.route("/todos", methods=["GET"])
def get_todos():
    json_text = jsonify(todos), 200
    return json_text

@app.route("/todos", methods=["POST"])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    return jsonify([todos[len(todos) - 1], todos]), 201

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    todos.pop(position)
    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)