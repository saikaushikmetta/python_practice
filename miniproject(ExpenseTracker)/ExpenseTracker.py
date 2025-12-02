#1.add expense with deatails like date,category,description,and amount
#2. view all recorded expenses in a clean format
#3. calculate total spending so far
#4. exit rhe program gracefully when the user chooses
expenses=[]
while True:
    print("-----welcome to money management app-----")
    print("======MENU======")
    print("1.Add expense\n2.View all expenses\n3.View total spending\n4.Exit")
    print("========")
    user=int(input("Enter your choice (1-4)"))
    if user==1:
        date=input("enter the date of transaction")
        category=input("in which neeche you used the money")
        description=input("enter a description about it")
        amount=float(input("enter amount that you spended"))
        dict={"Date":date,
                "Category":category,
                "Description":description,
                "Amount":amount
                }
        expenses.append(dict)
        print("expense added succesfully")
        print("=======")
    elif user==2:
        if len(expenses)==0:
            print("you havent done any transaction yet")
        else:
            count=1
            for i in expenses:
                print(f"spending {count} -> {i['Date']}, {i['Category']}, {i['Description']}, {i['Amount']}")
                count+=1
            print("======")
    elif user==3:
        total=0
        for every_transaction in expenses:
            total = total + every_transaction["Amount"]

        print("\nTotal amount spended",total)
        print("======")
    elif user==4:
        print("Thank you for using this app")
        break
    else:
        print("Invalid choice try again")

        