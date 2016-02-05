from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

#assuming 5 computers
data = []
if rank == 0:
    data = [1, 2, 3, 4, 5]
data = comm.scatter(data, root = 0)
data = data + 2
data = comm.gather(data, root = 0)
if rank == 0:
    print(data)
