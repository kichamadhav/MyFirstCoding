lst1 = ["#","X","O","!","!!","!!!"] #Assiging the List of Symbols
lst2 = [5, 3, 1, -1, -3, -5] # Assigning the List of Values
dict1 = dict(zip(lst1,lst2)) # Assigning Value to the Symbols by converting the two list to dictionary
lst3 = [] # Empty List to Collect the Symbols Selected by User
lst4 =[] # Empty List to Match Values of Symbols in Lst3

b = 1

while b != 0:
    try:
        Times = int(input("Enter How Many Symbols you want " )) # Asking the user for How many Symbols he will select
    except (ValueError, IndexError):
        print('This is not a valid selection')
        continue
    b = b-1


i = int(Times) # Above Value Converted to int and stored in "i"

# If user Selecting 0 times the code will end and print "Bye"

if i < 1:
    print("Bye")

#If user input not equal to 0, then prompt the user to select a
# symbol and verify whether the symbol is there in lst1 or not and append the same to lst3.

x = 1
while i >=x:
    Symbol = input("Select Your Symbol from : # , X, O, !, !! or !!!")
    y = lst1.count(Symbol)
    if y ==1:
            lst3.append(Symbol)
            i = i - 1
    elif y != 1:
            print("Wrong Selection - Available Symbols : # , X, O, !, !! or !!!")
            i = i

print('You have selected {}'.format(lst3))

a = len(lst3)

while a !=0 :
    for k in lst3:
        if k in dict1:

            lst4.append(dict1.get(k))
            a = a -1

        if sum(lst4)>=0 :
            result = sum(lst4)
        else:
            result = 0

    print("Sum of the Selected Symbol: {}".format(result))