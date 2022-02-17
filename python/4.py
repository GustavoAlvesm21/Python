from random import seed
from random import choice
# seed random number generator
seed(1)
# prepare a sequence
sequence = [i for i in range(25)]
print(sequence)
# make choices from the sequence
for _ in range(15):
	selection = choice(sequence)
	print(selection)