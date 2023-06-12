
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

count_letter_t = int(lower_case_name1.count("t")) + int(lower_case_name2.count("t"))
count_letter_r = int(lower_case_name1.count("r")) + int(lower_case_name2.count("r"))
count_letter_u = int(lower_case_name1.count("u")) + int(lower_case_name2.count("u"))
count_letter_e = int(lower_case_name1.count("e")) + int(lower_case_name2.count("e"))
total_count_true = count_letter_t + count_letter_r + count_letter_u + count_letter_e


count_letter_l = int(lower_case_name1.count("l")) + int(lower_case_name2.count("l"))
count_letter_o = int(lower_case_name1.count("o")) + int(lower_case_name2.count("o"))
count_letter_v = int(lower_case_name1.count("v")) + int(lower_case_name2.count("v"))
count_letter_e = int(lower_case_name1.count("e")) + int(lower_case_name2.count("e"))
total_count_love = count_letter_l + count_letter_o + count_letter_v + count_letter_e

love_score = str(total_count_true) + str(total_count_love)

if int(love_score) <=10 or int(love_score) >= 90:
    print (f"Your score is {love_score}, you go together like coke and mentos.")
elif int(love_score)>= 40 and int(love_score)<= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")