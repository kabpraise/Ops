import pickle

pickle_in_file = open("ex_dict.pickle", "rb")
ex_dict = pickle.load(pickle_in_file)
print(ex_dict)
