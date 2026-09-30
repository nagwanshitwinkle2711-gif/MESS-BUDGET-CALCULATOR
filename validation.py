def get_amount():
    while True:
        amount = input("Enter amount: ")

        if amount.isdigit():
            amount = int(amount)

            if amount > 0:
                return amount
            else:
                print("Amount must be greater than 0.")

        else:
            print("Please enter a valid number.")
