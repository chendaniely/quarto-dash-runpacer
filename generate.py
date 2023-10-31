import convert

def generate_reference_range(input_time, range_faster=-30, range_slower=30, by=1):
  """Generate a list of seconds.

  Tries to keep the input_time value in the center of the list when the ranges
  on both sides are the same.
  This helps when the `by` is not a multiple of the faster and slower second ranges.
  """
  seconds = convert.input_time_seconds(input_time, verbose=False)
  seconds_range = (
    list(range(int(seconds), int(seconds) + range_faster, by * -1))
    + [int(seconds)]
    + list(range(int(seconds), int(seconds) + range_slower, by))
  )

   # use set to remove duplicates, then sort
  return sorted(list(set(seconds_range)))
