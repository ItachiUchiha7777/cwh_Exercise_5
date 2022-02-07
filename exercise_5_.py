'''


exrcise 5 Health management system
health management system
3 clients Rohan,Harry,Hammad
total 6 fies
write a function which Inputs client name


'''

# opening files

clients = ['Shrey' , 'Itachi' , 'Ishan']
shrey_ecrcise = open ( "shrey_exercise.txt" , 'a' )
ishan_excercise = open ( "Ishan_exercise.txt" , 'a' )


# #date return krne wala functioon
def getdate() :
    """returns time"""
    import datetime
    return datetime.datetime.now ()


# choosing client name
name = int ( input ( "Enter 0 for Itachi:\nEneter 1 for shrey:\nEnter 2 for Ishan:" ) )
if name == 0 :
    person_name = clients[0]
elif name == 1 :
    person_name = clients[1]
elif name == 2 :
    person_name = clients[2]
ask = int ( input ( "type 1 to choose Diet, type 2 to choose exercise  " ) )
enter_or_retrieve = int(input ( " type 1 to input data, type 2 if u want to retrieve data" ))

if enter_or_retrieve == 1 :
    if ask == 1 and 1 == name :

        shrey_diet = open ( "shrey_diet.txt" , 'a' )
        kya_khaya = input ( "what did u ate u fat pig?" )
        getdate ()
        time = getdate ()

        shrey_diet.write ( "What did u ate?? " + kya_khaya + ' at ' )
        shrey_diet.write ( f"time: [{time}] " + '\n' )
        shrey_diet.close
    elif ask == 1 and 0 == name :
        Itachi_diet = open ( "Itachi_diet.txt" , 'a' )
        kya_khaya = input ( "what did u ate u fat pig?" )
        getdate ()
        time = getdate ()

        Itachi_diet.write ( "What did u ate?? " + kya_khaya + ' at ' )
        Itachi_diet.write ( f"time: [{time}] " + '\n' )
        Itachi_diet.close ()
    elif ask == 1 and 2 == name :
        Ishan_diet = open ( "Ishan_diet.txt" , 'a' )
        kya_khaya = input ( "what did u ate u fat pig?" )
        getdate ()
        time = getdate ()

        Ishan_diet.write ( "What did u ate?? " + kya_khaya + ' at ' )
        Ishan_diet.write ( f"time: [{time}] " + '\n' )
        Ishan_diet.close ()

    elif ask == 2 and 1 == name :
        shrey_ecrcise = open ( "shrey_ecrcise" , "a" )
        kya_kia = input ( "which ecxercise u did u fat pig?" )
        getdate ()
        time = getdate ()

        shrey_ecrcise.write ( "exercise name " + kya_kia + ' at ' )
        shrey_ecrcise.write ( f"time: [{time}] " + '\n' )
        shrey_ecrcise.close
    elif ask == 2 and 1 == name :
        Itachi_exercsie = open ( "Itachi_exercsie.txt" , 'a' )
        kya_kia = input ( "which ecxercise u did u fat pig?" )
        getdate ()
        time = getdate ()

        Itachi_exercsie.write ( "Exercise name: " + kya_kia + ' at ' )
        Itachi_exercsie.write ( f"time: [{time}] " + '\n' )
        Itachi_exercsie.close ()
    elif ask == 2 and 2 == name :
        ishan_excercise = open ( "ishan_excercise.txt" , 'a' )
        kya_kia = input ( "which exercise u did u fat pig?" )
        getdate ()
        time = getdate ()

        ishan_excercise.write ( "Exercise name: " + kya_kia + ' at ' )
        ishan_excercise.write ( f"time: [{time}] " + '\n' )
        ishan_excercise.close ()
    print('sorry wrong input plese try again')
elif enter_or_retrieve == 2 :
    if ask == 1 and 0 == name :

        shrey_diet = open ( "shrey_diet.txt" )

        print ( shrey_diet.read () )

        shrey_diet.close
    elif ask == 1 and 0 == name :
        Itachi_diet = open ( "Itachi_diet.txt" )

        print ( Itachi_diet.read () )

        Itachi_diet.close ()
    elif ask == 1 and 2 == name :
        Ishan_diet = open ( "Ishan_diet.txt" )

        print ( Ishan_diet.read () )

        Ishan_diet.close ()

    if ask == 2 and 1 == name :
        shrey_ecrcise = open ( "shrey_ecrcise" )

        print ( shrey_ecrcise.read () )
        shrey_ecrcise.close
    elif ask == 2 and 1 == name :
        Itachi_exercsie = open ( "Itachi_exercsie.txt" , 'a' )

        print ( Itachi_exercsie.read () )
        Itachi_exercsie.close ()
    elif ask == 2 and 2 == name :
        ishan_excercise = open ( "ishan_excercise.txt" , 'a' )

        print ( ishan_excercise.read )
        ishan_excercise.close ()
    else:
        print('sorry wrong input plese try again')
print('sorry wrong input plese try again')

# ask_choice = int ( input ("enter 1 to lock data, enter 2 to retrive data"))


# shrey_ecrcise.close()
# shrey_diet.close()
# ishan_excercise.close()
# ishan_excercise.close()
