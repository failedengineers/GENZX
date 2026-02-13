from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, Http404,HttpResponseRedirect,HttpResponse
from django.contrib import messages
import datetime
from .forms import UploadFileForm # ADD THIS IN UPDATED GITHUB

from goal.models import Course, Semester, Subject, contact, Resource
from .utils import editor


#from django.http import HttpResponseRedirect add this
#from .forms import UploadFileForm add this 


def base(request):
    return render(request,'base.html')

# home
def home(request):
    courses = Course.objects.all()  # all courses to populate dropdown#rint(courses)
    return render(request, 'index.html', {'courses': courses})



# semester list
def get_semesters(request):
    course_id = request.GET.get("course")

    if not course_id or not course_id.isdigit():
        return JsonResponse({"semesters": []})

    semesters = Semester.objects.filter(course_id=course_id).values("id", "number")

    return JsonResponse({
        "semesters": list(semesters)
    })
    return JsonResponse({"semesters": []})



#subjecs list
def subject(request):
    course = request.GET.get('course_id')
    sem = request.GET.get('sem_id')

    if not course or not sem:
        raise Http404("Invalid request")

    if not course.isdigit() or not sem.isdigit():
        raise Http404("Invalid request")

    data = Subject.objects.filter(
        semester_id=int(sem),
        semester__course_id=int(course)
    )

    if not data.exists():
        raise Http404("Subject not found")

    return render(request, 'subjects.html', {'subjects': data})



# about page 
def about(request):
    return render(request,'about.html')


#  conatct form page
def CONTACT(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contactdata=contact(name=name,email=email,message=message,date=datetime.datetime.now())
        contactdata.save()
        messages.success(request, "Message submitted successfully. We will contact you soon.")
        return redirect("contact")  # reload page cleanly

    return render(request,'contact.html')

# cgpa calc page
def cgpa(request):
    if request.method == 'POST':
        marks_list = request.POST.getlist('grades[]')
        credits_list = request.POST.getlist('credits[]')

        def marks_to_gp(marks):
            marks = float(marks)
            if marks >= 90:       # O
                return 10
            elif marks >= 75:     # A+
                return 9
            elif marks >= 65:     # A
                return 8
            elif marks >= 55:     # B+
                return 7
            elif marks >= 50:     # B
                return 6
            elif marks >= 45:     # C
                return 5
            elif marks >= 40:     # P
                return 4
            else:                 # F or absent
                return 0

        total_weighted_gp = 0
        total_credits = 0

        for m, c in zip(marks_list, credits_list):
            if m and c:
                gp = marks_to_gp(m)
                c = float(c)
                total_weighted_gp += gp * c
                total_credits += c

        if total_credits == 0:
            return render(request, 'cgpa.html', {
                'error': 'Please enter credits for all subjects'
            })

        cgpa_value = round(total_weighted_gp / total_credits, 2)

        return render(request, 'cgpa.html', {
            'cgpa': cgpa_value
        })

    return render(request, 'cgpa.html')





# main page
def res_page(request):
    subject_id = request.GET.get('subject_id')

    
    if not subject_id:
        raise Http404("Subject not provided")

    if not subject_id.isdigit():
        raise Http404("Invalid subject")

    subject = get_object_or_404(Subject, id=int(subject_id))

    sem = subject.semester
    course = sem.course

    subjects = Subject.objects.filter(
        semester=sem,
        semester__course=course
    )

    return render(request, "resources.html", {
        "subjects": subjects,
        "current_subject": subject
    })




from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Subject, Resource

def api_resources(request):
    subject_id = request.GET.get("subject_id")
    if not subject_id or not subject_id.isdigit():
        return Http404('invalid subject id')
        #return JsonResponse({"error": "Invalid subject"}, status=404)

    subject = get_object_or_404(Subject, id=int(subject_id))

    resources_qs = Resource.objects.filter(subject=subject)
    resources = [
        {
            "id": r.id,
            "type": r.type,
            "title": r.title,
            "unit_number": r.unit_number,
            "content": r.content,
            "link": r.link,
            "link_text": getattr(r, "link_text", "View Link")
        }
        for r in resources_qs
    ]

    return JsonResponse({"subject": subject.name, "resources": resources})

# 404
from django.shortcuts import render

def custom_404(request, exception):
    return render(request, "404.html", status=404)

def file(request):
    if request.method == "POST":

        old=request.POST.getlist('old_value[]')
        new=request.POST.getlist('new_value[]')
        print(old)
        print(new)
        if "" in old:
            return HttpResponse("Values cannot be empty")
        if "" in new:
            return HttpResponse("Values cannot be empty")

        file=request.FILES['pdf_file']
        print(old)
        print(new)
        print(file)
        response=editor(file,old,new)
        return response

    return render(request,'file.html')
