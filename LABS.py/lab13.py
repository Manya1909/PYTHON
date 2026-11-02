inventory=["Notebook", "Pen", "Eraser", "Ruler"]

while True:
    print("Select an operation:")
    print("1. View")
    print("2. Add")
    print("3. Remove")
    print("4. Sort")
    print("5. Exit")

    choice=input("Enter choice (1-5): ").strip()

    if choice == "1":
        print(inventory)

    elif choice == "2":
        add_element=input("Enter a new element:")
        inventory.append(add_element)
        print(f'[Success] "{add_element}"element added')

    elif choice == "3":
        rem_element=input("Enter element to be removed:")
        inventory.remove(rem_element)
        print(f'[Success] "{rem_element}"element removed:')

        for i in range(len(inventory)):
            print(f"{i+1}.inventory")

    elif choice == "4":
        inventory.sort()
        print(inventory)
    elif choice == "5":
        print("Thank you. Goodbye!")
    else:
        print("Invalid")
