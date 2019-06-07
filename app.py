from flask import Flask, jsonify, request, abort


app = Flask(__name__)

tasks = []

@app.route('/list', methods=['GET'])
def list_tasks():
    return jsonify({'tasks':tasks})

@app.route('/add', methods=['POST'])
def add_task():
    if not request.json or not 'title' in request.json or not 'description' in request.json:
        abort(400)
    temp = 1
    if (len(tasks) > 0):
        temp = tasks[-1]['id'] + 1
    task = {
        'id':temp,
        'title': request.json['title'],
        'description': request.json['description']
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/supp/<int:id>', methods=['DELETE'])
def supp_task(id):
    task = [task for task in tasks if task['id'] ==id]
    if len(task) == 0:
        abort(400)
    tasks.remove(task[0])
    return jsonify({'result':True})

if __name__ == '__main__':
    app.run(debug=True)
