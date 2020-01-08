from holidays.models import Holiday


def create_holiday(date, name):
    holiday = Holiday.objects.create(
        date=date,
        name=name
    )

    return holiday
