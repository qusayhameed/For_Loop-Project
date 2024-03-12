
# A Code to display the "*" in the required form using just a for-loop and an if-else statement
highest_stars_numbers = 5
j= highest_stars_numbers * 2
for i in range(1,j):
    if i<= highest_stars_numbers:
        print("*" * i)
    else:
        print("*" * (j-i))
