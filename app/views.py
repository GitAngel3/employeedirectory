

from django.shortcuts import render

def app(request):
    my_objects = [
        {'name': 'John', 'Job_title': 'Manager', 'salary': 84000,'employee_type':'Part time'},
        {'name': 'Jane', 'Job_title': 'Employee', 'salary': 25000,'employee_type':'Full time'},
        {'name': 'Bob', 'Job_title': 'HR Manager', 'salary':48000,'employee_type':'Full time' },
        {'name': 'Ann', 'Job_title': 'Programmer', 'salary': 60000,'employee_type':'Full time'},
        {'name': 'George', 'Job_title': 'Assistant', 'salary':25000,'employee_type':'Part time'},
        {'name': 'Seena', 'Job_title': 'Employee', 'salary': 25000,'employee_type':'Part time'}
        
    ]
    context = {'my_objects': my_objects}
    return render(request, 'index.html', context)