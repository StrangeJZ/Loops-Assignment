def shop_menu():
    print("Welcome to Taco Stop. Here is our lovely menu.")
    print(" 1. Taco - $4.00 \n 2. Burrito - $5.00 \n 3. Nachos - $3.00 \n 4. Soft Drink - $1.00 \n 5. Checkout")
shop_menu()
items_selected = []
item = int(input("Please select an item: "))
if item == 1:
    print("You have selected a taco")
    items_selected.append(4)
elif item == 2:
    print("you have selected a Burrito")
    items_selected.append(5)
elif item == 3:
    print("You have selected Nachos")
    items_selected.append(3)
elif item == 4:
    print("You have selected a Soft Drink")
    items_selected.append(1)
while item < 5:
   item = int(input("Please select another item: "))
   if item == 1:
       items_selected.append(4)
       print("You have selected a Taco")
   elif item == 2:
       items_selected.append(5)
       print("You have selected a Burrito")
   elif item == 3:
       items_selected.append(3)
       print("You have selected Nachos")
   elif item == 4:
       items_selected.append(1)
       print("You have selected a Soft drink")
   elif item == 5:
       print("Your amount due is $", sum(items_selected))

