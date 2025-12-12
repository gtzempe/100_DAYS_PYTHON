print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0
small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepperoni_small = 2
pepperoni_medium_or_large = 3
extra_cheese_any_size = 1


if size == "S" or size == "s":
    bill = small_pizza
elif size == "M" or size == "m":
    bill = medium_pizza
elif size == "L" or size == "l":
    bill = large_pizza
else:
    print("Sorry you have to enter S, M, or L.")


if pepperoni == "Y" or pepperoni == "y":
    if size == "S" or size == "s":
        bill = bill + pepperoni_small
    else:
        bill = bill + pepperoni_medium_or_large


if extra_cheese == "Y" or extra_cheese == "y":
   bill += extra_cheese_any_size

print(f"Your final bill is: ${bill}.")

