#Bartender app. Creating a drink according to users preference.
import random

qualities=("strong", "salty", "bitter", "sweet", "fruity")
ingredients = {
    "strong": ("glug of rum", "slug of whisky", "splash of gin"),
    "salty": ("olive on a stick", "salt-dusted rim", "rasher of bacon"),
    "bitter": ("shake of bitters", "splash of tonic", "twist of lemon peel"),
    "sweet": ("sugar cube", "spoonful of honey", "spash of cola"),
    "fruity": ("slice of orange", "dash of cassis", "cherry on top")
}

def questions():
    users_pref = {
        "strong": False,
        "salty": False,
        "bitter": False,
        "sweet": False,
        "fruity": False
    }
    for quality in qualities:
        while True: 
            like=raw_input ("Do you like your drink {}? (yes/no)".format(quality))
            if like =="yes" or like == "no":  
                if like == "yes":
                    users_pref[quality]=True
                break
            else: 
                print "Please enter yes/no." 
    return users_pref

def construct_drink (users_pref):
    drink=[]
    for quality in users_pref:
        if users_pref[quality]==True:
            drink.append(random.choice(ingredients[quality]))
    return drink

def main ():
    print(construct_drink(questions()))  
    #This will first run question, than provide return to construnct drink function, than print the result
    
if __name__ == '__main__':
    main()
