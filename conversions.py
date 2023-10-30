from collections import namedtuple


def m2k(miles):
    """Convert miles to kilometers."""
    return miles * 1.60934


def k2m(kilometers):
    """Convert kilometers to miles."""
    return kilometers * 0.621371


def km_mile_distances(distance, unit, round_digits=1):
    """Return a dictionary of distances in miles and kilometers.

    unit: a string, either 'km' for kilometers or 'mi' for miles
    """

    if unit == "mi":
        distance_mi = distance
        distance_km = m2k(distance)
    elif unit == "km":
        distance_mi = k2m(distance)
        distance_km = distance
    else:
        raise ValueError('unit must be either "km" or "mi"')

    return {
        "mi": round(distance_mi, round_digits),
        "km": round(distance_km, round_digits),
    }
