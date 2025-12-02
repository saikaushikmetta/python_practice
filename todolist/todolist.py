print("----welcome to todolist----")
task=[]
while True:
    user=int(input("enter the number to perform\n1.Add task\n2.Edit task\n3View task\n4Delete task\n5.Exit\nenter number to performt that task"))
    if user == 1:
        Task=input("Enter task")
        Date=input("Enter date")
        dict={
            "task":Task,
            "date":Date
        }
        task.append(dict)
        print("task is succesfully entered")
    elif user==2:
        edit=input("enter the task to edit: ")
        for item in task:
            if item["task"]==edit:
                item["task"]=input('enter new task')
                print("task changed successfully")
            else:
                print("you cannot edit")
        ask=input("do you want to also change date type y/n").lower()
        if ask=='y':
            new_date=input("enter the date to edit")
            item["date"]=new_date
            print("date has successfully updated")
        else:
            break
    elif user==3:
        for i in task:
            if i in task:
                print("Here are your task\n",i)
            else:
                print("there are no tasks added!")
    elif user==4:
        del1=input("enter task name that you want to remove")
        for item1 in task:
            if item1["task"]==del1:
                task.remove(item)
                print('your task has been succesfully deleted')
            else:
                print('task not found')
    elif user==5:
        print("Thanks for using!!")
        break
    else:
        print('wrong input')
