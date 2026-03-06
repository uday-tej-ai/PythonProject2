def get_user_info():
    name = input("Enter your name: ")
    while True:
        age_input = input("Enter your age: ")
        if age_input.isdigit():
            age = int(age_input)
            break
        else:
            print("That doesn't look like a number. Please try again.")
#uday
    #age
    #changed version-->
    print("\n--- Profile Created ---")
    print(f"User: {name}")
    print(f"Status: {age} years old")


get_user_info()