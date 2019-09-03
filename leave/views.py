from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_date
from django.utils import timezone
import datetime
from django.db.models import (
    Sum,
    Count
)
from datetime import timedelta
import calendar
from collections import namedtuple
from employees.models import Employee
from .models import (
    Leave_Types, 
    Holidays,
    Approval_Path,
    LeaveApplication,
    annual_planner
)

def get_current_user(request, need):
    user = request.user #getting the current logged in User

    cur_user = f'{user.solitonuser.employee.first_name} {user.solitonuser.employee.last_name}'
    cur_role = user.solitonuser.soliton_role.name
    user_dept = user.solitonuser.employee.organisationdetail.department.id
    cur_id = user.solitonuser.employee.id
    gender = user.solitonuser.employee.gender

    if need == "name":
        return cur_user
    elif need == "role":
        return cur_role
    elif need == "dept":
        return user_dept
    elif need == "id":
        return cur_id
    elif need == "gender":
        return gender
    else:
        return 0

@login_required
def leave_dashboard_page(request):
    #applications=""
    # The line requires the user to be authenticated before accessing the view responses.
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page
        return render(request,'registration/login.html',{"message":None})

    user_role = get_current_user(request,"role")
    
    if user_role == "Supervisor":
        applications = LeaveApplication.objects.filter(sup_Status="Pending").order_by('apply_date')
    elif user_role == "HOD":
        applications = LeaveApplication.objects.filter(hod_status="Pending", sup_Status="Approved")\
            .order_by('apply_date')
    elif user_role == "HR":
        applications = LeaveApplication.objects\
            .filter(hr_status="Pending", sup_Status="Approved", hod_status="Approved").order_by('apply_date')
    else:
        applications = ""

    leave_types = Leave_Types.objects.all()
    
    leave_types_dict = {}
    for typ in leave_types:
        leave_count = LeaveApplication.objects.filter(leave_type=typ).count()
        leave_types_dict.update({typ:leave_count})

    context = {
        "leave_dashboard_page": "active",
        "applications": applications,
        "role": user_role,
        "maternity": LeaveApplication.objects.filter(leave_type=1).count(),
        "paternity": LeaveApplication.objects.filter(leave_type=2).count(),
        "compassionate": LeaveApplication.objects.filter(leave_type=3).count(),
        "annual": LeaveApplication.objects.filter(leave_type=4).count(),
        # "sick": LeaveApplication.objects.filter(leave_type=5).count(),
    }
    return render(request, 'leave/dashboard.html', context)

def leave_types_page(request):
     # The line requires the user to be authenticated before accessing the view responses.
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page
        return render(request,'registration/login.html',{"message":None})

    context = {
        "leave_page": "active",
        "types": Leave_Types.objects.all()
    }
    return render(request, 'leave/leave_types.html', context)

def add_new_type(request):
    if request.method == 'POST':
        # Fetching data from the add new leave type form
        leave_type = request.POST['leave_type']
        leave_days = request.POST['leave_days']
        desc = request.POST['desc']

        try:
            # Creating instance of Leave Types
            type_leave = Leave_Types(leave_type=leave_type, leave_days=leave_days,description=desc)
            
            #Saving the leave type instance
            type_leave.save()
            messages.success(request, f'Info Successfully Saved')

            return redirect('leave_types_page')

        except:
            messages.error(request, f'Info Not Saved, Check Your inputs and try again!!!')

            return redirect('leave_types_page')            

    else:
        context = {
            "leave_types_page": "active",
            "failed_msg": "Failed! You performed a GET request"
        }

        return render(request, "employees/failed.html", context)

@login_required
def edit_leave_type_page(request, id):
    # The line requires the user to be authenticated before accessing the view responses.
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page
        return render(request, 'registration/login.html', {"message": None})
    
    leave = Leave_Types.objects.get(pk=id)

    context = {
        "leave_page": "active",
        "leave": leave  
    }
    return render(request, 'leave/leave_type.html', context)

def holidays_page(request):
     # The line requires the user to be authenticated before accessing the view responses.
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page
        return render(request,'registration/login.html',{"message":None})

    context = { 
        "leave_page": "active",
        "holidays": Holidays.objects.all()
    }
    return render(request, 'leave/holidays.html', context)

def add_new_holiday(request):
    if request.method == 'POST':
        # Fetching data from the add new holiday form
        hol_name = request.POST['hol_name']
        hol_date = request.POST['hol_date']
        duration = request.POST['duration']

        try:

            hols = Holidays(holiday_date = hol_date, holiday_name=hol_name, duration=duration)
            hols.save()

            messages.success(request, f'Info Successfully Saved')
            return redirect('holidays_page')

        except:
           messages.error(request, f'Infor Not Saved, Check you inputs and try again!')

           return redirect('holidays_page') 


def approval_path_page(request):
     # The line requires the user to be authenticated before accessing the view responses.
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page
        return render(request,'registration/login.html',{"message":None})

    context = {
        "leave_page": "active",
        "a_path": Approval_Path.objects.all()
    }

    return render(request, "leave/approval_path.html", context)

def add_new_path(request):
    if request.method=="POST":
        path_name = request.POST["pname"]
        required = request.POST["required"]
        fapproval = request.POST["fapproval"]
        sapproval = request.POST["sapproval"]
        lapproval = request.POST["lapproval"]

    try:
        path_ = Approval_Path(path_name=path_name, required = required, 
        first_approval=fapproval, second_approval = sapproval, fourth_approval = lapproval)

        path_.save()

        messages.success(request, f'Info Successfully Saved')
        return redirect('path_page')

    except:
        messages.error(request, f'Infor Not Saved, Check you inputs and try again!')

        return redirect('path_page')

def apply_leave_page(request):
     #The line requires the user to be authenticated before accessing the view responses.
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page
        return render(request,'registration/login.html',{"message":None})

    context = {
        "leave_page": "active",
        "apps": LeaveApplication.objects.filter(employee=get_current_user(request, "id")),
        "l_types":Leave_Types.objects.all(),
        "gender": get_current_user(request, "gender")
    }

    return render(request, "leave/apply_leave.html", context)



@login_required
def apply_leave(request):
    if request.method=="POST":
        
        user = request.user #getting the current logged in user
        employee = user.solitonuser.employee
    

        l_type = Leave_Types.objects.get(pk=request.POST["ltype"])

        date_format = "%Y-%m-%d"
        s_date = request.POST["s_date"]
        e_date = request.POST["e_date"]

        #getting the leave type entitlement
        n_days = calculate_leave_days(s_date, e_date)
        l_days =  l_type.leave_days         
        
        if n_days <= l_days:
            new_balance=0
            if l_type.leave_type == "Annual":
                curr_balance = employee.leave_balance
                new_balance = curr_balance - n_days 

            if n_days <= new_balance:
                leave_app = LeaveApplication(employee = employee, leave_type = l_type, start_date=s_date, 
                end_date = e_date, no_of_days = n_days, balance = curr_balance)

                leave_app.save()

                messages.success(request, 'Leave Request Sent Successfully')

                if str(user.solitonuser.soliton_role) =='Employee':
                    context = {
                    "employee": user.solitonuser.employee,
                    "employee_leave_page":'active'
                    }
                    return render(request,"role/employee/leave.html",context)
                else:
                    return render(request,"role/employee/leave.html",context)
                
            else:
                messages.warning(request, f'You have insufficient {l_type} leave Balance {n_days}')
                if str(user.solitonuser.soliton_role) =='Employee':
                    context = {
                    "employee": user.solitonuser.employee,
                    "employee_leave_page":'active'
                    }
                    return render(request,"role/employee/leave.html",context)
                else:
                    return render(request,"role/employee/leave.html")      

        else:
            messages.warning(request, f'You cannot Request({n_days}) for more than the\
                {l_type.leave_type} leave days ({l_type.leave_days})')
            return render(request,"role/employee/leave.html")

def approve_leave(request):
    if request.method=="POST":
        user = request.user #getting the current logged in User  
        employee = user.solitonuser.employee
        role = get_current_user(request, "role")

        l_type = Leave_Types.objects.get(pk = request.POST.get("ltype"))
        n_days = request.POST.get("ndays")
        leave = LeaveApplication.objects.get(pk=request.POST["app_id"])

        if role == "Supervisor": 
            LeaveApplication.objects.filter(pk=leave.id).update(supervisor=f'{employee.first_name} {employee.last_name}', 
            sup_Status="Approved")

            messages.success(request, 'Leave Approved Successfully')
            return redirect('leave_dashboard_page') 
        elif role == "HOD": 
            LeaveApplication.objects.filter(pk=leave.id).update(hod=f'{employee.first_name} {employee.last_name}', 
            hod_status="Approved")

            messages.success(request, 'Leave Approved Successfully')
            return redirect('leave_dashboard_page') 
        elif role == "HR": 
            curr_balance = 0
            if l_type.leave_type == "Annual":                    
                curr_balance = leave.employee.leave_balance
                new_balance = int(curr_balance) - int(n_days)
            else:
                new_balance = curr_balance
           
            LeaveApplication.objects.filter(pk=leave.id).update(hr = f'{employee.first_name} {employee.last_name}', 
            hr_status="Approved", app_status="Approved", balance = new_balance)

            Employee.objects.filter(pk=leave.employee_id).update(leave_balance=new_balance)

            messages.success(request, 'Leave Approved Successfully')
            return redirect('leave_dashboard_page') 
            
def calculate_leave_days(start_date, end_date):    
    date_format = "%Y-%m-%d"
    from_date = datetime.datetime.strptime(start_date, date_format)
    to_date = datetime.datetime.strptime(end_date, date_format)
    
    date_difference = to_date - from_date  

    all_days_between = (date_difference.days + 1)

    holidays = Holidays.objects.filter(holiday_date__range=(from_date, to_date)).count()


    all_working_days = all_days_between - holidays
    k=0
    while k <= all_days_between:
        check_date = from_date + datetime.timedelta(days = k)
        
        if check_date.weekday() == 6:
            all_working_days = all_working_days - 1
        
        k = k + 1
       
    return all_working_days
        

def leave_calendar(request):
    # first_day = calendar.TextCalendar(calendar.MONDAY)
    # annual_calendar = first_day.formatyear(2019)

    year=2011
    month=12
    change=None

    # init variables
    cal = calendar.Calendar()
    cal.setfirstweekday(6)
    month_days = cal.itermonthdays(year, month)
    lst = [[]]
    week = 0

    # make month lists containing list of days for each week
    # each day tuple will contain list of entries and 'current' indicator
    for day in month_days:
        lst[week].append((day))
        if len(lst[week]) == 7:
            lst.append([])
            week += 1
    
    return redirect("leave/annual_calendar.html")

def leave_planer(request):
     # The line requires the user to be authenticated before accessing the view responses.
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page
        return render(request,'registration/login.html',{"message":None})
    context = { 
        "leave_planner": "active",
        "planner": annual_planner.objects.all(),
        "leave_types": Leave_Types.objects.all(),
        "employees": Employee.objects.all()
    }
    return render(request, 'leave/leave_planner.html', context)
    
def add_new_absence(request):
    if request.method=="POST":
        employee = Employee.objects.get(pk=request.user.id)
        leave = Leave_Types.objects.get(pk=request.POST["leave_type"])
        from_date = request.POST["from_date"]
        to_date = request.POST["to_date"]

    try:
        planner = annual_planner(leave_year="2019", date_from = from_date, date_to = to_date,\
            employee=employee, leave = leave)

        planner.save()

        messages.success(request, f'Data Saved Successfully')

        return redirect('leave_planner')

    except:
        messages.error(request, f'Data Not Saved, Check you inputs and try again!')

        return redirect('leave_planner')
    
def get_leave_overlap(start_date, end_date):
    absences = leave_planer.objects.all()

    Range = namedtuple('Range', ['start', 'end'])

    r1 = Range(start=start_date, end=end_date)
    
    overlap = 0
    overlap_count = 0
    for absence in absences:
        r2 = Range(start=absence.start_date, end=absence.end_date)
        latest_start = max(r1.start, r2.start)
        earliest_end = min(r1.end, r2.end)
        delta = (earliest_end - latest_start).days + 1
        overlap = max(0, delta)

        if overlap > 0:
            overlap_count += 1

    
    return overlap_count