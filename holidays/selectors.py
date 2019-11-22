from holidays.models import Holiday


def is_on_holiday(date):
    # Check if date is a holiday
    holiday = Holiday.objects.filter(date=date)

    if holiday:
        return True
    else:
        return False
