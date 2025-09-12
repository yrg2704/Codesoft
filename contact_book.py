import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBookApp:
    """
    Contact Book Application
    -----------------------
    Manage contacts with name, phone, email, and address.
    Supports adding, viewing, searching, updating, and deleting contacts.
    Provides an intuitive GUI for user interaction.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        # Internal list to store contacts
        self.contacts = []  # Each contact is a dict: {name, phone, email, address}

        # --- User Interface ---

        # Entry fields for new contact details
        self.entry_name = tk.Entry(root, width=25)
        self.entry_phone = tk.Entry(root, width=15)
        self.entry_email = tk.Entry(root, width=25)
        self.entry_address = tk.Entry(root, width=35)

        # Arrange input fields and labels
        row = 0
        tk.Label(root, text="Name:").grid(row=row, column=0, sticky='w', padx=5)
        self.entry_name.grid(row=row, column=1, padx=5)
        row += 1
        tk.Label(root, text="Phone:").grid(row=row, column=0, sticky='w', padx=5)
        self.entry_phone.grid(row=row, column=1, padx=5)
        row += 1
        tk.Label(root, text="Email:").grid(row=row, column=0, sticky='w', padx=5)
        self.entry_email.grid(row=row, column=1, padx=5)
        row += 1
        tk.Label(root, text="Address:").grid(row=row, column=0, sticky='w', padx=5)
        self.entry_address.grid(row=row, column=1, padx=5)
        row += 1

        # Buttons for actions
        tk.Button(root, text="Add Contact", command=self.add_contact).grid(row=row, column=0, pady=8)
        tk.Button(root, text="View Contacts", command=self.view_contacts).grid(row=row, column=1, pady=8)
        row += 1
        tk.Button(root, text="Search Contact", command=self.search_contact).grid(row=row, column=0, pady=4)
        tk.Button(root, text="Clear Input", command=self.clear_inputs).grid(row=row, column=1, pady=4)

        # Listbox for contact display/selection
        row += 1
        self.listbox = tk.Listbox(root, width=70, height=8)
        self.listbox.grid(row=row, columnspan=2, pady=10)

        # Buttons for update and delete
        tk.Button(root, text="Update Selected", command=self.update_contact).grid(row=row+1, column=0, pady=3)
        tk.Button(root, text="Delete Selected", command=self.delete_contact).grid(row=row+1, column=1, pady=3)

    def clear_inputs(self):
        """Clear all input fields."""
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)

    def add_contact(self):
        """Create a new contact and add to internal list."""
        name = self.entry_name.get().strip()
        phone = self.entry_phone.get().strip()
        email = self.entry_email.get().strip()
        address = self.entry_address.get().strip()
        if not name or not phone:
            messagebox.showwarning("Input Error", "Name and Phone are required fields.")
            return
        for contact in self.contacts:
            if contact['phone'] == phone:
                messagebox.showwarning("Duplicate", "A contact with this phone number already exists.")
                return
        self.contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
        messagebox.showinfo("Success", f"Contact '{name}' added.")
        self.clear_inputs()
        self.view_contacts()

    def view_contacts(self):
        """Display all contacts in the listbox."""
        self.listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.listbox.insert(tk.END, f"{contact['name']} | {contact['phone']} | {contact['email']} | {contact['address']}")

    def search_contact(self):
        """Search for contacts by name or phone number."""
        query = simpledialog.askstring("Search", "Enter name or phone to search:")
        if not query:
            return
        results = []
        for contact in self.contacts:
            if query.lower() in contact['name'].lower() or query in contact['phone']:
                results.append(contact)
        self.listbox.delete(0, tk.END)
        for contact in results:
            self.listbox.insert(tk.END, f"{contact['name']} | {contact['phone']} | {contact['email']} | {contact['address']}")
        if not results:
            messagebox.showinfo("No Match", "No contact found with your search.")

    def update_contact(self):
        """Update the selected contact with new info."""
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showwarning("Select Contact", "Please select a contact to update.")
            return
        idx = sel[0]
        fields = self.listbox.get(idx).split(' | ')
        # Fill input fields for easy editing
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)
        self.entry_name.insert(0, fields[0])
        self.entry_phone.insert(0, fields[1])
        self.entry_email.insert(0, fields[2])
        self.entry_address.insert(0, fields)
        # After editing, call add_contact to save changes
        self.contacts.pop(idx)
        self.view_contacts()

    def delete_contact(self):
        """Delete the selected contact."""
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showwarning("Select Contact", "Please select a contact to delete.")
            return
        idx = sel[0]
        contact = self.contacts.pop(idx)
        messagebox.showinfo("Deleted", f"Contact '{contact['name']}' removed.")
        self.view_contacts()

# --- Run the App ---
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
# Hey