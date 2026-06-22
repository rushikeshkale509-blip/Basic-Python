'''Wap to create a class student with instace variable
 stdname stdid stdmo Accept and print the details
 for one student'''

'''class student:
    def accept(self):
        self.student_name = input("Enter a name: ")
        self.student_id = input("Enter an id: ")
        self.student_mo = input("Enter a mobile number: ")

    def print_details(self):
        print("Student Name:", self.student_name)
        print("Student ID:", self.student_id)
        print("Student Mobile Number:", self.student_mo)

s1 = student()
s1.accept()
s1.print_details()'''


'''Wap to create a class customer with customer
ID name emailid mo.no.use construction to initialize
instance variable and print details'''


class Customer:
    def __init__(self, id, name, email, mobile):
        self.customer_id = id
        self.name = name
        self.email = email
        self.mobile = mobile

    def print_details(self):
        print("Customer ID :", self.customer_id)
        print("Name        :", self.name)
        print("Email ID    :", self.email)
        print("Mobile No.  :", self.mobile)

id = int(input("Enter Customer ID: "))
name = input("Enter Name: ")
email = input("Enter Email ID: ")
mobile = input("Enter Mobile Number: ")

c1 = Customer(id, name, email, mobile)

c1.print_details()