from mpi4py import MPI
import sys
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if size != 2:
    if rank == 0:
        print('Need two processes.')
    sys.exit()

if rank == 0:
    dest = 1
else:
    dest = 0

data = {'rank': rank}
recvdata = comm.sendrecv(data, dest)
print('Rank', rank, 'received', recvdata)

data = np.full(100000, rank, dtype=float)
recvdata = np.empty(100000, dtype=float)

comm.Sendrecv(data, dest, recvbuf=recvdata, source=dest)
print('Rank', rank, 'received an array [', recvdata[0], '...')

# If sends/recvs are in wrong order, communication will deadlock.
# if rank == 0:
#     comm.Send(data, dest)
#     comm.Recv(recvdata, source=dest)
# else:
#     # These are in the wrong order. Both processes will try to send.
#     comm.Send(data, dest=dest)
#     comm.Recv(recvdata, source=dest)
# print('Rank', rank, 'received an array [', recvdata[0], '...')
