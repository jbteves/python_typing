"""Mathemagical functions to help mathemagicians."""

from beartype import beartype
import numpy as np
from nptyping import NDArray, Shape, Float


# Affine matrix voxel-to-world mapping (and other more common graphics uses)
AffineMatrix = NDArray[Shape["4, 4"], Float]


@beartype
def default_affine() -> AffineMatrix:
    """Get the default affine, where one voxel = one world."""
    return np.asarray(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0],
        ],
        dtype=Float
    )

@beartype
def spooky_math(x: Float) -> Float:
    return default_affine()
