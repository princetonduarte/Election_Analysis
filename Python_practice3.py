# x = 0
# while x <= 5:
#     print(x)
#     x = x + 1

my_votes = int(input("How many votes did you get in the election? "))

total_votes = int(input("What is the total votes in the election? "))

percentage_votes = (my_votes / total_votes) * 100

print(f"I received {my_votes / total_votes * 100}% of the total votes.")
