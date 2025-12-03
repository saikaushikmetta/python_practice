print("-----WELCOME TO STUDENT MANAGEMENT SYSTEM-----")
student_list=[]
def add_student():
    name=input("enter name: ")
    rollno=int(input("enter roll no: "))
    address=input("enter address: ")
    main={
        'Name':name,
        'Rollno':rollno,
        'Address':address
    }
    student_list.append(main)
    print('student info added succesfully')
def edit():
    edit_name=input("enter name that you want to edit")
    for item in student_list:
        if item['Name']==edit_name:
            item['Name']=input("enter new name")
            print("name has been updated and changed successfully")
        else:
            print("record not found")
    print("do you want edit the roll no type'y/n'")
    edit_rollno=input('enter y/n').lower()
    if edit_rollno == 'y':
        item['Rollno']=int(input("enter new roll no"))
        print("roll no has updated and changed successfully")
    elif edit_rollno=='n':
        pass
    print("do you want edit the address type'y/n'")
    edit_address=input("enter'y/n'").lower()
    if edit_address=='y':
        item["Address"]=input("enter new address")
        print("address has been successfully changed")
    elif edit_address=='n':
        pass
def view_student():
    for i in student_list:
        if i in student_list:
            print("Here is you student list\n",i)
        else:
            print("No record found")
def delete_student():
    del1=input("enter student name  to remove")
    for item in student_list:
        if item['Name']==del1:
            student_list.remove(item)
            print("Deleted successfully")
        else:
            print("Record not found")
def exit_program():
    print("Thanks for using this app")
while True:
    print("\n1.add_student\n2.edit\n3.view\n4.delete\n5.exit")
    user=int(input("enter number to perform task"))
    if user==1:
        add_student()
    elif user==2:
        edit()
    elif user==3:
        view_student()
    elif user==4:
        delete_student()
    elif user==5:
        exit_program()
        break
    else:
        print("wrong choice")