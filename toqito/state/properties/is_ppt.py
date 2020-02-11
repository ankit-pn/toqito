"""Determines whether or not a matrix has positive partial transpose."""
from typing import List, Union
import numpy as np

from toqito.matrix.properties.is_psd import is_psd
from toqito.super_operators.partial_transpose import partial_transpose


def is_ppt(mat: np.ndarray,
           sys: int = 2,
           dim: Union[int, List[int]] = None,
           tol: float = None) -> bool:
    """
    Determine whether or not a matrix has positive partial transpose.

    Yields either `True` or `False`, indicating that `mat` does or does not
    have positive partial transpose (within numerical error). The variable
    `mat` is assumed to act on bipartite space.

    :param mat: A square matrix.
    :param sys: Scalar or vector indicating which subsystems the transpose
                should be applied on.
    :param dim: The dimension is a vector containing the dimensions of the
                subsystems on which `mat` acts.
    :param tol: Tolerance with which to check whether `mat` is PPT.
    :return: True if `mat` is PPT and False if not.
    """
    eps = np.finfo(float).eps

    if dim is None:
        dim = np.round(np.sqrt(mat.size))
    if tol is None:
        tol = np.sqrt(eps)
    return is_psd(partial_transpose(mat, sys, dim), tol)