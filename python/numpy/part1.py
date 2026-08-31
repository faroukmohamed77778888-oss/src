import numpy as np

def array_factory(mode, shape, value=None):

    if mode == "zeros":
        return np.zeros(shape)

    elif mode == "ones":
        return np.ones(shape)

    elif mode == "full":
        return np.full(shape, value)

    elif mode == "identity":
        return np.eye(shape)

    else:
        return "Invalid mode"


print(array_factory("zeros", (2, 3)))
print(array_factory("ones", (2, 3)))
print(array_factory("full", (2, 3), 5))
print(array_factory("identity", 3))