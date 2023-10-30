import importlib
import parse
importlib.reload(parse)

from parse import parse_distance_text


def test_parse_distance_text():
  expected = {"distance": 0.4, "unit": "km"}
  calculated = parse_distance_text("     400 m     ")
  assert calculated == expected

  expected = {"distance": 10, "unit": "km"}
  calculated = parse_distance_text("     10 km     ")
  assert calculated == expected

  expected = {"distance": 21.1, "unit": "km"}
  calculated = parse_distance_text("  half  ")
  assert calculated == expected

  expected = {"distance": 42.2, "unit": "km"}
  calculated = parse_distance_text("  marathon  ")
  assert calculated == expected

  expected = {"distance": 6.1, "unit": "mi"}
  calculated = parse_distance_text("  6.1 mi  ")
  assert calculated == expected
