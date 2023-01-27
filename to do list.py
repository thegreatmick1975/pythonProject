todo_list = []

def view_list():
    for i, task in enumerate(todo_list):
        print(f'{i+1} - {task}')

def add_item(task):
    todo_list.append(task)
    print(f'Task "{task}" added to list')

def remove_item(index):
    task = todo_list.pop(index)
    print(f'Task "{task}" removed from list')

while True:
    user_input = input('Enter a command (view, add, remove, exit): ')
    if user_input == 'view':
        view_list()
    elif user_input == 'add':
        task = input('Enter the task: ')
        add_item(task)
    elif user_input == 'remove':
        index = int(input('Enter the task number: ')) - 1
        remove_item(index)
    elif user_input == 'exit':
        break
    else:
        print('Invalid command')
