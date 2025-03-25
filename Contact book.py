import tkinter as tk
from tkinter import messagebox

# Contact Manager Class
class ContactManager:
    def __init__(self, root):
        self.contacts = {}
        self.root = root
        self.root.title("Contact Manager")

        # Labels and Entries for contact details
        tk.Label(root, text="Name").grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        tk.Label(root, text="Phone Number").grid(row=1, column=0)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1)

        tk.Label(root, text="Email").grid(row=2, column=0)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1)

        tk.Label(root, text="Address").grid(row=3, column=0)
        self.address_entry = tk.Entry(root)
        self.address_entry.grid(row=3, column=1)

        # Buttons for operations
        tk.Button(root, text="Add Contact", command=self.add_contact).grid(row=4, column=0)
        tk.Button(root, text="View Contacts", command=self.view_contacts).grid(row=4, column=1)
        tk.Button(root, text="Search", command=self.search_contact).grid(row=5, column=0)
        tk.Button(root, text="Update", command=self.update_contact).grid(row=5, column=1)
        tk.Button(root, text="Delete", command=self.delete_contact).grid(row=6, column=0)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        if name and phone and email and address:
            self.contacts[name] = (phone, email, address)
            messagebox.showinfo("Added", f"Contact {name} added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "All fields are required!")

    def view_contacts(self):
        contacts_list = "\n".join(f"{name}: {details}" for name, details in self.contacts.items())
        messagebox.showinfo("Contacts List", contacts_list)

    def search_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            contact_details = self.contacts[name]
            messagebox.showinfo("Search Result", f"{name}: {contact_details}")
        else:
            messagebox.showwarning("Not Found", f"No contact found for {name}")

    def update_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()
            self.contacts[name] = (phone, email, address)
            messagebox.showinfo("Updated", f"Contact {name} updated successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Not Found", f"No contact found for {name}")

    def delete_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Deleted", f"Contact {name} deleted successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Not Found", f"No contact found for {name}")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

# Main window
root = tk.Tk()
app = ContactManager(root)
root.mainloop()
