from storage import save_tasks
from datetime import datetime

def add_task(todo_list):
    title=input("Enter a Task Title: ")
    if not title.strip():
        print("Title cannot be empty")
        return
    description=input("Enter description (optional): ")
    due_date=input("Enter due date(format: YYYY-MM-DD(Optional)): ")
    if due_date:
        try:
            datetime.strptime(due_date,"%Y-%m-%d")
        except ValueError:
            print("Invalid date format.")
            due_date=None
    else:
        due_date=None #Ensure empty input results in None
    #to generate unique ID incrementing the maximum exiting ID
    task_id=max([task["id"] for task in todo_list],default=0) if todo_list else 0
    task={
        "id": task_id+1,
        "Title": title,
        "Description": description,
        "Status": "Pending",
        "due_date": due_date
    }
    todo_list.append(task)
    save_tasks(todo_list)
    print("New task added successfully\n")


def view_task(todo_list,sort_by_due_date=False):
    # To display all tasks with ID,title,description,status and due date
    print("Your To-do List: ")
    if len(todo_list)==0:
        print("Task list is empty")
    else:
        tasks=todo_list
        if sort_by_due_date:
            # To sort tasks by due date,placing tasks with no due date at the end
            tasks=sorted(todo_list,key=lambda x:(x["due_date"] is None,x
                                                 ["due_date"] or ""))
        for task in tasks:
            desc=f" | {task['Description']}" if task['Description'] else ""
            due=f" | Due: {task.get('due_date','None')}"
            print(f"ID: {task['id']}: {task['Title']}{desc} - {task['Status']}{due}")
    print("\n")


def remove_task(todo_list):
    if not todo_list:
        print("List is empty")
        return
    
    try:
        task_id=int(input("Enter the task ID to remove: "))
        for i,task in enumerate(todo_list):
            if task["id"]==task_id:
                removed_task=todo_list.pop(i)
                save_tasks(todo_list)
                print(f"Task removed: {removed_task['Title']}")
                return
        print("Invalid Task ID")
    except ValueError:
        print("Please enter a valid task ID")


def completed(todo_list):
    if not todo_list:
        print("List is empty")
        return
    try:
        task_id=int(input("Enter the task ID that you wish to mark complete: ")) 
        for i,task in enumerate(todo_list):
            if task["id"]==task_id:
                task["Status"]="Completed"
                save_tasks(todo_list)
                print(f"Task {task['Title']} has been marked completed")
                return
        print("Invalid Task ID")
    except ValueError:
        print("Please enter a valid task ID")




        