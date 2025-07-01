con = 1
starter=[]
menu=[]
d=[]
print("--------------------WELCOME TO MY RESTURANT--------------------")
def starters(starter):
    n = int(input("Enter a number for add the item(starter):"))
    for i in range(1,n+1):
        s = str(input("Enter  a name of starter:"))
        starter.append(s)
    return starter
    
def maincourse(menu):
    n = int(input("Enter a number for add the item(maincourse):"))
    for i in range(1,n+1):
        m = str(input("Enter a name of maincourse:"))
        menu.append(m)
    return menu
def desert(d):
    n = int(input("Enter a number for add the item(desert):"))
    for i in range(1,n+1):
        de = str(input("Enter a  name of desert:"))
        d.append(de)
    return d
while con == 1:
    choice = int(input("1 for starter\n 2 for main-course\n 3 for desert \n Choose any option"))    
    if choice == 1:
        s1 = starters(starter)
        print(s1)
    elif choice == 2:
        m = maincourse(menu)
        print(m)
    elif choice == 3:
        d1 = desert(d)
        print(d1)
    con = int(input("Do you want to add another item?? ......If you want then press 1 or another for exit......"))


#**************************************************************************************************************************************

l1=[]
l2=[]
l3=[]

def starter2(s1,l1):
    print("-----Choose the starter-----")
    for i in s1:
        print(i)
    num = str(input("Enter a name which you want from starter:"))
    if num in s1:
        l1.append(num)
    else:
        print("This item isn't available") 
    return l1
def main(m,l2):
    print("-----Choose the main-course-----")
    for i in m:
        print(i)
    m1 = str(input("Enter a name which you  want from main-course:"))
    if m1 in m:
        l2.append(m1)
    else:
        print("This item isn't available") 
    return l2
def des(d1,l3):
    print("-----Choose the desert-----")
    for i in d1:
        print(i)
    d2 = str(input("Enter a name which you  want from desert:"))
    if d2 in d1:
        l3.append(d2)
    else:
        print("This item isn't available") 
    return l3
count = 1
while count == 1:
    choose = (input("i for starter\n ii for main-course\n iii for desert\n Choose your choice:"))
    if choose == "i":
        l1 = starter2(s1,l1)
        print(l1)
    elif choose == "ii":
        l2 = main(m,l2)
        print(l2)
    elif choose == "iii":
        l3 = des(d1,l3)
        print(l3)
    count = int(input("Press 1 for continue or exit for other..."))


