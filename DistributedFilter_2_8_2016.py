# A program that will take a list of UNSPECIFIED length and 
# UNSPECIFIED number of processes and filter it based off 
# of some function. Basically make a distributed program 
# that works like Python's filter.

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

def filter_func(x): #this is the filter function to be changed
	if (x != 3):
		return True
	else:
		return False


data = []
if rank == 0:
    data = [1, 2, 3, 4, 5] #this is the data list to be changed
rec = comm.scatter(data, root = 0)
if (filter_func(rec)):
	rec = True
else:
	rec = False
results = comm.gather(rec, root = 0)
if rank == 0:
	final = []
	i = 0
	while i < len(results):
		if results[i]:
			final += [data[i]]
		i += 1
	print(final)
