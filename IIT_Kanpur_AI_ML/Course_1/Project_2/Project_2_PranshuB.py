import hashlib 
import os 

def user_exists():
    users = {}
    if os.path.exists('users.txt'):
        with open('users.txt', 'r') as file:
           for line in file: 
                user, hashed_password = line.strip().split(':')
                users[user] = hashed_password
    return users

def register_user():     
    username = input("Enter a username: ").strip()
    users = user_exists()
    if username in users: 
        print('Username already exists. Please choose a different one.')
        return
    while True:             
        password = input("Enter a password: ")
        if password == '' or username == '': 
            print('Password or username cannot be empty.')
            continue
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        users[username] = hashed_password
        with open('users.txt', 'a') as file: 
            file.write(f'{username}:{hashed_password}\n')
        print(f'User {username} registered successfully!')
        break

def login_user(): 
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    users = user_exists()
    if username in users: 
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if users[username] == hashed_password: 
            print('Login successful!')
            return True
        else: 
            print('Incorrect password.')
    else: 
        return 'Username not found.'

def add_task(username,users):
     
    if username in users: 
        task = input("Enter a task description: ")
        task_id = str(len(username))+str(len(task))+username[:3]
        if task == '':
            print('Task description cannot be empty.')
            return
        with open(f'{username}_tasks.txt', 'a') as file:
            file.write(f'{task_id}:{task}:Pending\n')
            print(f'Task added with ID: {task_id}')
    else:
        print('User not found. Please register first.')
        return

def view_tasks(username,users): 
    
    tasks= {}
    if username in users: 
        with open(f'{username}_tasks.txt', 'r') as file:  
            for line in file: 
                task_id, task, status = line.strip().split(':')
                tasks[task_id] = {'task': task, 'status': status}
        print(f'Tasks for {username}:',tasks)
        return tasks
    else: 
        print('User not found. Please register first.')
        return {}

def select_task(username,users):
     
    if username in users: 
        task_id = input('Enter the task ID to select: ')
        tasks = view_tasks(username,users)
        if task_id in tasks: 
            status = input('Do you want to mark this task as completed? (yes/no): ')
            if status.lower() == 'yes': 
                tasks[task_id]['status'] = 'Completed'
                with open(f'{username}_tasks.txt', 'w') as file:
                    for task_id, task_info in tasks.items(): 
                        file.write(f"{task_id}:{task_info['task']}:{task_info['status']}\n") 
                print('Task marked as completed.')
                return 
            else:
                print('Task not marked as completed.') 
                return        
        else:
            print('Task not found.') 
            return 
    else:
        print('User not found. Please register first.')
        return

def delete_task(username,users): 
    if username in users: 
        task_id = input('Enter the task ID to delete: ')
        tasks = view_tasks(username,users)
        if task_id in tasks: 
            del tasks[task_id]
            with open(f'{username}_tasks.txt', 'w') as file:
                for task_id, task_info in tasks.items(): 
                    file.write(f"{task_id}:{task_info['task']}:{task_info['status']}\n") 
            print('Task deleted successfully.')
            return 
        else: 
            print('Task not found.')
            return
    else:
        print('User not found. Please register first.')
        return
    
def task_menu(username):
    users = user_exists()
    while True:
        print("\n--- Task Menu ---")
        print("1. Add a Task")
        print("2. View Tasks")
        print("3. Mark a Task as Completed")
        print("4. Delete a Task")
        print("5. Logout")

        choice = input("Enter your choice (1–5): ")

        if choice == '1':
            add_task(username,users)
        elif choice == '2':
            view_tasks(username,users)
        elif choice == '3':
            select_task(username,users)
        elif choice == '4':
            delete_task(username,users)
        elif choice == '5':
            print("Logging out..., Taking back to main menu.")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    """
    Initial menu for login/registration.
    """
    while True:
        print("\n=== Welcome to Task Manager ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option (1–3): ")

        if choice == '1':
            register_user()
        elif choice == '2':
            if login_user()== True:
                username = input('Enter your username again : ')  
                task_menu(username)
            else: 
                print('='*40)
                print('Login failed. Please try again.')
        elif choice == '3':
            print("Goodbye!")
            break
            
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()