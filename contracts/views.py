from django.shortcuts import render


# Create your views here.
from contracts.selectors import get_all_contracts
from employees.selectors import get_active_employees
from organisation_details.selectors import get_all_positions


def manage_job_contracts(request):
    positions = get_all_positions()
    employees = get_active_employees()
    contracts = get_all_contracts()
    context = {
        "contracts_page": "active",
        "employees": employees,
        "positions": positions,
        "contracts": contracts,
    }
    return render(request, 'contracts/manage_job_contracts.html', context)


def view_user_contracts(request):
    context = {
        "contracts_page": "active"
    }

    return render(request, 'contracts/view_user_contracts.html', context)
