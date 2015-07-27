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
    users_pref = {}
    for quality in qualities:
        like = raw_input("Do you want your drink %r? (yes/no)   " % quality).lower()
        while like not in ["y", "yes", "n", "no"]: 
            like = raw_input("Please enter yes/no   ")
        users_pref[quality] = like in ["y", "yes"]
    return users_pref

def construct_drink (users_pref):
    drink=[]
    for quality in users_pref:
        if users_pref[quality]:
            drink.append(random.choice(ingredients[quality]))
    return drink

def drink ():
    print(construct_drink(questions()))  
    #This will first run question, than provide return to construnct drink function, than print the result

def main ():
    print"Welcome to XXXX bar. I do not want to support over consumption of alcohol. Therefor I will offer only one drink for a customer." 
    first_iteration = True 
    while True:
        if first_iteration: 
            print "Are you a customer?"
        else:
            print "Are you a new customer?"
        wants_a_drink = raw_input ("Yes/no")
        while wants_a_drink not in ["y", "yes", "n", "no"]: 
            wants_a_drink = raw_input("Please enter yes/no   ")
        if wants_a_drink in ["y", "yes"]: 
            drink ()
        else: 
            break
        first_iteration=False
    
if __name__ == '__main__':
    main()
