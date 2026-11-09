students = int(input("Students: "))

total = 0
highest = 0

for i in range(students):
    score = int(input("Score: "))

    total += score

    if score > highest:
        highest = score

average = total / students

print("Total:", total)
print("Average: {:.2f}".format(average))
print("Highest:", highest)
