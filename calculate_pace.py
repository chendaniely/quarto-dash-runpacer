# used for end-to-end testing of the pace calculator

import conversions
import parse
from convert import pace_times

REFERENCE_DISTANCES = [
    "400m",
    "1km",
    "1mi",
    "5km",
    "8km",
    "10km",
    "10mi",
    "half",
    "marathon",
    "50km",
    "50mi",
    "100km",
    "100mi",
]

distance_unit = parse.parse_distance_text("10km")

pace_times("23:31", "5km", "1mi")
pace_times("25:00", "5km", "1mi")
pace_times("1:53:02", "half", "1mi")
pace_times("53:00", "6.1 mi", "")
