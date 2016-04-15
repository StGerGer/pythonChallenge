import pickle

file = open("banner.p", 'rb')

unpickled = pickle.load(file)

for x in unpickled:
    for u in x:
        if "#" in u:
            print(u)

for x in unpickled:
    for u in x:
        if "#" not in u:
            print(u)