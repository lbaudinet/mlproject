from math import radians, cos, sin, asin, sqrt
from mlproject.tools import haversine
import pytest

def test_haversine():
    lon1, lat1, lon2, lat2 = map(radians, [48.865, 2.380, 48.235, 2.393])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    assert c * r == 70.00696965697475
