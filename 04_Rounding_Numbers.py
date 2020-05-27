#Display output using int/float

to_round = [1/1, 1/2, 1/3]

print("Numbers to round:")
print(to_round)

print()
print("Rounded numbers:")

for i in to_round:
    if i%1 == 0:
        print("{:.0f}".format(i))
    else:
        print("{:.1f}".format(i))
        