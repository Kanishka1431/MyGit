# app_14_3/views.py

from django.shortcuts import render
from datetime import datetime

def resume_view(request):
    skills = [
        {'name': 'Java', 'category': 'Programming'},
        {'name': 'C', 'category': 'Programming'},
        {'name': 'Python', 'category': 'Programming'},
        {'name': 'Django', 'category': 'Framework'},
 {'name': 'OpenCV', 'category': 'Library'},
        {'name': 'Communication', 'category': 'Soft Skill'},
        {'name': 'Teamwork', 'category': 'Soft Skill'},
    ]
    
    contact_details = {
        'email': 'your_email@example.com',  # Replace with your email
        'phone': '123-456-7890',            # Replace with your phone number
        'linkedin': 'your_linkedin_profile', # Replace with your LinkedIn profile
    }

    current_year = datetime.now().year

    return render(request, 'app_14_3/resume.html', {'skills': skills, 'contact': contact_details, 'current_year': current_year})