# 18/03/2025

def remove_dupes(L1, L2):

    L1_Copy = L1[:] # Creating clone/copy to loop over so that the
                    # original list is not accidentally mutated.

    for e in L1_Copy:
        if e in L2:
            L1.remove(e)

L1 = [10, 20, 30, 40] # Can alias as La

L2 = [10, 20, 50, 60] # Can alias as Lb 

# Both will still be passed as parameters, no matter the alias.
# L1 will point to La, L2 will point to Lb.

remove_dupes(L1, L2)

# Solved, works.

# Below is an example of an alias (just another name referring to the same object):

def remove_dupes(L1, L2):

    L1_Copy = L1 # Because we do not make a clone here,
                 # L1_Copy still points to the original
                 # L1 object in memory. AKA an alias.

    for e in L1_Copy:
        if e in L2:
            L1.remove(e)

# Buggy code, does not work due to aliasing issues.