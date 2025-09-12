import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    """
    A GUI-based To-Do List application using Tkinter.
    
    Allows users to add tasks, mark tasks as completed, and remove tasks via a simple graphical interface.
    """

    def __init__(self, root):
        """
        Initialize the main window and widgets for the To-Do List app.
        
        Parameters:
        root (tk.Tk): The root window object of Tkinter.
        """
        self.root = root
        self.root.title("To-Do List")

        # Listbox widget to display tasks
        self.task_listbox = tk.Listbox(root, width=40, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Entry widget for inputting new tasks
        self.entry_task = tk.Entry(root, width=40)
        self.entry_task.pack(pady=5)

        # Button to add new task
        tk.Button(root, text="Add Task", command=self.add_task).pack()

        # Button to mark selected task as completed
        tk.Button(root, text="Mark as Completed", command=self.complete_task).pack()

        # Button to remove selected task
        tk.Button(root, text="Remove Task", command=self.remove_task).pack()

    def add_task(self):
        """
        Adds a new task from the input entry to the listbox.
        Shows an error popup if the entry is empty.
        """
        task = self.entry_task.get().strip()  # Get text and remove leading/trailing spaces
        if not task:
            messagebox.showwarning("Input Error", "Please enter a task!")
            return
        self.task_listbox.insert(tk.END, task)  # Insert task at the end of listbox
        self.entry_task.delete(0, tk.END)       # Clear entry after adding

    def complete_task(self):
        """
        Marks the selected task as completed by appending '[Done]'.
        Shows an error popup if no task is selected.
        """
        try:
            idx = self.task_listbox.curselection()[0]  # Get index of selected task
            task = self.task_listbox.get(idx)
            # Remove old task and insert updated completed task at the same index
            self.task_listbox.delete(idx)
            self.task_listbox.insert(idx, f"{task} [Done]")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

    def remove_task(self):
        """
        Removes the selected task from the listbox.
        Shows an error popup if no task is selected.
        """
        try:
            idx = self.task_listbox.curselection()[0]
            self.task_listbox.delete(idx)
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to remove.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

""" hey"""