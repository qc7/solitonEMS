from contracts.selectors import get_contract
from employees.services import suspend


def terminate(contract):
    employee = contract.employee
    suspend(employee)
    contract.status = "Passive"
    contract.save()
    return contract


def activate(contract):
    employee = contract.employee
    employee.status = "Active"
    employee.save()
    contract.status = "Active"
    contract.save()
    return contract
