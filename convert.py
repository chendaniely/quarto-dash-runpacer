import datetime
import time

import conversions
import parse


def input_time_seconds(input_time, verbose):
    num_colons = input_time.count(":")

    if num_colons == 1:
        x = time.strptime(input_time, "%M:%S")
        seconds = datetime.timedelta(
            minutes=x.tm_min, seconds=x.tm_sec
        ).total_seconds()
    elif num_colons == 2:
        x = time.strptime(input_time, "%H:%M:%S")
        seconds = datetime.timedelta(
            hours=x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec
        ).total_seconds()
    else:
        raise ValueError("input_time must be in the format HH:MM:SS or MM:SS")

    if verbose:
        print(f"Total number of seconds: {seconds}")

    return seconds


def pace_times(input_time, input_dist_unit, output_dist_unit, verbose=False):
    """Return a time in minutes per output distance unit."""
    input_distance_unit_parsed = parse.parse_distance_text(input_dist_unit)
    input_distance = input_distance_unit_parsed["distance"]
    input_unit = input_distance_unit_parsed["unit"]

    seconds = input_time_seconds(input_time, verbose=verbose)

    km_mile_input = conversions.km_mile_distances(input_distance, input_unit)
    output_parsed = parse.parse_distance_text(output_dist_unit)
    km_mile_output = conversions.km_mile_distances(
        output_parsed["distance"], output_parsed["unit"]
    )

    x = seconds / km_mile_input["km"] * km_mile_output["km"]
    td = datetime.timedelta(seconds=x)

    return(
        f"{td.seconds // 3600:02d}:{td.seconds // 60 % 60:02d}:{td.seconds % 60:02d}"
    )
