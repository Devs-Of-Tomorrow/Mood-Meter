from django.views import View
from django.shortcuts import render, redirect
from Maintain.models.employee import Employee
from django.contrib.auth.hashers import make_password


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        # Validation

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        error_message = None
        employee = Employee(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)

        if not error_message:
            employee.password = make_password(employee.password)
            employee.register()
            return redirect('emphome')

        else:
            data = {
                'error': error_message,
                'valuse': value
            }

        return render(request, 'signup.html', data)

    def validateEmployee(self, employee):
        error_message = None;
        if employee.isExists():
            error_message = 'Email Address Already Registered..'

        return error_message