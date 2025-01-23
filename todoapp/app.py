from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# In-memory list to store ToDo items
todo_list = []

@app.route('/')
def home():
    return redirect(url_for('get_todos'))

@app.route('/todos', methods=['GET'])
def get_todos():
    return render_template('todos.html', todos=todo_list)

@app.route('/todos', methods=['POST'])
def add_todo():
    task = request.form.get('task')  # Get task from form data
    if task:
        # Add the new task to the list
        todo_list.append({'id': len(todo_list) + 1, 'task': task, 'completed': False})
    return redirect(url_for('get_todos'))

@app.route('/todos/<int:id>/complete', methods=['POST'])
def complete_todo(id):
    # Find the task by ID and toggle its completion status
    for todo in todo_list:
        if todo['id'] == id:
            todo['completed'] = not todo['completed']
            break
    return redirect(url_for('get_todos'))

@app.route('/todos/<int:id>/delete', methods=['POST'])
def delete_todo(id):
    # Remove the task from the list by ID
    global todo_list
    todo_list = [todo for todo in todo_list if todo['id'] != id]
    return redirect(url_for('get_todos'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
