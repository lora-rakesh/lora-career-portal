from django.shortcuts import render

# Create your views here.
import random
import string
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Applicant
from datetime import datetime

def generate_referral_code():
    # Keeps trying until a unique referral code is generated
    while True:
        code = 'LIT' + ''.join(random.choices(string.digits, k=5))
        if not Applicant.objects.filter(referral_code=code).exists():
            return code

def user_form_view(request):
    if request.method == 'POST':
        data = request.POST
        file = request.FILES.get('resume')

        # 1. Check if email already exists
        if Applicant.objects.filter(email=data['email']).exists():
            messages.error(request, "This email has already been used to apply.")
            return render(request, 'index.html')

        referral_code = generate_referral_code()

        try:
            # 2. Save applicant data
            applicant = Applicant.objects.create(
                full_name=data['fullName'],
                gender=data['gender'],
                dob=data['dob'],
                email=data['email'],
                phone=data['phone'],
                address=data['address'],
                education=data['education'],
                graduation_year=data['graduationYear'],
                skills=data['skills'],
                experience=data['experience'],
                resume=file,
                job_role=data['jobRole'],
                current_company=data.get('currentCompany', ''),
                expected_salary=data.get('expectedSalary') or 0,
                notice_period=data.get('noticePeriod') or 0,
                relocate=data['relocate'],
                referral_code=referral_code
            )

            # 3. Send referral code via email
            send_mail(
                'Your Referral Code from JobPortal',
                f'Thank you for applying to LoRa IT Innovations!....we have received your application.If your skill set matches the position, our Recruitment team will reach out to discuss next steps in the process. Your referral code is: {referral_code} for future reference.',
                'loracareerportal@gmail.com',  # Must match EMAIL_HOST_USER
                [data['email']],
                fail_silently=False,
            )

            return render(request, 'thankyou.html')

        except IntegrityError:
            messages.error(request, "There was an error saving your data. Please try again.")
            return render(request, 'index.html')

    return render(request, 'index.html')



def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_login')
        else:
            messages.error(request, 'Invalid username or password.')

    applicants = []
    if request.user.is_authenticated:
        applicants = Applicant.objects.all().order_by('-submitted_at')

        search_date = request.GET.get('search_date')
        if search_date:
            try:
                date_obj = datetime.strptime(search_date, "%Y-%m-%d").date()
                applicants = applicants.filter(submitted_at__date=date_obj)
            except ValueError:
                messages.error(request, "Invalid date format.")

    return render(request, 'admin.html', {'applicants': applicants})


def admin_logout(request):
    logout(request)
    return redirect('admin_login')


def delete_applicant(request, id):
    applicant = get_object_or_404(Applicant, id=id)
    applicant.delete()
    return redirect('admin_login')