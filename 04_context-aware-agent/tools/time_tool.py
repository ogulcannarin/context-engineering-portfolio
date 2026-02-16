from datetime import datetime

def get_time():
    """Returns the current time in HH:MM:SS format."""
    return datetime.now().strftime("%H:%M:%S")

def get_datetime():
    """Returns the current date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")