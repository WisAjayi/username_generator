import random
from random import choice, randint, shuffle
import os

base_path = os.getcwd()
print(base_path)


#Generate random numbers for SELECTIONS
hah = randint(0,84) # STARWARS
zah = randint(0,87) # QUANTUM
mah = randint(0,99) # TECH NAMES
lah = randint(0,169) # TECH WORDS
tah = randint(0,96) # WOW
jah = randint(0,457) # AMERICAN

#print(hah)
#print(zah)
#print(mah)
#print(lah)
#print(tah)
#print(jah)

def random_gen():
    
    
    

    #First Selection of files
    First = "Q","S","T"
    fah = choice(First)
    print(fah)
    if fah == "S":
        with open("DataUsername/starwars.txt","r") as file:
            contents = file.readlines()
            random.shuffle(contents)

        flex = contents[hah]
        #print(flex)

    elif fah == "Q":
        with open("DataUsername/quantum.txt", "r") as file:
            container = file.readlines()
            random.shuffle(container)

        wow = container[zah]
        #print(wow)

    elif fah == "T":
        with open("DataUsername/wow.txt", "r") as file:
            contains = file.readlines()
            random.shuffle(contains)

        zoo = contains[tah]
        #print(wow)




    #Second collections of Files
    Second = "N","W","A"
    gah = choice(Second)
    print(gah)

    if gah == "N":
        with open("DataUsername/tech.txt","r") as file:
            holder = file.readlines()
            random.shuffle(holder)

        doom = holder[mah]
        #print(doom)

    elif gah == "W":
        with open("DataUsername/tech_word.txt", "r") as file:
            hands = file.readlines()
            random.shuffle(hands)

        royal = hands[lah]
        #print(royal)

    elif gah == "A":
        with open("DataUsername/american_culture.txt", "r") as file:
            dands = file.readlines()
            random.shuffle(dands)

        pole = dands[jah]
        #print(royal)






    #Concatenate First & Second name.     COMBINATIONS LOGIC.     6 TOTAL COMBINATIONS
    if fah == "S" and gah == "N":

        galut = flex.replace("\n","")
        galute = doom.replace("\n","")
        galutee = galut + " " + galute
        print(galutee)
        

        with open("user_name_save.txt", "a") as lofer:
            lofer.write("\n \n" + galutee)
            
        return galutee

    elif fah == "Q" and gah == "N":

        lalut = wow.replace("\n","")
        lalute = doom.replace("\n","")
        lalutee = lalut + " " + lalute
        print(lalutee)
        

        with open("user_name_save.txt", "a") as lofer:
            lofer.write("\n \n" + lalutee)
            
        return lalutee

    elif fah == "S" and gah == "W":

        salut = flex.replace("\n","")
        salute = royal.replace("\n","")
        salutee = salut + " " + salute
        print(salutee)
        

        with open("user_name_save.txt", "a") as lofer:
            lofer.write("\n \n" + salutee)
            
        return salutee

    elif fah == "Q" and gah == "A":
        lut = wow.replace("\n", "")
        lute = pole.replace("\n", "")
        lutee = lut + " " + lute
        print(lutee)
        
        with open("user_name_save.txt", "a") as lofer:
            lofer.write("\n \n" + lutee)
            
        return lutee


    elif fah == "S" and gah == "A":
        nalut = flex.replace("\n", "")
        nalute = pole.replace("\n", "")
        nalutee = nalut + " " + nalute
        print(nalutee)

        with open("user_name_save.txt", "a") as lofer:
            lofer.write("\n \n" + nalutee)

        return nalutee

    elif fah == "T" and gah == "A":
        valut = zoo.replace("\n", "")
        valute = pole.replace("\n", "")
        valutee = valut + " " + valute
        print(valutee)
       

        with open("user_name_save.txt", "a") as lofer:
            lofer.write("\n \n" + valutee)
            
        retrun valutee


    elif fah == "Q" and gah == "W":

        alut = wow.replace("\n","")
        alute = royal.replace("\n","")
        alutee = alut + " " + alute
        print(alutee)
        

        with open("user_name_save.txt", "a") as lofer:
            lofer.write("\n \n" + alutee)
            
        return alutee

    elif fah == "T" and gah == "W":

        palut = zoo.replace("\n","")
        palute = royal.replace("\n","")
        palutee = palut + " " + palute
        print(palutee)

        with open("user_name_save.txt", "a") as lofer:
            lofer.write("\n \n" + palutee)

        return palutee
    
    elif fah == "T" and gah == "N":

        qalut = zoo.replace("\n","")
        qalute = doom.replace("\n","")
        qalutee = qalut + " " + qalute
        print(qalutee)

        with open("user_name_save.txt", "a") as lofer:
            lofer.write("\n \n" + qalutee)
        return galutee


def generate_username():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    #Genarates & Save Password
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    final_password_list = ''.join(password_list)
    print("Your Password is: ",final_password_list)

    #Generate Username for Email
    password_letters = [choice(letters) for _ in range(randint(5, 10))]
    user_name = ''.join(password_letters)
    print("Your Username is: ",user_name)

    
    return final_password_list, user_name


random_gen()