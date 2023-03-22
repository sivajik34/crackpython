from itertools import chain
gen_1 = range(0, 5, 2)               # 0.. 2.. 4
gen_2 = (i**2 for i in range(3, 6))  # 9.. 16.. 25
iter_3 = ["moo", "cow"]
iter_4 = "him"
print(list(chain(gen_1,gen_2,iter_3,iter_4)))

print(list(chain('ABC','DEF','GHI')))
