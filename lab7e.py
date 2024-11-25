#!/usr/bin/env python3
# Student ID: 155871221
class Time:
    """Simple object type for time of the day.
       Data attributes: hour, minute, second
    """
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object"""
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """Return a string representation for the object self, used by print()"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        """Return a string representation for the object self in the interactive shell"""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def format_time(self):
        """Return time object as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, other_time):
        """Add the current time object with another time object."""
        total_seconds = self.time_to_sec() + other_time.time_to_sec()
        total_seconds %= 86400  # Wrap within a day
        return sec_to_time(total_seconds)

    def time_to_sec(self):
        """Convert the time object to seconds since midnight."""
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    @staticmethod
    def sec_to_time(seconds):
        """Convert seconds since midnight to a Time object."""
        return sec_to_time(seconds)

    def change_time(self, seconds):
        """Modify the current time object based on seconds passed."""
        total_seconds = self.time_to_sec() + seconds
        total_seconds %= 86400  # Wrap within a day
        if total_seconds < 0:  # Handle negative wrap-around
            total_seconds += 86400
        new_time = sec_to_time(total_seconds)
        self.hour, self.minute, self.second = new_time.hour, new_time.minute, new_time.second

    def valid_time(self):
        """Validate if the time object attributes are within a valid range."""
        if not (0 <= self.hour < 24 and 0 <= self.minute < 60 and 0 <= self.second < 60):
            return False
        return True


def sec_to_time(seconds):
    """Convert seconds since midnight to a Time object."""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
