print("---- Welcome to Todo List ----")

tasks = []

while True:
    try:
        user = int(input(
            "\nChoose an option:\n"
            "1. Add task\n"
            "2. Edit task\n"
            "3. View tasks\n"
            "4. Delete task\n"
            "5. Exit\n"
            "Enter your choice: "
        ))
    except ValueError:
        print("Please enter a valid number!")
        continue

    # 1️⃣ Add Task
    if user == 1:
        task_name = input("Enter task name: ")
        date = input("Enter date: ")

        task = {
            "task": task_name,
            "date": date
        }
        tasks.append(task)
        print("✅ Task added successfully!")

    # 2️⃣ Edit Task
    elif user == 2:
        edit_task = input("Enter the task name to edit: ")
        found = False

        for item in tasks:
            if item["task"] == edit_task:
                item["task"] = input("Enter new task name: ")
                change_date = input("Do you want to change date? (y/n): ").lower()
                if change_date == 'y':
                    item["date"] = input("Enter new date: ")
                print("✅ Task updated successfully!")
                found = True
                break

        if not found:
            print("❌ Task not found.")

    # 3️⃣ View Tasks
    elif user == 3:
        if not tasks:
            print("❌ No tasks available.")
        else:
            print("\n📋 Your Tasks:")
            for i, item in enumerate(tasks, start=1):
                print(f"{i}. {item['task']} - {item['date']}")

    # 4️⃣ Delete Task
    elif user == 4:
        delete_task = input("Enter task name to delete: ")
        found = False

        for item in tasks:
            if item["task"] == delete_task:
                tasks.remove(item)
                print("✅ Task deleted successfully!")
                found = True
                break

        if not found:
            print("❌ Task not found.")

    # 5️⃣ Exit
    elif user == 5:
        print("👋 Thanks for using Todo List!")
        break

    # ❌ Invalid Choice
    else:
        print("❌ Invalid option. Please choose between 1–5.")
