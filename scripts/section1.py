#!/usr/bin/env python3

# add import and helper functions here
import numpy as np

if __name__ == "__main__":
    # code goes here
    np.random.seed(42)
    A = np.random.normal(size=(4, 4))
    B = np.random.normal(size=(4, 2))
    print(A@B)

    np.random.seed(42)
    x = np.random.normal(size=(4,10))
    print(x)

    sq_norms = np.sum(np.square(x), axis=1, keepdims=True)
    print(sq_norms.shape)

    D = sq_norms + sq_norms.T - 2*(x@x.T)
    print(D)