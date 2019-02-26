import pickle

ex_dict = {"kabin":"XYZ","Siz":"ABC","Santosh":"PQR"}

pickle_out_file = open("ex_dict.pickle","wb")
pickle.dump(ex_dict, pickle_out_file)
pickle_out_file.close()
