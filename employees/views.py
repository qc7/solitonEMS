from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Employee, HomeAddress, Certification, EmergencyContact, Beneficiary, Spouse
# Create your views here.

# Authentication

# dashboard
@login_required
def dashboard_page(request):
    # # The line requires the user to be authenticated before accessing the view responses.
    # if not request.user.is_authenticated:
    #     # if the user is not authenticated it renders a login page
    #     return render(request,'registration/login.html',{"message":None})

    context = {
        "dashboard_page": "active"
    }
    return render(request, 'employees/dashboard.html', context)


@login_required
def employees_page(request):
    # The line requires the user to be authenticated before accessing the view responses.
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page
        return render(request, 'registration/login.html', {"message": None})
    context = {
        "employees_page": "active",
        "employees": Employee.objects.all()

    }
    return render(request, 'employees/employees.html', context)


@login_required
def leave_page(request):
    # The line requires the user to be authenticated before accessing the view responses.
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page
        return render(request, 'registration/login.html', {"message": None})
    context = {
        "leave_page": "active"
    }
    return render(request, 'employees/leave.html', context)


@login_required
def employee_page(request, id):
    # The line requires the user to be authenticated before accessing the view responses.
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page
        return render(request, 'registration/login.html', {"message": None})

    employee = Employee.objects.get(pk=id)
    context = {
        "employees_page": "active",
        "employee": employee,
        "certifications": employee.certification_set.all(),
        "emergency_contacts": employee.emergencycontact_set.all(),
        "beneficiaries": employee.beneficiary_set.all(),
        "spouses": employee.spouse_set.all()
    }
    return render(request, 'employees/employee.html', context)


@login_required
def payroll_page(request):
    # The line requires the user to be authenticated before accessing the view responses.
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page
        return render(request, 'registration/login.html', {"message": None})

    context = {
        "payroll_page": "active"
    }
    return render(request, 'employees/payroll.html', context)


@login_required
def edit_employee_page(request, id):
    # The line requires the user to be authenticated before accessing the view responses.
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page
        return render(request, 'registration/login.html', {"message": None})
    employee = Employee.objects.get(pk=id)
    context = {
        "employees_page": "active",
        "employee": employee
    }
    return render(request, 'employees/edit_employee.html', context)


@login_required
def edit_certification_page(request, id):
    # The line requires the user to be authenticated before accessing the view responses.
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page
        return render(request, 'registration/login.html', {"message": None})

    certification = Certification.objects.get(pk=id)
    context = {
        "employees_page": "active",
        "certification": certification
    }

    return render(request, 'employees/edit_cert.html', context)


@login_required
def edit_emergency_contact_page(request, id):
    # The line requires the user to be authenticated before accessing the view responses.
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page
        return render(request, 'registration/login.html', {"message": None})

    emergency_contact = EmergencyContact.objects.get(pk=id)
    context = {
        "employees_page": "active",
        "emergency_contact": emergency_contact
    }

    return render(request, 'employees/edit_emergency.html', context)

# The login view authenticates the user
# The view also renders the login page


@login_required
def edit_beneficiary_page(request, id):
    # The line requires the user to be authenticated before accessing the view responses.
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page
        return render(request, 'registration/login.html', {"message": None})

    beneficiary = Beneficiary.objects.get(pk=id)
    context = {
        "employees_page": "active",
        "beneficiary": beneficiary
    }

    return render(request, 'employees/edit_beneficiary.html', context)


def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('dashboard_page'))

    else:
        return render(request, "registration/login.html", {"message": "Invalid credentials"})


def login_page(request):
    return render(request, "registration/login.html")

# The logout view logs out the user


def logout_view(request):
    logout(request)
    return render(request, "registration/login.html", {"message": "Logged Out", "info": "info"})

###################################################################
# Processes
###################################################################
@login_required
def add_new_employee(request):
    if request.method == 'POST':
        # Fetching data from the add new employee form
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        position = request.POST['position']
        gender = request.POST['gender']
        marital_status = request.POST['marital_status']
        start_date = request.POST['start_date']
        nationality = request.POST['nationality']
        nssf_no = request.POST['nssf_no']
        ura_tin = request.POST['ura_tin']
        national_id = request.POST['national_id']
        telephone = request.POST['telephone']
        residence_address = request.POST['residence_address']
        dob = request.POST['dob']

        try:
            # Creating instance of Employee
            employee = Employee(first_name=first_name, last_name=last_name, position=position, gender=gender,
                                marital_status=marital_status, start_date=start_date, nationality=nationality, nssf_no=nssf_no,
                                ura_tin=ura_tin, national_id=national_id, telephone_no=telephone, residence_address=residence_address,
                                dob=dob)
            # Saving the employee instance
            employee.save()
            context = {
                "employees_page": "active",
                "success_msg": "You have successfully added %s to the employees" % (employee.first_name)
            }

            return render(request, 'employees/success.html', context)

        except:
            context = {
                "employees_page": "active",
                "failed_msg": "Failed! Something went wrong. Contact Bright and Hakim"
            }
            return render(request, "employees/failed.html", context)

    else:
        context = {
            "employees_page": "active",
            "failed_msg": "Failed! You performed a GET request"
        }

        return render(request, "employees/failed.html", context)


@login_required
def delete_employee(request, id):
    try:
        # Grab the employee
        employee = Employee.objects.get(pk=id)

        name = employee.first_name + " " + employee.last_name
    # Delete the employee
        employee.delete()

    except Employee.DoesNotExist:
        context = {
            "employees_page": "active",
            "deleted_msg": "The employee no longer exists on the system"
        }

        return render(request, 'employees/deleted.html', context)

    context = {
        "employees_page": "active",
        "deleted_msg": "You have deleted %s from employees" % (name)
    }
    return render(request, 'employees/deleted.html', context)


@login_required
def edit_employee(request, id):
    if request.method == 'POST':
        # Fetching data from the add new employee form
        try:
            employee = Employee.objects.get(pk=id)
            employee.first_name = request.POST['first_name']
            employee.last_name = request.POST['last_name']
            employee.position = request.POST['position']
            employee.gender = request.POST['gender']
            employee.marital_status = request.POST['marital_status']
            employee.start_date = request.POST['start_date']
            employee.nationality = request.POST['nationality']
            employee.nssf_no = request.POST['nssf_no']
            employee.ura_tin = request.POST['ura_tin']
            employee.national_id = request.POST['national_id']
            employee.telephone_no = request.POST['telephone']
            employee.residence_address = request.POST['residence_address']
            employee.dob = request.POST['dob']

            # Saving the employee instance
            employee.save()
            context = {
                "employees_page": "active",
                "success_msg": "You have successfully updated %s's bio data" % (employee.first_name)
            }

            return render(request, 'employees/success.html', context)

        except:
            context = {
                "employees_page": "active",
                "failed_msg": "Something went wrong. Contact Bright and Hakim"
            }
            return render(request, "employees/failed.html", context)

    else:
        context = {
            "employees_page": "active",
            "failed_msg": "Failed! You performed a GET request"
        }

        return render(request, "employees/failed.html", context)


@login_required
def add_new_home_address(request):
    if request.method == 'POST':
        # Fetching data from the add new home address form
        employee_id = request.POST['employee_id']
        division = request.POST['division']
        district = request.POST['district']
        county = request.POST['county']
        sub_county = request.POST['sub_county']
        parish = request.POST['parish']
        village = request.POST['village']
        address = request.POST['address']
        telephone = request.POST['telephone']
        try:
            employee = Employee.objects.get(pk=employee_id)
            # Creating instance of Home Address
            homeaddress = HomeAddress(employee=employee, district=district, division=division, county=county, sub_county=sub_county,
                                      parish=parish, village=village, address=address, telephone=telephone)
            # Saving the Home Address instance
            homeaddress.save()
            context = {
                "employees_page": "active",
                "success_msg": "You have successfully added Home Address to the %s's details" % (employee.first_name)
            }

            return render(request, 'employees/success.html', context)

        except:
            context = {
                "employees_page": "active",
                "failed_msg": "Failed! Something went wrong. Contact Bright and Hakim"
            }
            return render(request, "employees/failed.html", context)

    else:
        context = {
            "employees_page": "active",
            "failed_msg": "Failed! You performed a GET request"
        }

        return render(request, "employees/failed.html", context)


@login_required
def edit_home_address(request):
    if request.method == 'POST':
        # Fetching data from the edit home address form
        try:
            # Fetch the employee
            employee_id = request.POST['employee_id']
            employee = Employee.objects.get(pk=employee_id)
            # Grab the home address
            home_address = HomeAddress.objects.get(employee=employee)

            home_address.district = request.POST['district']
            home_address.division = request.POST['division']
            home_address.county = request.POST['county']
            home_address.sub_county = request.POST['sub_county']
            home_address.parish = request.POST['parish']
            home_address.village = request.POST['village']
            home_address.address = request.POST['address']
            home_address.telephone = request.POST['telephone']

            # Saving the home address instance
            home_address.save()
            context = {
                "employees_page": "active",
                "success_msg": "You have successfully updated %s's home address" % (employee.first_name)
            }

            return render(request, 'employees/success.html', context)

        except:
            context = {
                "employees_page": "active",
                "failed_msg": "Something went wrong. Contact Bright and Hakim"
            }
            return render(request, "employees/failed.html", context)

    else:
        context = {
            "employees_page": "active",
            "failed_msg": "Failed! You performed a GET request"
        }

        return render(request, "employees/failed.html", context)


@login_required
def add_certification(request):
    if request.method == 'POST':
        # Fetching data from the add new employee form
        institution = request.POST['institution']
        year_completed = request.POST['year_completed']
        certification = request.POST['certification']
        grade = request.POST['grade']
        employee_id = request.POST['employee_id']

        employee = Employee.objects.get(pk=employee_id)

        try:
            # Creating instance of Certification
            certification = Certification(employee=employee, institution=institution, year_completed=year_completed, name=certification,
                                          grade=grade)
            # Saving the certification instance
            certification.save()
            context = {
                "employees_page": "active",
                "success_msg": "You have successfully added %s to the certifications" % (certification.name)
            }

            return render(request, 'employees/success.html', context)

        except:
            context = {
                "employees_page": "active",
                "failed_msg": "Failed! Something went wrong. Contact Bright and Hakim"
                "back"
            }
            return render(request, "employees/failed.html", context)

    else:
        context = {
            "employees_page": "active",
            "failed_msg": "Failed! You performed a GET request"
        }

        return render(request, "employees/failed.html", context)


def edit_certification(request):
    if request.method == 'POST':

        # Fetch the certification id
        cert_id = request.POST['cert_id']

        # Grab the certification
        certification = Certification.objects.get(pk=cert_id)
        certification.institution = request.POST['institution']
        certification.year_completed = request.POST['year_completed']
        certification.name = request.POST['name']
        certification.grade = request.POST['grade']

        # Saving the certification instance
        certification.save()
        context = {
            "employees_page": "active",
            "success_msg": "You have successfully updated %s's certification" % (certification.employee.first_name)
        }

        return render(request, 'employees/success.html', context)
        context = {
            "employees_page": "active",
            "failed_msg": "Something went wrong. Contact Bright and Hakim"
        }
        return render(request, "employees/failed.html", context)

    else:
        context = {
            "employees_page": "active",
            "failed_msg": "Failed! You performed a GET request"
        }

        return render(request, "employees/failed.html", context)


@login_required
def delete_certification(request, id):
    try:
        # Grab the certification
        certification = Certification.objects.get(pk=id)

        name = certification.name
    # Delete the certification
        certification.delete()

    except Certification.DoesNotExist:
        context = {
            "employees_page": "active",
            "deleted_msg": "The certification no longer exists on the system"
        }

        return render(request, 'employees/deleted.html', context)

    context = {
        "employees_page": "active",
        "deleted_msg": "You have deleted %s from certifications" % (name)
    }
    return render(request, 'employees/deleted.html', context)


def add_emergency_contact(request):
    if request.method == 'POST':
        # Fetching data from the add new employee form
        name = request.POST['name']
        relationship = request.POST['relationship']
        email = request.POST['email']
        mobile_number = request.POST['mobile_number']
        employee_id = request.POST['employee_id']

        employee = Employee.objects.get(pk=employee_id)

        # Creating instance of EmergencyContact
        emergency_contact = EmergencyContact(employee=employee, name=name, relationship=relationship,
                                             mobile_number=mobile_number, email=email)
        # Saving the certification instance
        emergency_contact.save()
        context = {
            "employees_page": "active",
            "success_msg": "You have successfully added %s to the emergency contacts" % (emergency_contact.name)
        }

        return render(request, 'employees/success.html', context)

        context = {
            "employees_page": "active",
            "failed_msg": "Failed! Something went wrong. Contact Bright and Hakim"
            "back"
        }

        return render(request, "employees/failed.html", context)

    else:
        context = {
            "employees_page": "active",
            "failed_msg": "Failed! You performed a GET request"
        }

        return render(request, "employees/failed.html", context)


@login_required
def delete_emergency_contact(request, id):
    try:
        # Grab the emergency contact
        emergency_contact = EmergencyContact.objects.get(pk=id)

        name = emergency_contact.name
    # Delete the certification
        emergency_contact.delete()

    except EmergencyContact.DoesNotExist:
        context = {
            "employees_page": "active",
            "deleted_msg": "The emergency contact no longer exists on the system"
        }

        return render(request, 'employees/deleted.html', context)

    context = {
        "employees_page": "active",
        "deleted_msg": "You have deleted %s from emergency contacts" % (name)
    }
    return render(request, 'employees/deleted.html', context)


def edit_emergency_contact(request):
    if request.method == 'POST':

        # Fetch the emergency contact id
        emergency_id = request.POST['emergency_id']

        # Grab the EmergencyContact
        emergency_contact = EmergencyContact.objects.get(pk=emergency_id)

        emergency_contact.name = request.POST['name']
        emergency_contact.relationship = request.POST['relationship']
        emergency_contact.mobile_number = request.POST['mobile_number']
        emergency_contact.email = request.POST['email']

        # Saving the EmergencyContact instance
        emergency_contact.save()
        context = {
            "employees_page": "active",
            "success_msg": "You have successfully updated %s's emergency contact" % (emergency_contact.employee.first_name)
        }

        return render(request, 'employees/success.html', context)

        context = {
            "employees_page": "active",
            "failed_msg": "Something went wrong. Contact Bright and Hakim"
        }
        return render(request, "employees/failed.html", context)

    else:
        context = {
            "employees_page": "active",
            "failed_msg": "Failed! You performed a GET request"
        }

        return render(request, "employees/failed.html", context)


def add_beneficiary(request):
    if request.method == 'POST':
        # Fetching data from the add new employee form
        name = request.POST['name']
        relationship = request.POST['relationship']
        percentage = request.POST['percentage']
        mobile_number = request.POST['mobile_number']
        employee_id = request.POST['employee_id']

        employee = Employee.objects.get(pk=employee_id)

        # Creating instance of Beneficiary
        beneficiary = Beneficiary(employee=employee, name=name, relationship=relationship,
                                             mobile_number=mobile_number, percentage=percentage)
        # Saving the certification instance
        beneficiary.save()
        context = {
            "employees_page": "active",
            "success_msg": "You have successfully added %s to the emergency beneficiaries" % (beneficiary.name)
        }

        return render(request, 'employees/success.html', context)

        context = {
            "employees_page": "active",
            "failed_msg": "Failed! Something went wrong. Contact Bright and Hakim"
            "back"
        }

        return render(request, "employees/failed.html", context)

    else:
        context = {
            "employees_page": "active",
            "failed_msg": "Failed! You performed a GET request"
        }

        return render(request, "employees/failed.html", context)


def edit_beneficiary(request):
    if request.method == 'POST':

        # Fetch the beneficiary id
        beneficiary_id = request.POST['beneficiary_id']

        # Grab the EmergencyContact
        beneficiary = Beneficiary.objects.get(pk=beneficiary_id)

        beneficiary.name = request.POST['name']
        beneficiary.relationship = request.POST['relationship']
        beneficiary.mobile_number = request.POST['mobile_number']
        beneficiary.percentage = request.POST['percentage']

        # Saving the EmergencyContact instance
        beneficiary.save()
        context = {
            "employees_page": "active",
            "success_msg": "You have successfully updated %s's beneficiary details" % (beneficiary.employee.first_name)
        }

        return render(request, 'employees/success.html', context)

        context = {
            "employees_page": "active",
            "failed_msg": "Something went wrong. Contact Bright and Hakim"
        }
        return render(request, "employees/failed.html", context)

    else:
        context = {
            "employees_page": "active",
            "failed_msg": "Failed! You performed a GET request"
        }

        return render(request, "employees/failed.html", context)


@login_required
def delete_beneficiary(request, id):
    try:
        # Grab the Beneficiary
        beneficiary = Beneficiary.objects.get(pk=id)

        name = beneficiary.name
    # Delete the Beneficiary
        beneficiary.delete()

    except Beneficiary.DoesNotExist:
        context = {
            "employees_page": "active",
            "deleted_msg": "The beneficiary no longer exists on the system"
        }

        return render(request, 'employees/deleted.html', context)

    context = {
        "employees_page": "active",
        "deleted_msg": "You have deleted %s from beneficiaries" % (name)
    }
    return render(request, 'employees/deleted.html', context)


def add_spouse(request):
    if request.method == 'POST':
        # Fetching data from the add new employee form
        name = request.POST['name']
        national_id = request.POST['national_id']
        dob = request.POST['dob']
        occupation = request.POST['occupation']
        telephone = request.POST['telephone']
        nationality = request.POST['nationality']
        passport_number = request.POST['passport_number']
        alien_certificate_number = request.POST['alien_certificate_number']
        immigration_file_number = request.POST['immigration_file_number']
        employee_id = request.POST['employee_id']

        employee = Employee.objects.get(pk=employee_id)

        # Creating instance of Spouse
        spouse = Spouse(employee=employee, name=name, national_id=national_id, dob=dob, occupation=occupation,
                   telephone=telephone, nationality=nationality, passport_number=passport_number,
        alien_certificate_number=alien_certificate_number, immigration_file_number=immigration_file_number)
        # Saving the Spouse instance
        spouse.save()
        context = {
            "employees_page": "active",
            "success_msg": "You have successfully added %s to the spouses" % (spouse.name)
        }

        return render(request, 'employees/success.html', context)

        context = {
            "employees_page": "active",
            "failed_msg": "Failed! Something went wrong. Contact Bright and Hakim"
            "back"
        }

        return render(request, "employees/failed.html", context)

    else:
        context = {
            "employees_page": "active",
            "failed_msg": "Failed! You performed a GET request"
        }

        return render(request, "employees/failed.html", context)


def delete_spouse(request):
    try:
        # Grab the Beneficiary
        beneficiary = Beneficiary.objects.get(pk=id)

        name = beneficiary.name
    # Delete the Beneficiary
        beneficiary.delete()

    except Beneficiary.DoesNotExist:
        context = {
            "employees_page": "active",
            "deleted_msg": "The beneficiary no longer exists on the system"
        }

        return render(request, 'employees/deleted.html', context)

    context = {
        "employees_page": "active",
        "deleted_msg": "You have deleted %s from beneficiaries" % (name)
    }
    return render(request, 'employees/deleted.html', context)

def edit_spouse(request):
    pass
