import datetime

from django.db.models import Sum
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from overtime.models import OvertimeApplication


def get_total_non_statutory_deductions(employee):
    if employee.deduction_set.all():
        sum = employee.deduction_set.aggregate(Sum('amount'))
        total_deduction = sum['amount__sum']
        return total_deduction


def get_total_nssf(payrolls):
    sum = payrolls.aggregate(Sum('total_nssf_contrib'))
    total_nssf_contrib = sum['total_nssf_contrib__sum']
    return total_nssf_contrib


def get_total_paye(payrolls):
    sum = payrolls.aggregate(Sum('paye'))
    paye = sum['paye__sum']
    return paye


def get_total_gross_pay(payrolls):
    sum = payrolls.aggregate(Sum('gross_salary'))
    gross_salary = sum['gross_salary__sum']
    return gross_salary


def get_total_basic_pay(employees):
    sum = employees.aggregate(Sum('basic_salary'))
    basic_salary = sum['basic_salary__sum']
    return basic_salary


def get_total_net_pay(payrolls):
    sum = payrolls.aggregate(Sum('net_salary'))
    net_salary = sum['net_salary__sum']
    return net_salary


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def get_overtime_pay(applicant):
    current_month = datetime.datetime.today().month
    overtime_applications = OvertimeApplication.objects.filter(date__month=current_month, applicant=applicant)

    total_overtime_pay=0
    if not overtime_applications:
        return None
    else:
        for overtime_application in overtime_applications:
            total_overtime_pay = total_overtime_pay + float(overtime_application.overtime_pay)

        return total_overtime_pay

