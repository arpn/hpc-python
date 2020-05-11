from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n_data = 100000
data = np.full(n_data, rank, dtype=int)
recv_data = np.empty(n_data, dtype=int)

# if rank < size-1:
#     comm.Send(data, rank+1)
#     print('Rank', rank, 'sends', n_data, 'integers.')
# 
# if rank > 0:
#     comm.Recv(recv_data, rank-1)
#     print('Rank', rank, 'received an array [', recv_data[0], '...')

# A simpler version?
dst = rank + 1
src = rank - 1
if rank == 0:
    src = MPI.PROC_NULL
elif rank == size - 1:
    dst = MPI.PROC_NULL
comm.Sendrecv(data, dst, recvbuf=recv_data, source=src)
if rank > 0:
    print('Rank', rank, 'received an array [', recv_data[0], '...')
if rank < size - 1:
    print('Rank', rank, 'sends', n_data, 'integers.')