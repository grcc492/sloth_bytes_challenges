from datetime import datetime, timedelta


def bed_time(alarm_time, sleep_duration):
    try:
        duration_hours, duration_minutes = map(int, sleep_duration.split(":"))
        alarm = datetime.strptime(alarm_time, "%H:%M")
        go_to_bed = alarm - timedelta(hours=duration_hours, minutes=duration_minutes)
        return go_to_bed.strftime("%H:%M")
    except ValueError as e:
        raise ValueError(f"Invalid input: {e}")


if __name__ == "__main__":
    sleep_time_tests = (
        (["07:50", "07:50"],),
        (["06:15", "10:00"], ["08:00", "10:00"], ["09:30", "10:00"]),
        (["05:45", "04:00"], ["07:10", "04:30"]),
    )

    for sleep_time_test in sleep_time_tests:
        go_to_bed_time = [bed_time(alarm, duration) for alarm, duration in sleep_time_test]
        print(go_to_bed_time)
