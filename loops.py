# Example loop
# for i in range(1, 21, 2):
#     print(i, end=' ')
# print()

# a.
# for i in range(0, 110, 10):
#     print(i, end=' ')
# print()

# b.
# for i in range(20, 0, -1):
#     print(i, end=' ')
# print()

# c.
# amount_of_stars = int(input("Number of stars: "))
# for i in range(amount_of_stars):
#     print('*', end='')
# print()

# d.
amount_of_stars = int(input("Number of stars: "))
for i in range(amount_of_stars):
    for c in range(i + 1):
        print('*', end='')
    print()