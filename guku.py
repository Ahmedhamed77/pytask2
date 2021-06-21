import numpy as np


def crossingover(p1, p2, size):
    # generating the random number to perform crossover two points
    p1_new = np.random.randint(0, size - 1)
    p2_new = np.random.randint(0, size + 1)
    print("Crossover point :", p1_new, p2_new)

    # interchanging the genes and producing new offspring
    for i in range(p1_new, p2_new):
        p1[i], p2[i] = p2[i], p1[i]

    print(p1)
    print(p2)
    return p1, p2


size = 15
generations_number = 5

# parents chromosomes:
symbols1 = ('A', 'T', 'G', 'C')
symbols2 = ('a', 't', 'g', 'c')

# random pick of the arr
p1 = np.random.choice(symbols1, size)
p2 = np.random.choice(symbols2, size)

print("Parents")
print("P1 :", p1)
print("P2 :", p2)

# function calling and storing the off springs for
# next generation crossover
for i in range(generations_number):
    print("Generation", i+1, "Childrens :")
    p1, p2 = crossingover(p1, p2, size)
