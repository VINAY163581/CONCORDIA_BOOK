from django.shortcuts import render
from .models import Textbook
from django.http import HttpResponse

def display_textbooks(request, course_code):
    # Retrieve textbooks filtered by course code and availability
    textbooks = Textbook.objects.filter(course_code=course_code, availability=True)

    if textbooks:
        context = {'textbooks': textbooks, 'course_code': course_code}
    else:
        context = {'message': "No textbooks available for this course."}

    return render(request, 'display_textbooks.html', context)

def index(request):
    return HttpResponse("Welcome to the Textbooks module.")

