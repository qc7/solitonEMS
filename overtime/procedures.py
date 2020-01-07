from django.utils.dateparse import parse_datetime


def is_duration_valid(start_time, end_time):
    start_time_obj = parse_datetime(start_time)
    end_time_obj = parse_datetime(end_time)
    return end_time_obj > start_time_obj


def get_overtime_application_hours(start_time, end_time) -> int:
    difference = end_time - start_time
    hours = difference.seconds/3600
    return hours
