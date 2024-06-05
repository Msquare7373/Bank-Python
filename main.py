# Bank System

def c_account():
    accno = input("Enter account number: ")
    name = input("Enter account name: ")
    balance = input("Enter initial balance: ")

    with open("db.txt", "a") as dfile:
        dfile.write(f"{accno},{name},{balance}\n")

    print("Account created successfully!")

def deposit():
    accno = input("Enter account number: ")
    amt = input("Enter amount to deposit: ")

    with open("db.txt", "r+") as dfile:
        data = dfile.readlines()
        dfile.seek(0)
        for line in data:
            xx = line.strip().split(",")
            if xx[0] == accno:
                xx[2] = str(int(xx[2]) + int(amt))
                dfile.write(",".join(xx) + "\n")
            else:
                dfile.write(line)
        dfile.truncate()

    print("Deposit successful!")

def withdraw():
    accno = input("Enter account number: ")
    amt = input("Enter amount to withdraw: ")

    with open("db.txt", "r+") as dfile:
        data = dfile.readlines()
        dfile.seek(0)
        for line in data:
            xx = line.strip().split(",")
            if xx[0] == accno:
                if int(xx[2]) >= int(amt):
                    xx[2] = str(int(xx[2]) - int(amt))
                    dfile.write(",".join(xx) + "\n")
                else:
                    print("Insufficient balance!")
                    dfile.write(line)
            else:
                dfile.write(line)
        dfile.truncate()

    print("Withdrawal successful!")

def display_balance():
    accno = input("Enter account number: ")

    with open("db.txt", "r") as dfile:
        for line in dfile:
            xx = line.strip().split(",")
            if xx[0] == accno:
                print(f"Balance: {xx[2]}")

while True:
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display Balance")
    print("5. Exit")

    xc = input("Enter your option: ")

    if xc == "1":
        c_account()
    elif xc == "2":
        deposit()
    elif xc == "3":
        withdraw()
    elif xc == "4":
        display_balance()
    elif xc == "5":
        break
    else:
        print("Invalid option!")
