import convert

def generate_reference_range(input_time, range_faster=30, range_slower=30, by=1):
  seconds = convert.input_time_seconds(input_time, verbose=False)
  seconds_range = range(int(seconds) - range_faster, int(seconds) + range_slower, by)

  return seconds_range
