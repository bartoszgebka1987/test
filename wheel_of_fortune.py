import random
import time


def loading_words():
    store = []
    f = open("storehouse.txt", "r")
    for line in f:
        store.append(line.rstrip("\n"))
    return store


def init():
    st=[]
    for i in range(0,len(r)):
        st.append('X')
    return st


r = random.choice(loading_words())
state_of_the_word=init()




def guessing(letter):
     d=0
     for i in r:
         if i == letter:
             state_of_the_word[d] = letter
             print("There is " +str(letter)+" !")
             print("You won " + str(a) + "!")
         d += 1
     print(state_of_the_word)



print("Welcome to wheel of fortune!\n")

lista_na_kole=[100,200,300,400,500,1000,2000,2500,'stop','bankrupt','bonus']

def printcircle():
    print("         " + str(lista_na_kole[0]) +  "      " + str(lista_na_kole[1]) + "      " +  str(lista_na_kole[2]))
    print("     " + str(lista_na_kole[9]) +  "                    " +  str(lista_na_kole[4]))
    print("   " + str(lista_na_kole[5]) +  "                            " +  str(lista_na_kole[10]))
    print("      " + str(lista_na_kole[6]) +  "                      " +  str(lista_na_kole[7]))
    print("           " + str(lista_na_kole[3]) + "  " + str(lista_na_kole[8]) +  "  " + str(lista_na_kole[4]) + "  " +  str(lista_na_kole[5]))

#Lets start the game

printcircle()
print("Lets start the game!")
print("Wheel is running...")

time.sleep(10)

a=str(random.choice(lista_na_kole))

if   a == "stop":
    print("You lost your turn!")
    quit()

elif a == "bankrupt":
    print("Unfortunately you lost all money!")
    quit()
elif a == "bonus":
    print("You won additional 10000zl!")
else:
    print("Wheel shows " + str(a) +" for each letter!")


while r != ''.join(state_of_the_word):
    letter=input("Guess one letter: ")
    guessing(letter)




