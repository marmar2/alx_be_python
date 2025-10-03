def add(List, x):

  List.append(x)
  
def remove(List, x):

  List.remove(x) 

def view(List):
   print(List)  
  
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
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add(shopping_list, int(input("Add item: ")))
            pass
        elif choice == 2:
            remove(shopping_list, int(input("remove item: ")))
            pass
        elif choice == 3:
            view(shopping_list)
            pass
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()  