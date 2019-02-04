import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}
# loop through questions dictionary, 
# 'ask' each question with input() - Y or N
# new dictionary with same keys, values - bool according to above response
# return new dictionary

def askQuestions(q):
	responses = {}

	for style in q:

		question = q[style]
		response = input(question + " Y or N: ")

		if response == 'Y':
			responses[style] = True
		elif response == 'N':
			responses[style] = False
	return responses

# take preferences
# create empty list = drink
# for true preferences, append random value from ingredient dict to drink list
# return drink

def drinkGenerator(pref):
	drink = []

	for flavor in pref:
		
		ingredient = random.choice(ingredients[flavor])
		if pref[flavor] == True:
			drink.append(ingredient)

	return drink

if __name__ == '__main__':
	preferences = askQuestions(questions)
	drink = drinkGenerator(preferences)
	print(drink)