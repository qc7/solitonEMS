from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from contracts.models import Contract
from contracts.selectors import get_contract, get_active_contracts, get_terminated_contracts
from contracts.services import terminate
from employees.selectors import get_active_employees, get_employee
from employees.services import suspend
from organisation_details.selectors import get_all_positions, get_position


def manage_job_contracts(request):
    if request.POST and request.FILES:
        reference_number = request.POST.get('reference_number')
        position_id = request.POST.get('position')
        employee_id = request.POST.get('employee')
        effective_date = request.POST.get('effective_date')
        expiry_date = request.POST.get('expiry_date')
        risk = request.POST.get('risk')
        document = request.FILES.get('document')

        position = get_position(position_id)
        employee = get_employee(employee_id)
        try:
            new_contract = Contract.objects.create(
                reference_number=reference_number,
                position=position,
                employee=employee,
                effective_date=effective_date,
                expiry_date=expiry_date,
                risk=risk,
                document=document
            )
        except IntegrityError:
            messages.warning(request, "The reference number needs to be unique")

        return HttpResponseRedirect(reverse(manage_job_contracts))

    positions = get_all_positions()
    employees = get_active_employees()
    contracts = get_active_contracts()
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


def terminate_contract(request, contract_id):
    contract = get_contract(contract_id)
    terminate(contract)
    return HttpResponseRedirect(reverse(manage_job_contracts))


def edit_contract_page(request, contract_id):
    if request.POST and request.FILES:
        reference_number = request.POST.get('reference_number')
        position_id = request.POST.get('position')
        employee_id = request.POST.get('employee')
        effective_date = request.POST.get('effective_date')
        expiry_date = request.POST.get('expiry_date')
        risk = request.POST.get('risk')
        document = request.FILES.get('document')

        position = get_position(position_id)
        employee = get_employee(employee_id)

        contract_list = Contract.objects.filter(id=contract_id)
        contract_list.update(
            reference_number=reference_number,
            position=position,
            employee=employee,
            effective_date=effective_date,
            expiry_date=expiry_date,
            risk=risk,
            document=document
        )

        return HttpResponseRedirect(reverse(manage_job_contracts))

    contract = get_contract(contract_id)
    positions = get_all_positions()
    employees = get_active_employees()
    context = {
        "contracts_page": "active",
        "contract": contract,
        "employees": employees,
        "positions": positions,
    }
    return render(request, 'contracts/edit_contract.html', context)


def terminated_contracts_page(request):
    terminated_contracts = get_terminated_contracts()
    context = {
        "contracts_page": "active",
        "terminated_contracts": terminated_contracts
    }

    return render(request, 'contracts/terminated_contracts.html', context)
