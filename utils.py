def show_menu():
    print("======TO DO APP======")
    print("1. Add tasks\n2. View tasks\n3. Mark task as completed\n4. Delete task\n5. Exit")

def get_choice():
    while True:
        try:
            return int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
