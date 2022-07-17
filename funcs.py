import numpy as np

def indicator_func(x, X, W=None):
    if isinstance(W, type(None)):
        W = np.ones(len(X))
    assert len(X) == len(W), 'X and W must have the same length'
    xx, XX = np.meshgrid(x, X)
    return np.heaviside(xx-XX, 1)

def emp_dist_func(x, X):
    """Empirical distribution function"""
    return np.mean(indicator_func(x,X), axis=0)
 