def coalesce(*arg):
    return next((a for a in arg if a is not None), None)


def seconds_to_minutes(seconds: int) -> str:
    minutes = seconds // 60
    left_seconds = seconds % (minutes * 60) if minutes != 0 else seconds

    return f"{str(minutes).rjust(2, '0')}:{str(left_seconds).rjust(2, '0')}"
