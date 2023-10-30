import re


def parse_distance_text(distance_string):
    """Parse a distance string into a number and a unit.

    The distance portion of the string can be 'm' (meters), 'km' (kilometers),
    'mi' (miles), 'half' (half marathon), or 'marathon' (marathon).
    the 'half' and 'marathon' do not need a numeric component,
    these strings are their for you as a convenience
    """

    # remove all whitespace and convert to lowercase
    whitespace_pattern = re.compile(r"\s+")
    distance_string_clean = re.sub(
        whitespace_pattern, "", distance_string
    ).lower()

    number = None
    unit = None

    # https://docs.python.org/3/library/re.html#re.Match.group
    # match on group with label 'number'
    try:
      number_pattern = re.compile(r"(?P<number>\d*\.?\d*)")
      number_match = re.match(number_pattern, distance_string_clean)
      number = number_match.group("number")
      number = float(number)
    except ValueError:
      # when the value is only a string, there is no number
      number = None

    unit_pattern = re.compile(r"[a-zA-Z]+")
    unit = re.findall(unit_pattern, distance_string_clean)
    assert len(unit) == 1, "Expected exactly one unit in distance string"
    unit = str(unit[0])

    # convert meters to km
    if unit == "m":
        unit = "km"
        number *= 0.001
    elif unit == "half":
        unit = "km"
        number = 21.1
    elif unit == "marathon":
        unit = "km"
        number = 42.2

    return {"distance": number, "unit": unit}
