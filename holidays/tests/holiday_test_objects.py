from holidays.models import Holiday


def create_holiday_test_object():
    holiday = Holiday.objects.create(
        name="Christmas Day",
        date="2019-12-25"
    )

    return holiday