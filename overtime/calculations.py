from holidays.selectors import is_on_holiday


def get_overtime_pay(overtime_application) -> float:
    # determine the overtime pay for the overtime application
    if overtime_application.is_on_holiday or overtime_application.is_on_sunday:
        overtime_amount = overtime_application.number_of_hours * 2 * overtime_application.applicant.\
            overtime_hourly_rate
        return overtime_amount
    else:
        overtime_amount = overtime_application.number_of_hours * 1.5 * overtime_application.applicant.\
            overtime_hourly_rate
        return overtime_amount
