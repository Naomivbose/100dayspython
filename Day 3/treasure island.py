print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

task_1 = input("You arrive on the beach of the island. Where do you want to go? Left or Right").lower()

if task_1 == "left":
    task_2 = input ("You walk into a tropical forest. A monkey wants you to follow him. What do you do? Follow or alone").lower()
    if task_2 == "follow":
        task_3 = input ("The monkey bring you to a sign which says treasure. What will you use to dig it up? Hands or Rock ").lower()
        if task_3 == "hands":
            print("You found the treasure! You win!!")
        else:
            print("A poisinous spider was under the rock. It attacks you. Game Over")
    else:
        print("You get lost in the forest and slowley die of heath and dehydration")
else:
    print("You fall in a sinkhole. Game Over!")