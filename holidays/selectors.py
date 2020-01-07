import datetime
from holidays.models import Holiday


def is_on_holiday(date_time):
    # Check if date is a holiday
    date = date_time.date()
    holiday = Holiday.objects.filter(date=date)

    if holiday:
        return True
    else:
        return False


def get_all_holidays():
    holidays = Holiday.objects.all()
    return holidays


def get_holiday(holiday_id):
    holiday = Holiday.objects.get(pk=holiday_id)
    return holiday

