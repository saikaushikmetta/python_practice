import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = task_entry.get()
    date = date_entry.get()

    if task and date:
        tasks.append({"task": task, "date": date})
        listbox.insert(tk.END, f"{task} - {date}")
        task_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter both task and date.")

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        listbox.delete(index)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def edit_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        new_task = task_entry.get()
        new_date = date_entry.get()

        if new_task and new_date:
            tasks[index]["task"] = new_task
            tasks[index]["date"] = new_date
            listbox.delete(index)
            listbox.insert(index, f"{new_task} - {new_date}")
            task_entry.delete(0, tk.END)
            date_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Task edited successfully!")
        else:
            messagebox.showwarning("Warning", "Enter new task and date.")
    else:
        messagebox.showwarning("Warning", "Select a task to edit.")

# --- UI WINDOW ---
window = tk.Tk()
window.title("Todo List")
window.geometry("350x450")

# Inputs
task_entry = tk.Entry(window, width=30)
task_entry.pack(pady=10)
task_entry.insert(0, "Enter Task")

date_entry = tk.Entry(window, width=30)
date_entry.pack(pady=5)
date_entry.insert(0, "Enter Date")

# Buttons
add_btn = tk.Button(window, text="Add Task", command=add_task)
add_btn.pack(pady=5)

edit_btn = tk.Button_
