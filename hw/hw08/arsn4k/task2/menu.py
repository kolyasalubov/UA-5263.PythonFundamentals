def show_menu():
    """
    This function shows menu with 4 options.

    Returns: user's choice.
    """
    print("_ " * 20)
    print("\n1. Calculate the area of a rectangle.")
    print("2. Calculate the area of a triangle.")
    print("3. Calculate the area of a circle.")
    print("4. Exit...")
    print("_ " * 20)

    user_choice = int(input("\nEnter your choice: "))
    if user_choice < 1 or user_choice > 4:
        print("Invalid choice. Please try again.")
        return show_menu()
    return user_choice