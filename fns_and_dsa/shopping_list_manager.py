def add(list, x):

  list.append(x)
  
def remove(list, x):

  list.remove(x) 

def view(list):
   print(list)  
  
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add(shopping_list, input("Add item: "))
            pass
        elif choice == '2':
            remove(shopping_list, input("remove item: "))
            pass
        elif choice == '3':
            view(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()  