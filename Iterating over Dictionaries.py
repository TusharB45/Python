prices = {
    "box_of_spaghetti" : 4,
    "lasagna"  : 5,
    "hamburger" : 2
   }
quantity = {
    "box_of_spaghetti" : 6,
    "lasagna"  : 10,
    "hamburger" : 0
    }

money_spent = 0

for i in quantity:
    if prices[i]>=5:
        money_spent += prices[i]*quantity[i] 
    else:
        money_spent = money_spent

print (money_spent)
