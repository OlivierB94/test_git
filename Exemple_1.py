quotes = ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", "On doit pouvoir choisir entre s'écouter parler et se faire entendre."] 
characters = ["Alvin", "Chipmunks", "Babar", "Betty Boop", "Calimero", "Casper", "Le Chat", "Kirikou"]

def show_random_item(my_list):
    # get a random number
    item = my_list[0] # get a quote from a list
    return item # return the item

user_answer = "A"

while user_answer != "B":
    print(show_random_item(quotes))
	user_answer = "B"