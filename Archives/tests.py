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

# LIST
# Sets Variables
columns = ("Title", "Description", "DueDate", "Priority", "Status")

# List Frame
listFrame = tkb.Frame(root)
listFrame.pack(fill="both", expand=True)

# Canvas and Scrollbar
canvas = tk.Canvas(listFrame, highlightthickness=0)
scrollbar = tkb.Scrollbar(listFrame, orient='vertical', command=canvas.yview)\

canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side='right', fill='y')
canvas.pack(side='left', fill='both', expand=True)

# Items Container
itemsContainer = tkb.Frame(canvas)
canvas.create_window((0, 0), window=itemsContainer, anchor="nw")

itemsContainer.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

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

        refreshList()

    def cancelOnClick():
        saveNameLabel.destroy()
        saveNameInput.destroy()
        okButton.destroy()
        cancelButton.destroy()
        

        global isMenuOpen
        isMenuOpen = False

        refreshList()

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
    refreshList()

    

def refreshList():
    for widget in itemsContainer.winfo_children():
        widget.destroy()

    for item in code.items:
        itemCardRenderer(item)

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

        refreshList()

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

        refreshList()

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

        refreshList()

    def cancelOnClick():
        sampleTitle.destroy()
        okButton.destroy()
        cancelButton.destroy()

        global isMenuOpen
        isMenuOpen = False

        refreshList()

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

        refreshList()

    def cancelOnClick():
        sampleTitle.destroy()
        okButton.destroy()
        cancelButton.destroy()

        global isMenuOpen
        isMenuOpen = False

        refreshList()

    okButton = tkb.Button(root, text='Confirm', command=onClick)
    okButton.pack(pady=(0, 10))
    cancelButton = tkb.Button(root, text='Cancel', command=cancelOnClick, bootstyle='warning')
    cancelButton.pack(pady=(0, 10))

# Functions of Cards   

def formatPriority(priority):
    """Return human-readable priority label."""
    # If your item.priority is already text, just return it.
    if isinstance(priority, str):
        return f"Priority: {priority}"

    mapping = {
        1: "Not Important",
        2: "Keep In Mind",
        3: "Better Do",
        4: "Important",
        5: "Urgent",
    }
    return f"Priority: {mapping.get(priority, priority)}"


def formatStatus(status):
    """Return human-readable status label."""
    # Adjust to match whatever your `item.status` actually stores (bool/int/str).
    if isinstance(status, bool):
        return "Done" if status else "Not Done"
    return str(status)


def toggleStatus(item):
    """UI callback: toggle status for this item, then re-render list."""
    # If main.py only supports changeStatus(title), reuse that.
    code.changeStatus(item.title)
    refreshList()


def deleteItem(item):
    """UI callback: delete this item, then re-render list."""
    code.deleteItem(item.title)
    refreshList()

def itemCardRenderer(item):
    card = tkb.Frame(itemsContainer, padding=10, relief="ridge")
    card.pack(fill="x", pady=6, padx=8)

    title = ttk.Label(card, text=item.title, font=("Segoe UI", 11, "bold"))
    title.pack(anchor="w")

    desc = ttk.Label(card, text=item.description, wraplength=500)
    desc.pack(anchor="w", pady=(2, 4))

    meta = ttk.Frame(card)
    meta.pack(fill="x")

    ttk.Label(meta, text=f"Due: {item.dueDate}").pack(side="left")
    ttk.Label(meta, text=formatPriority(item.priority)).pack(side="left", padx=10)

    status = ttk.Label(meta, text=formatStatus(item.status))
    status.pack(side="right")

    actions = ttk.Frame(card)
    actions.pack(anchor="e", pady=(6, 0))

    ttk.Button(actions, text="Done", command=lambda: toggleStatus(item)).pack(side="left")
    ttk.Button(actions, text="Delete", command=lambda: deleteItem(item)).pack(side="left", padx=4)


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


createButton.pack(padx=5, pady=10)
statusButton.pack(padx=5, pady=10)
deleteButton.pack(padx=5, pady=10)
saveButton.pack(padx=5, pady=10)
loadButton.pack(padx=5, pady=10)

root.mainloop()