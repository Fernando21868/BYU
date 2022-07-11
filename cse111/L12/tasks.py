from tkinter import ttk
from tkinter import *

import sqlite3


class Task:

    db_name = 'database.db'

    def __init__(self, window):
        self.wind = window
        self.wind.title('Products Application')

        # Creating a Frame Container
        frame = LabelFrame(self.wind, text='Register a new task')
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        # Name input
        Label(frame, text='Name: ').grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=1, column=1)

        # Description input
        Label(frame, text='Description: ').grid(row=2, column=0)
        self.description = Entry(frame)
        self.description.grid(row=2, column=1)

        print(self.name.get(), self.description.get())

        # Button add task
        ttk.Button(frame, text='Save task', command=self.add_task).grid(
            row=3, columnspan=2, sticky=W+E)

        # Output messages
        self.message = Label(text='', fg='red')
        self.message.grid(row=3, column=0, columnspan=2, sticky=W+E)

        # Table
        self.tree = ttk.Treeview(height=10, columns=2)
        self.tree.grid(row=4, column=0, columnspan=2)
        self.tree.heading('#0', text='Name', anchor=CENTER)
        self.tree.heading('#1', text='Description', anchor=CENTER)

        # Buttons
        ttk.Button(text='DELETE', command=self.delete_task).grid(
            row=5, column=0, sticky=W+E)
        ttk.Button(text='EDIT', command=self.edit_task).grid(
            row=5, column=1, sticky=W+E)

        # Filling tre rows
        self.get_tasks()

    def get_tasks(self):
        # Cleaning table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

        # Quering data
        query = 'SELECT * FROM task ORDER BY name DESC'
        db_rows = self.run_query(query)

        # Filling data
        for row in db_rows:
            self.tree.insert('', 0, text=row[1], values=row[2])

    def add_task(self):
        boolean = validation(self.name.get(), self.description.get())
        if boolean:
            query = 'INSERT INTO task VALUES(NULL, ?, ?)'
            aux_name = format_data(self.name.get())
            aux_description = format_data(self.description.get())
            parameters = (aux_name, aux_description)
            self.run_query(query, parameters)
            self.message['text'] = f'Task {self.name.get()} added successfully'
            self.name.delete(0, END)
            self.description.delete(0, END)
        else:
            self.message['text'] = f'Task and Description are required'

        self.get_tasks()

    def delete_task(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Please select a row'
            return
        self.message['text'] = ''
        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM task WHERE name = ?'
        self.run_query(query, (name,))
        self.message['text'] = f'Task {name} deleted successfully'
        self.get_tasks()

    def edit_task(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Please select a row'
            return
        name = self.tree.item(self.tree.selection())['text']
        old_description = self.tree.item(self.tree.selection())['values'][0]
        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Edit task'

        # Old name
        Label(self.edit_wind, text='Old name: ').grid(row=0, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind,
              value=name), state='readonly').grid(row=0, column=2)
        # New name
        Label(self.edit_wind, text='New name').grid(row=1, column=1)
        new_name = Entry(self.edit_wind)
        new_name.grid(row=1, column=2)

        # Old description
        Label(self.edit_wind, text='Old description: ').grid(row=2, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind,
              value=old_description), state='readonly').grid(row=2, column=2)
        # New description
        Label(self.edit_wind, text='New description').grid(row=3, column=1)
        new_description = Entry(self.edit_wind)
        new_description.grid(row=3, column=2)

        # Button
        Button(self.edit_wind, text='Update',
               command=lambda: self.edit_records(new_name.get(), name, new_description.get(), old_description)).grid(row=4, column=2, sticky=W)

    def edit_records(self, new_name, name, new_description, old_description):
        query = 'UPDATE task SET name = ?, description = ? WHERE name = ? AND description = ?'
        parameters = (new_name, new_description, name, old_description)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.message['text'] = f'Task {name} updated successfully'
        self.get_tasks()

    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result


def format_data(data):
    data = data.upper()
    data = data.strip()
    return data


def validation(name, description):
    return len(format_data(name)) != 0 and len(format_data(description)) != 0


if __name__ == '__main__':
    window = Tk()
    application = Task(window)
    window.mainloop()
