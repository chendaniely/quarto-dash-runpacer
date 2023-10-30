import datetime

def display_seconds(seconds):
    """Return a time in HH:MM:SS format."""
    td = datetime.timedelta(seconds=seconds)
    return(
        f"{td.seconds // 3600:02d}:{td.seconds // 60 % 60:02d}:{td.seconds % 60:02d}"
    )
