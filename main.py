#GADS ASSIGNMENT DONE BY ABHIJITH U

#Main Array
arr = []

def InsertatPos(inp, pos):
    if len(arr)+1 < pos or pos < 0:
        print("Sorry, Element cannot be inserted at that position. The size of Array is "+str(len(arr)))
        newpos = input("Enter the new position (range upto " + str(len(arr)+1) + ") ")
        if newpos == "menu":
            print()
            mainmenu()
        try:
            newpos = int(newpos)
        except ValueError as ve:
            print("This algorithm is designed to work with only integers...")
            print()
            mainmenu()
        except TypeError as te:
            print("This algorithm is designed to work with only integers...")
            print()
            mainmenu()

        InsertatPos(inp, newpos)
    else:
        if pos == 0:
            print("0 position is not possible...")
            newpos = input("Enter the new position (range upto " + str(len(arr) + 1) + ") ")

            if newpos == "menu":
                print()
                mainmenu()
            try:
                newpos = int(newpos)
            except ValueError as ve:
                print("This algorithm is designed to work with only integers...")
                print()
                mainmenu()
            except TypeError as te:
                print("This algorithm is designed to work with only integers...")
                print()
                mainmenu()

            InsertatPos(inp, newpos)
        else:
            arr.insert(pos-1, inp)
            print("Element Inserted ....")
            print(arr)
    print()


def Insertatpos2():
    inp = input("Enter the element to be Inserted = ")

    if inp == "menu":
        print()
        mainmenu()
    try:
        inp = int(inp)
    except ValueError as ve:
        print("This algorithm is designed to work with only integers...")
        print()
        mainmenu()
    except TypeError as te:
        print("This algorithm is designed to work with only integers...")
        print()
        mainmenu()

    InsertatPos(inp, len(arr)+1)


def InsertElement():
    inp = input("Enter the element to be Inserted = ")
    pos = input("Enter the position to be Inserted = (range upto " + str(len(arr) + 1) + ") ")

    if inp == "menu" or pos == "menu":
        print()
        mainmenu()
    try:
        inp = int(inp)
        pos = int(inp)
    except ValueError as ve:
        print("This algorithm is designed to work with only integers...")
        print()
        mainmenu()
    except TypeError as te:
        print("This algorithm is designed to work with only integers...")
        print()
        mainmenu()



    if len(arr)+1 < pos or pos < 0:
        print("Sorry, Element cannot be inserted at that position. The current length of the Array is "+str(len(arr)))
        newpos = input("Enter the new position (range upto " + str(len(arr)+1) + ") ")

        if newpos == "menu":
            print()
            mainmenu()
        try:
            newpos = int(newpos)
        except ValueError as ve:
            print("This algorithm is designed to work with only integers...")
            print()
            mainmenu()
        except TypeError as te:
            print("This algorithm is designed to work with only integers...")
            print()
            mainmenu()

        InsertatPos(inp, newpos)
    else:
        if pos == 0:
            print("0 position is not possible...")
            newpos = input("Enter the new position (range upto " + str(len(arr) + 1) + ") ")

            if newpos == "menu":
                print()
                mainmenu()
            try:
                newpos = int(newpos)
            except ValueError as ve:
                print("This algorithm is designed to work with only integers...")
                print()
                mainmenu()
            except TypeError as te:
                print("This algorithm is designed to work with only integers...")
                print()
                mainmenu()

            InsertatPos(inp, newpos)
        else:
            arr.insert(pos-1, inp)
            print("Element Inserted ....")
            print(arr)
    print()

def findelement(inp):
    ret = []
    for i in range(len(arr)):
        if inp == arr[i]:
            ret.append(i+1)
    return ret

def delloop(inp):
    l = len(arr)
    for i in range(l):
        if inp == arr[i]:
            arr.pop(i)
            #print(arr)
            break

def delloop2(inp):
    print()
    print(arr)
    print("Positions given element is found " + str(findelement(inp)))
    ind = input("Enter the position to be deleted : ")

    if ind == "menu":
        print()
        mainmenu()
    try:
        ind = int(ind)
    except ValueError as ve:
        print("This algorithm is designed to work with only integers...")
        print()
        mainmenu()
    except TypeError as te:
        print("This algorithm is designed to work with only integers...")
        print()
        mainmenu()


    if ind not in findelement(inp):
        print("The position given is not that of the current given element. Try Again")
        delloop2(inp)
    else:
        DeleteElementatpos2(ind)
        if arr.count(inp) > 0:
            print("Do you want to Delete another index... (Y | N)")
            op2 = input()
            if op2 == "Y":
                delloop2(inp)
            elif op2 == "N":
                print("Returning to Main Menu")
            else:
                print()
                print("Invalid Input !!")
                print()
    print()


def DeleteElement():
    inp = input("Enter the item to be deleted = ")

    if inp == "menu":
        print()
        mainmenu()
    try:
        inp = int(inp)
    except ValueError as ve:
        print("This algorithm is designed to work with only integers...")
        print()
        mainmenu()
    except TypeError as te:
        print("This algorithm is designed to work with only integers...")
        print()
        mainmenu()

    if inp not in arr:
        print("Your Element "+str(inp)+" is not present in the array. Do you want to insert it ? (Y | N)")
        ques = input()
        if ques == "Y":
            newpos = input("Enter the position to insert the element (range upto " + str(len(arr) + 1) + ") ")

            if newpos == "menu":
                print()
                mainmenu()
            try:
                newpos = int(newpos)
            except ValueError as ve:
                print("This algorithm is designed to work with only integers...")
                print()
                mainmenu()
            except TypeError as te:
                print("This algorithm is designed to work with only integers...")
                print()
                mainmenu()


            InsertatPos(inp, newpos)
        elif ques == "N":
            print("Returning to main menu")

        else:
            print()
            print("Invalid Input !!")
            print()

    else:
        if arr.count(inp) > 1:
            print("Your Element is found "+str(arr.count(inp))+" times.")
            print("Options")
            print("----------")
            print("1. Delete all occurances")
            print("2. Delete elements at given index")
            print("========================================================================")
            op = input("Enter the option (1 or 2) : ")

            if op == "menu":
                print()
                mainmenu()
            try:
                op = int(op)
            except ValueError as ve:
                print("This algorithm is designed to work with only integers...")
                print()
                mainmenu()
            except TypeError as te:
                print("This algorithm is designed to work with only integers...")
                print()
                mainmenu()

            if op == 1:
                for val in arr:
                    delloop(inp)
                print(arr)
            elif op == 2:
                print()
                print(arr)
                print("Positions given element is found " + str(findelement(inp)))
                ind = int(input("Enter the position to be deleted : "))
                if ind not in findelement(inp):
                    print("The position given is not that of the current given element. Try Again")
                    delloop2(inp)
                else:
                    DeleteElementatpos2(ind)
                    if arr.count(inp) > 0:
                        print("Do you want to Delete another index... (Y | N)")
                        op2 = input()
                        if op2 == "Y":
                            delloop2(inp)
                        elif op2 == "N":
                            print("Returning to Main Menu")
                        else:
                            print()
                            print("Invalid Input !!")
                            print()
            else:
                print()
                print("Invalid Input !!")
                print()

        else:
            delloop(inp)
            print(arr)
    print()

def DeleteElementatpos2(pos):
    if pos <= 0 or pos > len(arr):
        print("Sorry, Cannot delete element at that position. The current length of the Array is " + str(len(arr)))
        newpos = input("Enter the new position (range upto " + str(len(arr)) + ") ")

        if newpos == "menu":
            print()
            mainmenu()
        try:
            newpos = int(newpos)
        except ValueError as ve:
            print("This algorithm is designed to work with only integers...")
            print()
            mainmenu()
        except TypeError as te:
            print("This algorithm is designed to work with only integers...")
            print()
            mainmenu()

        DeleteElementatpos2(newpos)
    else:
        arr.pop(pos-1)
        print(arr)
    print()

def DeleteElementatpos():
    print()
    print(arr)
    pos = input("Enter the position of the element to be Deleted = (range upto " + str(len(arr)) + ") ")

    if pos == "menu":
        print()
        mainmenu()
    try:
        pos = int(pos)
    except ValueError as ve:
        print("This algorithm is designed to work with only integers...")
        print()
        mainmenu()
    except TypeError as te:
        print("This algorithm is designed to work with only integers...")
        print()
        mainmenu()

    if pos <= 0 or pos > len(arr):
        print("Sorry, Cannot delete element at that position. The current length of the Array is " + str(len(arr)))
        newpos = input("Enter the new position (range upto " + str(len(arr)) + ") ")

        if newpos == "menu":
            print()
            mainmenu()
        try:
            newpos = int(newpos)
        except ValueError as ve:
            print("This algorithm is designed to work with only integers...")
            print()
            mainmenu()
        except TypeError as te:
            print("This algorithm is designed to work with only integers...")
            print()
            mainmenu()


        DeleteElementatpos2(newpos)
    else:
        arr.pop(pos-1)
        print(arr)
    print()

def SearchElement():
    print()
    inp = input("Enter the Element to search = ")

    if inp == "menu":
        print()
        mainmenu()
    try:
        inp = int(inp)
    except ValueError as ve:
        print("This algorithm is designed to work with only integers...")
        print()
        mainmenu()
    except TypeError as te:
        print("This algorithm is designed to work with only integers...")
        print()
        mainmenu()

    if inp in arr:
        print(str(inp)+" is found " + str(arr.count(inp)) + " times.")
        print("The positions are " + str(findelement(inp)))
    else:
        print("The entered Element is not found in the array...")
        print("Search Again ? (Y | N)")
        op = input()
        if op == "Y":
            SearchElement()
        elif op == "N":
            print("Returning to Main Menu")
        else:
            print()
            print("Invalid Input !!")
            print()
    print()

def SearchElementatPos2(pos):
    if pos <= 0 or pos > len(arr):
        print("Sorry, position range is out of limit. The current length of the Array is " + str(len(arr)))
        newpos = input("Enter the new position (range upto " + str(len(arr)) + ") ")

        if newpos == "menu":
            print()
            mainmenu()
        try:
            newpos = int(newpos)
        except ValueError as ve:
            print("This algorithm is designed to work with only integers...")
            print()
            mainmenu()
        except TypeError as te:
            print("This algorithm is designed to work with only integers...")
            print()
            mainmenu()

        SearchElementatPos2(newpos)
    else:
        print("Element at position " + str(pos) + " is " + str(arr[pos-1]))
    print()

def SearchElementatPos():
    print()
    pos = input("Enter the position to Search = (range upto " + str(len(arr)) + ") ")

    if pos == "menu":
        print()
        mainmenu()
    try:
        pos = int(pos)
    except ValueError as ve:
        print("This algorithm is designed to work with only integers...")
        print()
        mainmenu()
    except TypeError as te:
        print("This algorithm is designed to work with only integers...")
        print()
        mainmenu()

    if pos <= 0 or pos > len(arr):
        print("Sorry, position range is out of limit. The current length of the Array is " + str(len(arr)))
        newpos = input("Enter the new position (range upto " + str(len(arr)) + ") ")

        if newpos == "menu":
            print()
            mainmenu()
        try:
            newpos = int(newpos)
        except ValueError as ve:
            print("This algorithm is designed to work with only integers...")
            print()
            mainmenu()
        except TypeError as te:
            print("This algorithm is designed to work with only integers...")
            print()
            mainmenu()

        SearchElementatPos2(newpos)
    else:
        print("Element at position "+str(pos)+" is "+str(arr[pos-1]))
    print()


def mainmenu():
    print("ARRAY CODE - GADS")
    print("----------------------")
    print("1. Insert Element at the end of the array")
    print("2. Insert Element at a given position")
    print("3. Delete a given Element")
    print("4. Delete an Element at a given position")
    print("5. Search for an Element")
    print("6. Search for an Element using given position")
    print("7. Display Array")
    print("8. Instructions")
    print("9. Exit")
    print("========================================================================")
    op = input("Enter the option (1 - 9) : ")

    if op == "menu":
        print()
        mainmenu()
    try:
        op = int(op)
    except ValueError as ve:
        print("This algorithm is designed to work with only integers...")
        print()
        mainmenu()
    except TypeError as te:
        print("This algorithm is designed to work with only integers...")
        print()
        mainmenu()

    if op == 1:
        print()
        Insertatpos2()
        print()
    elif op == 2:
        print()
        InsertElement()
        print()
    elif op == 3:
        print()
        DeleteElement()
        print()
    elif op == 4:
        print()
        DeleteElementatpos()
        print()
    elif op == 5:
        print()
        SearchElement()
        print()
    elif op == 6:
        print()
        SearchElementatPos()
        print()
    elif op == 7:
        print()
        print("Current Status of array is : ")
        print(arr)
        print()
    elif op == 8:
        print()
        print("---------------Instructions------------------")
        print("     * Type 'menu' to get back to mainmenu")
        print("     * The Algorithm is designed to get only numbers.")
        print("     * Invalid Entry may cause data loss.")
        print()
        print()
    elif op == 9:
        print()
        print("Thank you for using my algorithm :)")
        exit()

    else:
        print()
        print("Invalid Input !!")
        print()
while True:
    print()
    mainmenu()