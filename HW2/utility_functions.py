# this module defines some utility functions for the course

def Newmark(M,C,K,f,t,u0,gamma=0.5,beta=0.25,v0=None) :
    """Newmark time integration
    
    Implements the Newmark-method to integrate 
    M*x''+C*x'+K*x = f(t)
    using the initial values x(t=0) = u0
    
    Parameters
    ----------
    M : array(N,N) or csc_matrix(N,N)
        mass matrix
    C : array(N,N) or csc_matrix(N,N)
        damping matrix
    K : array(N,N) or csc_matrix(N,N)
        stiffness matrix
    f : array(N,T) or csc_matrix(N,T)
        forcing vector, rows correspond to dgerees of freedom
        and columns to time poitns
    t : array(T,)
        time vector with T elements, must be equally spaced
    u0: array(N,)
        initial condition vector 
        
    Returns
    -------
    u : array(N,T)
        integrated solution, u[:,i] is the soluion vector for t[i],
        i.e. x(t_i)
    v : array(N,T)
        integrated velovity, v[:,i] is the velocity vector for t[i],
        i.e. x'(t_i)
    a : array(N,T)
        integrated acceleration a[:,i] is the acceleration vector for t[i],
        i.e. x''(t_i)
    """
    from numpy import diff, unique, round, zeros, zeros_like, squeeze, array
    from scipy.sparse import csc_matrix
    from scipy.sparse.linalg import factorized
    dt = unique(round(diff(t),12))
    if len(dt) > 1 :
        print('time vector must be equally spaced')
    else :
        dt = dt[0]
    # compute necessary parameters
    a0 = 1./(beta*dt**2)
    a1 = gamma/(beta*dt)
    a2 = 1./(beta*dt)
    a3 = 1./(2.*beta) - 1.
    a4 = gamma/beta - 1.
    a5 = dt/2.*(gamma/beta - 2.0)
    a6 = dt*(1.0-gamma)
    a7 = gamma*dt
    
    # convert to sparse
    K = csc_matrix(K)
    M = csc_matrix(M)
    C = csc_matrix(C)

    # compute the factorisation
    Kn = K + a0*M + a1*C # effective system matrix
    solve_step = factorized(Kn)
    
    # initialize
    ut = u0 # initial position
    if v0 is None :
        vt = zeros_like(ut) # initial velocity
    at = zeros_like(ut) # initial acceleration

    # check matrix sizes
    def isSquare(A,N=None) :
        s = A.shape
        if s[0]==s[1]:
            return s[0]
            if N is not None :
                if s[0]==N :
                    return True
                else :
                    print('wrong size: %i != %i'%(s[0],N))
                    return False
        else :
            print('not square with shape',s)
            return 0
    N = isSquare(M)
    isSquare(C,N)
    isSquare(K,N)
    # check vector sizes
    if not f.shape[0]==N and f.shape[1]==len(t) :
        print('shape of f must be [N, len(t)] with N=K.shape[0]')
    if not len(u0.shape)==1:
        print('u0 must be a vector!')
    else :
        if not len(u0) == N :
            print('len(u0) must be = %i (N=K.shape[0])'%N)
    
    # preallocate result
    u = zeros([N,len(t)])
    v = zeros_like(u)
    a = zeros_like(u)

    # do the time integration
    for i in range(len(t)) :
        # compute effective forcing vector
        ft = squeeze(array(f[:,i])) # forcing vector: extract column, convert to vector
        ft1 = ft + M.dot(a0*ut + a2*vt + a3*at) + C.dot(a1*ut + a4*vt + a5*at )
        # solve for u at t+dt using the pre-factorized matrix
        ut1 = solve_step(ft1)
        # update v & a
        at1 = a0*(ut1-ut) - a2*vt - a3*at
        vt1 = vt + a6*at + a7*at1
        # save and prepare next step
        u[:,i] = ut1
        v[:,i] = vt1
        a[:,i] = at1
        ut = ut1
        vt = vt1
        at = at1
    return u,v,a

def nullspace(B, atol=1e-13, rtol=0):
    """Compute an approximate basis for the nullspace of B.

    The algorithm used by this function is based on the singular value
    decomposition of `B`.

    Parameters
    ----------
    B : ndarray
        A should be at most 2-D.  A 1-D array with length k will be treated
        as a 2-D with shape (1, k)
    atol : float
        The absolute tolerance for a zero singular value.  Singular values
        smaller than `atol` are considered to be zero.
    rtol : float
        The relative tolerance.  Singular values less than rtol*smax are
        considered to be zero, where smax is the largest singular value.

    If both `atol` and `rtol` are positive, the combined tolerance is the
    maximum of the two; that is::
        tol = max(atol, rtol * smax)
    Singular values smaller than `tol` are considered to be zero.

    Return value
    ------------
    Q : ndarray
        If `B` is an array with shape (m, k), then `ns` will be an array
        with shape (k, n), where n is the estimated dimension of the
        nullspace of `B`.  The columns of `Q` are a basis for the
        nullspace; each element in numpy.dot(B, Q) will be approximately
        zero.

    Referencens
    -----------
    Implementation from [scipy-cookbook](http://scipy-cookbook.readthedocs.io/items/RankNullspace.html)
    """
    from numpy import atleast_2d
    from numpy.linalg import svd
    A = atleast_2d(B)
    u, s, vh = svd(A)
    tol = max(atol, rtol * s[0])
    nnz = (s >= tol).sum()
    Q = vh[nnz:].conj().T
    return Q
