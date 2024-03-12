
# A Code to display the "*" in the required form using just a for-loop and an if-else statement
highest_stars_numbers = 5
j= highest_stars_numbers * 2
"""Create a for loop from 1 and make the end of the loop is the \ 
   double of the highest numbers of stars required"""
for i in range(1,j):
    if i<= highest_stars_numbers:
        print("*" * i)
    else:
        print("*" * (j-i))
