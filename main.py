from task_manager import add_task,remove_task,view_task,completed
from storage import load_tasks,save_tasks
todo_list=load_tasks()

def menu():
    while(True):
        print("Main Menu")
        print("1.Add new task")
        print("2.View all tasks")
        print("3.View all tasks(sorted by due date)")
        print("4.Remove a task")
        print("5.Mark task as completed")
        print("6.Exit")

        choice=input("Enter your choice: ")
        if choice=="1":
            add_task(todo_list)
        elif choice=="2":
            view_task(todo_list)
        elif choice=="3":
            view_task(todo_list,sort_by_due_date=True)
        elif choice=="4":
            remove_task(todo_list)
        elif choice=="5":
            completed(todo_list)
        elif choice=="6":
            print("Exiting")
            exit()
        else:
            print("Invalid choice")

if __name__=="__main__":
    menu()

