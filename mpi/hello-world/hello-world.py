from mpi4py import MPI

comm = MPI.COMM_WORLD

size = comm.Get_size()
rank = comm.Get_rank()

print('This is rank', rank, 'out of', size, 'processes.')
