''''
Task 1: Write a function that lets the user add items to a list.
'''

shopping_list = []


while True:
    item = input("Please enter an item for your shopping list (or done to exit): ")
    if item == "done":
        break
    shopping_list.append(item)
    
print(shopping_list)

'''
Task 2: Include a function to remove items from the list.
'''
def remove_item(item):
    return shopping_list.remove(item)


shopping_list = []

while True:
    item = input("Please enter an item for your shopping list (or done to exit): ").lower()
    if item == "done":
        remove = input("Would you like to remove an item before exiting (yes/no)? ").lower()
        if remove == "yes":
            item_removed = input("Which item would you like to remove? ").lower()
            shopping_list.remove(item_removed)
        elif remove == "no":
            print("thank you, you are now exiting the program. ")
    shopping_list.append(item)
    print(shopping_list)
    

'''
Task 3: Add a function that prints out the entire list in a formatted way.
'''
def formatted_print(shopping_list):
    print("Shopping List")
    counter = 0
    for item in shopping_list:
        counter += 1
        print(f"{counter}. {item}")
    


def remove_item(item):
    return shopping_list.remove(item)


shopping_list = []

while True:
    item = input("Please enter an item for your shopping list (or done to exit): ").lower()
    
    if item == "done":
        
        remove = input("Would you like to remove an item before exiting (yes/no)? ").lower()
        
        if remove == "yes":
            
            item_removed = input("Which item would you like to remove? ").lower()
            shopping_list.remove(item_removed)
            
        else:
            
            formatted_print(shopping_list)
            break
    else:
        shopping_list.append(item)
        

