import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import cython
cimport numpy as cnp


matplotlib.use('Agg')

# Set the colormap
plt.rcParams['image.cmap'] = 'BrBG'


# According to cProfile, the vast majority of time
# is spent here, so we'll only optimize 'evolve'
# Results: initial runtime is around ~22s
#          cdefing everything dropped runtime to ~0.05s
#          turning off bounds checking and wraparound didn't do much
#          for overall runtime since 'evolve' is so fast already
@cython.boundscheck(False)
@cython.wraparound(False)
cdef evolve(cnp.ndarray[cnp.double_t, ndim=2] u,
            cnp.ndarray[cnp.double_t, ndim=2] u_previous,
            double a,
            double dt,
            double dx2,
            double dy2):
    """Explicit time evolution.
       u:            new temperature field
       u_previous:   previous field
       a:            diffusion constant
       dt:           time step. """

    cdef int n = u.shape[0]
    cdef int m = u.shape[1]

    cdef int i, j

    for i in range(1, n-1):
        for j in range(1, m-1):
            u[i, j] = u_previous[i, j] + a * dt * (
                (u_previous[i+1, j] - 2*u_previous[i, j] +
                 u_previous[i-1, j]) / dx2 +
                (u_previous[i, j+1] - 2*u_previous[i, j] +
                 u_previous[i, j-1]) / dy2)
    u_previous[:] = u[:]


def iterate(field, field0, a, dx, dy, timesteps, image_interval):
    """Run fixed number of time steps of heat equation"""

    dx2 = dx**2
    dy2 = dy**2

    # For stability, this is the largest interval possible
    # for the size of the time-step:
    dt = dx2*dy2 / (2*a*(dx2+dy2))

    for m in range(1, timesteps+1):
        evolve(field, field0, a, dt, dx2, dy2)
        if m % image_interval == 0:
            write_field(field, m)


def init_fields(filename):
    # Read the initial temperature field from file
    field = np.loadtxt(filename)
    field0 = field.copy()  # Array for field of previous time step
    return field, field0


def write_field(field, step):
    plt.gca().clear()
    plt.imshow(field)
    plt.axis('off')
    plt.savefig('heat_{0:03d}.png'.format(step))

