#Tamagotchi game
import random
class Tama(object):
    number=0
    def __init__(self,name,hunger,boredom,age,weight):
        self.name=name
        self.hunger=hunger
        self.boredom=boredom
        self.age=age
        self.weight=weight+random.randrange(10)/10
        print("\n",name," has been born!")
        Tama.number+=1

    #time passing
    def time(self):
        self.hunger+=1
        self.boredom+=1
        self.age+=0.5
        weight+=0.1*(random.randrange(10)-5)

    #feed the animal
    def eat(self):
        print("How much food would you like to give",self.name,"?")
        b=input("\n Please enter 1, 2 or 3.")
        a_invalid=True
        while a_invalid==True:
            try:
                a=int(b)
            except ValueError:
                a=0
            else:
                if a==1 or a==2 or a==3:
                    a_invalid=False
                    break
            print("\nSorry, ",b," isn't a reasonable amount of food!")
            b=input("\n Please enter 1, 2 or 3.")
        self.hunger-=a
        self.weight+=2.5*a
        if self.hunger<0:
            self.hunger=0
        print("\n",self.name," says, 'Yum yum! I enjoyed that food!",
              "\n Now my hunger level is ",self.hunger,".'")

    #play with the animal
    def play(self):
        print("\nHow much fun will your game with ",self.name," be?")
        b=input("\n Please enter 1, 2 or 3.")
        a_invalid=True
        while a_invalid==True:
            try:
                a=int(b)
            except ValueError:
                a=0
            else:
                if a==1 or a==2 or a==3:
                    a_invalid=False
                    break
            print("\nSorry, ",b," isn't a reasonable amount of fun!")
            b=input("\n Please enter 1, 2 or 3.")
        self.boredom-=a
        if self.boredom<0:
            self.boredom=0
        print("\n",self.name," says, 'Woooo! I, enjoyed that game!",
              "\n Now my boredom level is ",self.boredom,".'")

    #define mood
    def mood(self):
        if self.hunger+self.boredom<5:
            mood="happy"
        elif self.hunger+self.boredom<8:
            mood="a bit grumpy"
        elif self.hunger+self.boredom<11:
            mood="angry"
        else:
            mood="FURIOUS"
        return mood

    #Saying its mood
    #Also says its age and weight
    def talk(self):
        print("\n",self.name," is ",self.age," years old,",
              "\n",self.name," weights ",self.weight," kilos,",
              "\nand ",self.name," says, 'I am feeling ",self.mood(),".'")

    #checking whether it's dead
    def is_dead(self):
        if self.weight<=0:
            print("\nOh no! ",self.name," has wasted away and has died!")
            return True
        elif self.hunger>11:
            print("\nOh no! ",self.name," has died of starvation!")
            return True
        elif self.boredom>11:
            print("\nOh no! ",self.name," has died of boredom!")
            return True
        else:
            return False

    #checking whether it's 18
    def is_adult(self):
        if self.age==18:
            print("\nCongratulations! ",self.name," has reached the age of 18 alive.",
                  "\nYou no longer need to look after ",self.name,".")

#main menu function
def menu():
    if Tama.number-number_dead-number_adults==0:
        if number_dead==0 and number_adults==0:
            print("\nHello Colin! Welcome to the children game!",
              "\n\n Since you don't have any real children, you can have up to 3 children.")
        elif number_adults==0:
            print("\nColin, you have no children left because you have killed them all.\n\nYou lose.")
            return 5
        else:
            print("\nWell done Colin, your children all grew up!")
        c=input("\n\n Press 1 to create a child or 2 to quit.")
        c_invalid=True
        while c_invalid:
            try:
                choice=int(c)
            except ValueError:
                choice=None
            else:
                if choice==1 or choice==2:
                    choice+=3
                    return choice
            c=input("\nYou must enter either 1 or 2.")
    elif Tama.number-number_dead-number_adults==1 or Tama.number-number_dead-number_adults==2:
        print("\nWhat would you like to do?",
              "\n\n Press 1 to find out how your children are feeling.",
              "\n Press 2 to feed a child.",
              "\n Press 3 to play with a child.",
              "\n Press 4 to create a new child.",
              "\n Press 5 to quit.")
        choice = input("Your choice: ")
        return choice
    elif Tama.number-number_dead-number_adults==3:
        print("\nYou now have the maximum number of children. \n\nWhat would you like to do?",
              "\n\n Press 1 to find out how your children are feeling.",
              "\n Press 2 to feed a child.",
              "\n Press 3 to play with a child.",
              "\n Press 5 to quit.")
        choice = input("Your choice: ")
        return choice
    else:
        print("Sorry, something appears to have gone wrong when asked to display the menu")

#create function
def create():
    N=input("What is the new child's name?")
    if Tama.number==0:
        pet1=Tama(name=N)
    elif Tama.number==1:
        pet2=Tama(name=N)
    elif Tama.number==2:
        pet3=Tama(name=N)

#feed function
def feed():
    P_invalid=True
    P=input("Which child would you like to feed? ")
    while P_invalid:
        if Tama.number==1:
            if pet1.name==P:
                pet1.eat()
                P_invalid=False
                break
        elif Tama.number==2:
            if pet1.name==P:
                pet1.eat()
                P_invalid=False
                break
            elif pet2.name==P:
                pet2.eat()
                P_invalid=False
                break
        elif Tama.number==3:
            if pet1.name==P:
                pet1.eat()
                P_invalid=False
                break
            elif pet2.name==P:
                pet2.eat()
                P_invalid=False
                break
            elif pet3.name==P:
                pet3.eat()
                P_invalid=False
                break
        print("You don't have a child called ",P,".\n\n")
        P=input("Enter the name of the child you would like to feed.")
    #then make time pass
    pet1.time()
    if Tama.number>=2:
        pet2.time()
    if Tama.number==3:
        pet3.time()

#play function
def user_play():
    if Tama.number==1:
        pet1.play()
        #this time the coding is more efficient with number of pets already coded for
        pet1.time()
    elif Tama.number==2:
        P=input("Which child would you like to play with?")
        while pet1.name!=P and pet2.name!=P:
            print("You don't have a child with that name.\n\n")
            P=input("Enter the name of the child you would like to play with.")
        if pet1.name==P:
            pet1.play()
        else:
            pet2.play()
        pet1.time()
        pet2.time()
    elif Tama.number==3:
        P=input("Which child would you like to play with?")
        while pet1.name!=P and pet2.name!=P and pet3.name!=P:
            print("You don't have a child with that name.\n\n")
            P=input("Enter the name of the child you would like to play with.")
        if pet1.name==P:
            pet1.play()
        elif pet2.name==P:
            pet2.play()
        else:
            pet3.play()
        pet1.time()
        pet2.time()
        pet3.time()
    else:
        print("There has been a problem. You probably have too many children.")
    

#listen
def listen():
    print("Listening...")
    pet1.talk()
    if Tama.number-number_dead-number_adults>=2:
        pet2.talk()
    if Tama.number-number_dead-number_adults==3:
        pet3.talk()

#check if they're dead or 18 and update the number of dead or 18 year old children
#DOESN'T WORK
def status():
    d=0
    a=0
    if Tama.number-number_dead-number_adults==3:
        print(3)
        #remove pet3 if it's grown up or dead
        if pet3.is_dead():
            d+=1
            pet3=None
        elif pet3.is_adult():
            a+=1
            pet3=None
        if pet2.is_dead():
            d+=1
            #if pet2 has died we need to change the names of the other pets
            if pet3:
                pet2=pet3
                pet3=None
            else:
                pet2=None
        elif pet2.is_adult():
            a+=1
            if pet3:
                pet2=pet3
                pet3=None
            else:
                pet2=None
        if pet1.is_dead():
            d+=1
            if pet3:
                pet1=pet2
                pet2=pet3
                pet3=None
            elif pet2:
                pet1=pet2
                pet2=None
            else:
                pet1=None
        if pet1.is_adult():
            a+=1
            if pet3:
                pet1=pet2
                pet2=pet3
                pet3=None
            elif pet2:
                pet1=pet2
                pet2=None
            else:
                pet1=None
    elif Tama.number-number_dead-number_adults==2:
        print(2)
        if pet2.is_dead():
            d+=1
            pet2=None
        elif pet2.is_adult():
            a+=1
            pet2=None
        if pet1.is_dead():
            d+=1
            if pet2:
                pet1=pet2
                pet2=None
            else:
                pet1=None
        if pet1.is_adult():
            a+=1
            if pet2:
                pet1=pet2
                pet2=None
            else:
                pet1=None
    elif Tama.number-number_dead-number_adults==1:
        #print 1 is so I could check that this is where the problem it
        print(1)
        #it sayd local variable pet1 referenced before assignment
        #but putting pet1.talk() into the menu function just before this function
        #is called doesn't result in an error
        pet1.talk()
        if pet1.is_dead():
            d+=1
            pet1=None
        elif pet1.is_adult()==True:
            a+=1
            pet1=None
    return(a,d)
        



#main
number_dead=0
number_adults=0
k=None
k_invalid=True
while k!=5:
    while k_invalid:
        #this was to make the error message come up even if they enter a non integer
        #but it then complicated the code later
        #so then I took out the bit where k_invalid is made false
        #so it's an infinite loop really
        try:
            k=int(menu())
        except ValueError:
            k=None
        else:
            if k==1 or k==2 or k==3 or k==4 or k==5:
                break
            else:
                print("That was not a valid choice.\n")
                k=input("Please try again. ")
    if k==1:
        listen()
    elif k==2:
        feed()
    elif k==3:
        user_play()
    elif k==4:
        N=input("\nWhat is the new child's name? ")
        if Tama.number-number_dead-number_adults==0:
            pet1=Tama(name=N,hunger=0,boredom=0,weight=0,age=0)
        elif Tama.number-number_dead-number_adults==1:
            pet1.time()
            pet2=Tama(name=N,hunger=0,boredom=0)
        elif Tama.number-number_dead-number_adults==2:
            pet1.time()
            pet2.time()
            pet3=Tama(name=N,hunger=0, boredom=0)
    (a,d)=status()
    number_dead+=d
    number_adults+=a
input("\nGoodbye Colin!\n\nPress the enter key to exit.")
