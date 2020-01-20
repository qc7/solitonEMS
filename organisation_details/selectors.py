from employees.models import Position
from recruitment.models import JobAdvertisement


def get_all_positions():
    return Position.objects.all()


def get_position(position_id):
    return Position.objects.get(pk=position_id)
