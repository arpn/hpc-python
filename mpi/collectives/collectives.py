from mpi4py import MPI
import numpy as np
from sys import stdout

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

assert size == 4, 'Number of tasks has to be 4.'

data = np.full(8, 0)
if rank == 0:
    data = np.arange(8)

# Broadcast from rank 0 to everyone
comm.Bcast(data, root=0)

print('Rank', rank, ': data =', data)

stdout.flush()
comm.barrier()
# First part done, now data vectors are
data = np.arange(rank*8, (rank+1)*8)
print('Rank', rank, ': data =', data)
recv = np.full(8, -1)

stdout.flush()
comm.barrier()
if rank == 0:
    print('CASE 1:')
comm.Scatter(data, recv[:2], root=0)
print('Rank', rank, ': recv =', recv)

stdout.flush()
comm.barrier()
if rank == 0:
    print('CASE 2:')
recv = np.full(8, -1)
comm.Gather(data[:2], recv, root=1)
print('Rank', rank, ': recv =', recv)

stdout.flush()
comm.barrier()
if rank == 0:
    print('CASE 3:')
recv = np.full(8, -1)
# This can be done by summing ranks 0 and 1 to
# the recv buffer of 0, and similarly for ranks 2 and 3.
local_comm = comm.Split(rank // 2)
local_comm.Reduce(data, recv, op=MPI.SUM, root=0)
print('Rank', rank, ': recv =', recv)
