def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")
def add_contact(contact_book):
    name=input()
    phone=input()
    email=input()
    address=input()
    if name in contact_book.keys():
        print("Contact already exists!")
    else:
        contact_book[name] = {"phone": phone, "email": email, "address": address}
        print("Contact added successfully!")
def view_contact(contact_book):
    name=input()
    if name in contact_book.keys():
        print("Name:",name)
        print("Phone:",contact_book[name]["phone"])
        print("Email:",contact_book[name]["email"])
        print("Address:",contact_book[name]["address"])
    else:
        print("Contact not found!")
def edit_contact(contact_book):
    name=input()
    if name in contact_book:
        phone=input()
        mail=input()
        address=input()
        contact_book[name] = {"phone": phone, "email": mail, "address": address}
        print("Contact updated successfully!")
    else:
        print("Contact not found!")
def delete_contact(contact_book):
    name=input()
    if name in contact_book:
        p=contact_book.pop(name)
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")
def list_all_contacts(contact_book):
    if contact_book=={}:
        print("No contacts available.")
    else:
        for i in contact_book.keys():
            print("Name:",i)
            print("Phone:",contact_book[i]["phone"])
            print("Email:",contact_book[i]["email"])
            print("Address:",contact_book[i]["address"])
            print()
contact_book={}
j=int(input())
while j!=6 :
        display_menu()
        if j==1 :
            add_contact(contact_book)
        elif j==2 :
            view_contact(contact_book)
        elif j==3 :
            edit_contact(contact_book)
        elif j==4 :
            delete_contact(contact_book)
        elif j==5 :
            list_all_contacts(contact_book)
        else :
            print("Invalid choice. Please try again.")
        j=int(input())
display_menu()
        



