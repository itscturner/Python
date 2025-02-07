
import json

def load_todos():
    try:
        with open('todos.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_todos(todos):
    with open('todos.json' 'w') as f:
        json.dump(todos, f)

def add_todo(todos):
    task = input("Enter A New Task: ")
    todos.append({"task": task, "completed": False})
    save_todos(todos)
    print("Task Added.")

def mark_complete(todos):
    print("Your Tasks:")
    for index, todo in enumerate(todos):
        print(f"{index + 1}. {todo['task']} (Completed: {todo['completed']})")

    choice = int(input("Enter Task Number To Mark Complete: ")) - 1
    if 0 <= choice < len(todos):
        todos[choice]["completed"] = True
        save_todos(todos)
        print("Task Marked Complete.")
    else:
        print("Invalid Task Number.")

def main():
    todos = load_todos()
    
    while True:
        print("\nChoose An Action:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Complete")
        print("4. Exit")
        
        choice = input("Enter Your Choice: ")
        
        if choice == '1':
            view_todos(todos)
        elif choice == '2':
            add_todo(todos)
        elif choice == '3':
            mark_complete(todos)
        elif choice == '4':
            break
        else:
            print("Invalid Choice.")

main()
