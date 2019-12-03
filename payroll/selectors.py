from payroll.models import Payslip, PayrollRecord


def get_payroll_by_id(payroll_id):
    payroll = Payslip.objects.get(pk=payroll_id)
    return payroll


def get_payroll_record_by_id(payroll_record_id):
    payroll_record = PayrollRecord.objects.get(pk=payroll_record_id)
    return payroll_record
