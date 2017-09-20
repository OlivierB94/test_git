import random

quotes = ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau �tre ou ne pas �tre, nous sommes !", "On doit pouvoir choisir entre s'�couter parler et se faire entendre."] 
characters = ["Alvin", "Chipmunks", "Babar", "Betty Boop", "Calimero", "Casper", "Le Chat", "Kirikou"]

def get_random_item(object_list):
    rand_numb = random.randint(0, len(object_list) - 1)
    item = object_list[rand_numb] # get a quote from a list
    return item # return the item

def capitalize(words):
    for word in words: 
        return word.capitalize()

def message(character, quote):
    capitalize(character)
    capitalize(quote)
    return "{} a dit : {}".format(character, quote)

user_answer = input('Tapez entr�e pour conna�tre une autre citation ou B pour quitter le programme.')

while user_answer != "B":
    print(message(get_random_item(characters), get_random_item(quotes)))
user_answer = input('Tapez entr�e pour conna�tre une autre citation ou B pour quitter le programme.')