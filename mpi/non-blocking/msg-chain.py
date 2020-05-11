from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n_data = 100000
data = np.full(n_data, rank, dtype=int)
recv_data = np.empty(n_data, dtype=int)

# A simpler version?
dst = rank + 1
src = rank - 1
if rank == 0:
    src = MPI.PROC_NULL
elif rank == size - 1:
    dst = MPI.PROC_NULL

recv_rq, send_rq = None, None
if rank > 0:
    recv_rq = comm.Irecv(recv_data, source=rank-1)
if rank < size - 1:
    send_rq = comm.Isend(data, dest=rank+1)

# Wait for communication to finish
MPI.Request.Waitall([rq for rq in [recv_rq, send_rq] if rq is not None])

if rank > 0:
    print('Rank', rank, 'received an array [', recv_data[0], '...')
if rank < size - 1:
    print('Rank', rank, 'sends', n_data, 'integers.')
