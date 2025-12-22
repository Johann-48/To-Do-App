import os
import json


# List of Items
items = []

# Model of item creation
class Item:
    def __init__(self, title, description, dueDate, priority):
        self.title = title.strip().lower()
        self.description = description
        self.dueDate = dueDate
        self.priority = priority
        self.status = False

# FUNCTIONS
# Add Item Function
def addItem(title, description, dueDate, priority):
    if description == 'NO':
        description = 'Description was not created'
    if dueDate == 'NO':
        dueDate = 'Due Date was not created'

    new_item = Item(str(title), str(description), str(dueDate), str(priority))
    items.append(new_item)

# Add Delete Item Function
def deleteItem(title):
    for i in items:
        if i.title == title:
            items.remove(i)
            return True
    return False

# Add cahnge Status Function
def changeStatus(title):
    for i in items:
        if i.title == title:
            if i.status == False:
                i.status = True
            else:
                i.status = False
            return True
    return False

# Add Show List Function
def showList():
    for i in items:
        if i.status == True:
            statusStr = 'Done'
        elif i.status == False:
            statusStr = 'Not done'

        match i.priority:
            case 1:
                priorityStr = 'Not Important'
            case 2:
                priorityStr = 'Keep In Mind'
            case 3:
                priorityStr = 'Better Do'
            case 4:
                priorityStr = 'Important'
            case 5:
                priorityStr = 'Urgent'

        print(f'- {i.title} // Status: {statusStr} // Due Date: {i.dueDate} // Priority: {priorityStr}')

# Add Show Description Function
def showDescription(title):
    for i in items:
        if i.title == title:
            print(f'{i.description}')
            return True
    return False

# Save the list into a file
def saveList(name):

    basePath = os.path.dirname(os.path.abspath(__file__))
    saveFolder = os.path.join(basePath, "saves")

    # Creates a saves Folder
    os.makedirs(saveFolder, exist_ok=True)

    # Converting into dictionaries
    convertedList = []
    for i in items:
        convertedList.append({
            "title": i.title,
            "description": i.description,
            "dueDate": i.dueDate,
            "priority": i.priority,
            "status": i.status
        })

    savePath = os.path.join(saveFolder, f"{name}.json")

    with open(savePath, "w", encoding="utf-8") as f:
        json.dump(convertedList, f, indent=4)
    print(f"List saved successfully to: {savePath}")


def loadList(path=None):

    basePath = os.path.dirname(os.path.abspath(__file__))
    savePath = path

    if not os.path.exists(savePath):
        print("No saved to-do list found. Starting with an empty list.")
        return
    
    try:

        items.clear()

        with open(savePath, "r", encoding="utf-8") as f:
            loadedData = json.load(f)

        for i in loadedData:
            item = Item(
                title=i["title"],
                description=i["description"],
                dueDate=i["dueDate"],
                priority=i["priority"]
            )
            item.status = i["status"]
            items.append(item)

        print(f"List loaded successfully from: {savePath}")

    except Exception as e:
        print(f"Error loading to-do list: {e}")

# RUNNING PROGRAM

while True:
    break
    # Asks what the user wants to do
    default = input('What do you want to do? (Create/End/Show List/Delete/Change Status/Show Description): ').strip().lower()

    # Filter of the Selected Option
    match default:

        case 'create':
            sampleTitle = str(input('Insert a item: '))
            sampleDescription = str(input('Insert item description (If it doesnt have one, type NO): '))
            sampleDueDate = str(input('Insert a Due Date (Format: DD/MM/YYYY)(If no Due Date, type NO): '))
            samplePriority = int(input('Insertr the item priority (Type from 1 to 5, 1 being not important, and 5 being urgent): '))

            addItem(sampleTitle, sampleDescription, sampleDueDate, samplePriority)
                

        case 'end':
            break

        case 'show list':
            showList()

        case 'delete':
            itemTitle = str(input('Insert the item you want to delete: ')).strip().lower()
            if deleteItem(itemTitle):
                print('Item deleted successfully')
            else:
                print("Item not found")
        
        case 'change status':
            itemTitle = str(input('Insert the item you want to change the status: ')).strip().lower()
            if changeStatus(itemTitle):
                print('Item changed its status')
            else:
                print("Item not found")
        
        case 'show description':
            itemTitle = str(input('Insert the item you want to view description: ')).strip().lower()
            if showDescription(itemTitle):
                print('DESCRIPTION SHOWED')
            else:
                print("Item not found")
            
        case _:
            print('Non-existent option')





# Prints the To-Do List
showList()