#given code
user_funds = 10.31
item_price = { "Burger" : 6.50 }


if item_price["Burger"] < user_funds:
    print("You have enough money!") #changed P to lowercase in print
if item_price["Burger"] == user_funds:
    print("You have the precise amount of money")
if item_price["Burger"] > user_funds: #changed < to >
    print("Sorry you don't have enough money") #added quotation marks