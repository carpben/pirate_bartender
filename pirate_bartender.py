#Bartender app. Creating drinks according to customers preferences.
import random

qualities=("strong", "salty", "bitter", "sweet", "fruity")
ingredients = {
    "strong": ("glug of rum", "slug of whisky", "splash of gin"),
    "salty": ("olive on a stick", "salt-dusted rim", "rasher of bacon"),
    "bitter": ("shake of bitters", "splash of tonic", "twist of lemon peel"),
    "sweet": ("sugar cube", "spoonful of honey", "spash of cola"),
    "fruity": ("slice of orange", "dash of cassis", "cherry on top")
}

def str_to_bol(ans):
    ans=ans.lower()
    while ans not in ["y", "yes", "n", "no"]:    
        ans=raw_input("Please enter yes/no.  ")
    if ans in ["y", "yes"]:
        return True
    else: 
        return False

def questions():
    users_pref = {}
    for quality in qualities:
        wanted = raw_input("Do you want your drink %r? (yes/no)   " % quality).lower()
        users_pref[quality] = str_to_bol(wanted)
    return users_pref

def construct_drink (users_pref):
    recipe=[]
    for quality in users_pref:
        if users_pref[quality]:
            recipe.append(random.choice(ingredients[quality]))
    return recipe

def drink ():
    recipe=construct_drink(questions())  
    print "One drink coming up. It includes:"
    for ingrident in recipe: 
        print "      " + ingrident

def main ():
    print"Welcome to XXXX bar. I do not want to support over consumption of alcohol. Therefore, I will offer only one drink for a customer. We shall finish working when there are no more customers to serve." 
    first_iteration = True 
    while True:
        if first_iteration: 
            deserves_a_drink = raw_input ("Are you a customer? yes/no   ")
            first_iteration=False
        else:
            deserves_a_drink = raw_input ("Are you a new customer? yes/no   ")
        deserves_a_drink = str_to_bol(deserves_a_drink)
        if not deserves_a_drink: 
            break
        wants_a_drink = raw_input("Do you want a drink? yes/no  ")
        wants_a_drink = str_to_bol(wants_a_drink)
        if wants_a_drink:
            drink()
        
if __name__ == '__main__':
    main()
