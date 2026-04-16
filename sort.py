"""Package stack classification for the technical screen challenge."""

from __future__ import annotations

import math
from numbers import Real
from typing import Literal

StackName = Literal["STANDARD", "SPECIAL", "REJECTED"]


def _is_valid_number(value: object) -> bool:
    return isinstance(value, Real) and not isinstance(value, bool) and math.isfinite(float(value))


def sort(width: float, height: float, length: float, mass: float) -> StackName:
    """Return the target stack name based on package dimensions and mass.

    Args:
        width: Package width in centimeters.
        height: Package height in centimeters.
        length: Package length in centimeters.
        mass: Package mass in kilograms.
    """
    values = (width, height, length, mass)

    if not all(_is_valid_number(v) for v in values):
        raise TypeError("All dimensions and mass must be finite numbers")

    if any(v < 0 for v in values):
        raise ValueError("All dimensions and mass must be non-negative")

    volume = width * height * length
    is_bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    if is_bulky or is_heavy:
        return "SPECIAL"
    return "STANDARD"
