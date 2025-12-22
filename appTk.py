import os
import tkinter as tk
import ttkbootstrap as tkb
from tkinter import ttk, filedialog

# Takes the data from main.py
import main as code

# Window Config
root = tkb.Window(themename = 'morph')
root.title("Table with Entry Widgets")
root.geometry("1000x800")

# Global Variables
isMenuOpen = False

#TABLE
# Create a Treeview widget
columns = ("Title", "Description", "DueDate", "Priority", "Status")
tree = ttk.Treeview(root, columns=columns, show="headings")

# Define column headings
for col in columns:
    tree.heading(col, text=col)

tree.column("Title", anchor="w")
tree.column("Description", anchor="w")
tree.column("DueDate", anchor="center")
tree.column("Priority", anchor="center")
tree.column("Status", anchor="center")

# FUNCTIONS

def packTitle(sampleInput):
    title = sampleInput.get()
    print('GOT', title)
    return title
def packDescription(sampleInput):
    description = sampleInput.get()
    print('GOT', description)
    return description

# This funciton doesn't need .get() because it has already got in the onclick() function
def packDueDate(sampleInput):
    print('GOT', sampleInput)
    return sampleInput
def packPriority(sampleInput):

    priority = sampleInput.get()
    print('GOT', priority)

    # Converts string into number
    try:
        priority = int(priority)
    except ValueError:
        return "Invalid Priority"
    
    # Converts number into text
    if priority == 1:
        result = 'Not Important'
    elif priority == 2:
        result = 'Keep In Mind'
    elif priority == 3:
        result = 'Better Do'
    elif priority == 4:
        result = 'Important'
    elif priority == 5:
        result = 'Urgent'

    return result

def save():

    saveNameLabel = tkb.Label(root, text="Insert Save Name")
    saveNameLabel.pack()
    saveNameInput = tkb.Entry(root, width=30)
    saveNameInput.pack(pady=(0, 10))
    
    def onClick():
        outSaveName = packTitle(saveNameInput)
        saveNameLabel.destroy()
        saveNameInput.destroy()


        okButton.destroy()
        cancelButton.destroy()
        global isMenuOpen
        isMenuOpen = False

        code.saveList(outSaveName)

        refreshTreeview()

    def cancelOnClick():
        saveNameLabel.destroy()
        saveNameInput.destroy()
        okButton.destroy()
        cancelButton.destroy()
        

        global isMenuOpen
        isMenuOpen = False

        refreshTreeview()

    okButton = tkb.Button(root, text='Confirm', command=onClick, bootstyle='success')
    okButton.pack(pady=(0, 10))
    cancelButton = tkb.Button(root, text='Cancel', command=cancelOnClick, bootstyle='warning')
    cancelButton.pack(pady=(0, 10))
    
    
def load():

    initial_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "saves")
    file_path = filedialog.askopenfilename(
        parent=root,
        title="Select saved list",
        initialdir=initial_dir,
        filetypes=[("JSON files", "*.json")]
    )
    if not file_path:
        return
    code.loadList(file_path)
    refreshTreeview()

    

def refreshTreeview():
    for item in tree.get_children():
        tree.delete(item)
    for row in code.items:

        # Changes the Status from Boolean to String
        if row.status == False:
            statusStr = 'Not Done'
        elif row.status == True:
            statusStr = 'Done'

        # Inserts values from (code.) to the tree
        tree.insert("", tkb.END, values=(row.title, row.description, row.dueDate, row.priority, statusStr))

# MAIN FUNCTIONS
def create():
    global isMenuOpen
    isMenuOpen = True
    # Title
    titleLabel = tkb.Label(root, text="Title")
    titleLabel.pack()
    sampleTitle = tkb.Entry(root, width=30)
    sampleTitle.pack(pady=(0, 10))

    # Description
    descriptionLabel = tkb.Label(root, text="Description")
    descriptionLabel.pack()
    sampleDescription = tkb.Entry(root, width=30)
    sampleDescription.pack(pady=(0, 10))

    # Due Date
    dueDateLabel = tkb.Label(root, text="Due Date")
    dueDateLabel.pack()
    sampleDueDate = tkb.DateEntry(root, width=30)
    sampleDueDate.pack(pady=(0, 10))

    # Priority
    priorityLabel = tkb.Label(root, text="Priority (1-5)")
    priorityLabel.pack()
    samplePriority = tkb.Entry(root, width=30)
    samplePriority.pack(pady=(0, 10))

    def onClick():
        outTitle = packTitle(sampleTitle)
        sampleTitle.destroy()
        titleLabel.destroy()

        outDescription = packDescription(sampleDescription)
        sampleDescription.destroy()
        descriptionLabel.destroy()

        # Getting and Transforming into str
        selectedDate = sampleDueDate.entry.get()

        outDueDate = packDueDate(selectedDate)
        sampleDueDate.destroy()
        dueDateLabel.destroy()

        outPriority = packPriority(samplePriority)
        samplePriority.destroy()
        priorityLabel.destroy()

        okButton.destroy()
        cancelButton.destroy()
        global isMenuOpen
        isMenuOpen = False

        code.addItem(outTitle, outDescription, outDueDate, outPriority)  

        refreshTreeview()

    def cancelOnClick():
        sampleTitle.destroy()
        titleLabel.destroy()
        sampleDescription.destroy()
        descriptionLabel.destroy()
        sampleDueDate.destroy()
        dueDateLabel.destroy()
        samplePriority.destroy()
        priorityLabel.destroy()
        okButton.destroy()
        cancelButton.destroy()

        global isMenuOpen
        isMenuOpen = False

        refreshTreeview()

    okButton = tkb.Button(root, text='Confirm', command=onClick, bootstyle='success')
    okButton.pack(pady=(0, 10))
    cancelButton = tkb.Button(root, text='Cancel', command=cancelOnClick, bootstyle='warning')
    cancelButton.pack(pady=(0, 10))



def status():
    global isMenuOpen
    isMenuOpen = True
    sampleTitle = tkb.Entry(root, width=30)
    sampleTitle.insert(0, "Title")
    sampleTitle.pack(pady=10)

    def onClick():
        search = packTitle(sampleTitle)
        sampleTitle.destroy()
        okButton.destroy()
        cancelButton.destroy()


        global isMenuOpen
        isMenuOpen = False

        code.changeStatus(search)

        refreshTreeview()

    def cancelOnClick():
        sampleTitle.destroy()
        okButton.destroy()
        cancelButton.destroy()

        global isMenuOpen
        isMenuOpen = False

        refreshTreeview()

    okButton = tkb.Button(root, text='Confirm', command=onClick)
    okButton.pack(pady=(0, 10))
    cancelButton = tkb.Button(root, text='Cancel', command=cancelOnClick, bootstyle='warning')
    cancelButton.pack(pady=(0, 10))



def delete():
    global isMenuOpen
    isMenuOpen = True
    sampleTitle = tkb.Entry(root, width=30)
    sampleTitle.insert(0, "Title")
    sampleTitle.pack(pady=10)

    def onClick():
        search = packTitle(sampleTitle)
        sampleTitle.destroy()
        okButton.destroy()
        cancelButton.destroy()

        global isMenuOpen
        isMenuOpen = False

        code.deleteItem(search)

        refreshTreeview()

    def cancelOnClick():
        sampleTitle.destroy()
        okButton.destroy()
        cancelButton.destroy()

        global isMenuOpen
        isMenuOpen = False

        refreshTreeview()

    okButton = tkb.Button(root, text='Confirm', command=onClick)
    okButton.pack(pady=(0, 10))
    cancelButton = tkb.Button(root, text='Cancel', command=cancelOnClick, bootstyle='warning')
    cancelButton.pack(pady=(0, 10))

# CHECKERS (Meant To be ran and run the other functions)

def runCreateChecker():
    global isMenuOpen
    if isMenuOpen == False:
        create()

def runStatusChecker():
    global isMenuOpen
    if isMenuOpen == False:
        status()

def runDeleteChecker():
    global isMenuOpen
    if isMenuOpen == False:
        delete()

# BUTTONS

createButton = tkb.Button(root, text = 'Create', command = runCreateChecker)
statusButton = tkb.Button(root, text = 'Change Status', command = runStatusChecker)
deleteButton = tkb.Button(root, text = 'Delete Item', command = runDeleteChecker)
saveButton = tkb.Button(root, text = 'Save List', command = save)
loadButton = tkb.Button(root, text = 'Load List', command = load)


# Pack the Treeview
tree.pack(fill=tkb.BOTH, expand=True)

createButton.pack(padx=5, pady=10)
statusButton.pack(padx=5, pady=10)
deleteButton.pack(padx=5, pady=10)
saveButton.pack(padx=5, pady=10)
loadButton.pack(padx=5, pady=10)

root.mainloop()