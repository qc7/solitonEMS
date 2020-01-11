from employees.models import Position


def get_all_positions():
    return Position.objects.all()
