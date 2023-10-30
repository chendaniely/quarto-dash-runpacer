from conversions import m2k, k2m, km_mile_distances


def test_m2k():
    assert round(m2k(3.1), 1) == 5
    assert round(m2k(3.1), 1) != 10


def test_k2m():
    assert round(k2m(10), 1) == 6.2
    assert round(k2m(10), 1) != 3


def test_km_mile_distances():
    expected = {"mi": 3.1, "km": 5}
    calculated = km_mile_distances(3.1, "mi")
    assert calculated == expected
