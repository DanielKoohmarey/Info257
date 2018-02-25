from django.shortcuts import render
from info257.models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def home(request):
    return render(request, 'index.html')

@csrf_exempt
def courses(request):
    if request.method == 'POST':
        new_course = Courses(   ccn = request.POST['ccn'], 
                                course_title = request.POST['course_title'],
                                course_code = request.POST['course_code'],
                                section_no = request.POST['section_no'],
                                description = request.POST['description'],
                                time = request.POST['time'],
                                room_no = request.POST['room_no'],
                                building_name = request.POST['building_name'],
                                course_type = request.POST['course_type'],
                                units = request.POST['units'],
                                exam = request.POST['exam']
                            )
        new_course.save()
    courses = Courses.objects.all()
    return render(request, 'courses.html', {'table':courses})

@csrf_exempt
def professors(request):
    print request.POST
    if request.method == 'POST':
        new_professor = Professors( professor_name = request.POST['professor_name'],
                                    ccn = request.POST['ccn'],
                                    rating = request.POST['rating'],
                                    salary = request.POST['salary'],
                                    position = request.POST['position'],
                                    homepage = request.POST['homepage']
                                  )
        new_professor.save()
    professors = Professors.objects.all()
    return render(request, 'professors.html', {'table':professors})

@csrf_exempt
def assistants(request):
    error = ''
    if request.method == 'POST':
        if 'search' in request.POST:
            return handleSearch(request,Assistants, 'assistants.html')
            
        else:
            new_assistant = Assistants( person_name = request.POST['person_name'][0],
                                        ccn = request.POST['ccn'][0],
                                        officer = 'officer' in request.POST
                                      )
            new_assistant.save()
    assistants = Assistants.objects.all()
    return render(request, 'assistants.html', {'table':assistants, 'error':error})

@csrf_exempt
def buildings(request):
    if request.method == 'POST':
        new_building = Buildings( building_name = request.POST['building_name'],
                                  history = request.POST['history'],
                                  built = request.POST['built'],
                                  namesake = request.POST['namesake']
                                )
        new_assistant.save()
    buildings = Buildings.objects.all()
    return render(request, 'buildings.html', {'table':buildings})

@csrf_exempt
def tutors(request):
    if request.method == 'POST':
        new_tutor = Tutors( person_name = request.POST['person_name'],
                            course_codes = request.POST['course_codes'],
                            day = request.POST['day'],
                            time = request.POST['time'],
                            building_name = request.POST['building_name'],
                            room_number = request.POST['room_number']
                          )
        new_tutor.save()
    tutors = Tutors.objects.all()
    return render(request, 'tutors.html', {'table':tutors})
    
def handleSearch(request,table,page):
    requestDict = dict(request.POST)
    requestDict.pop('search',None)
    for key,val in requestDict.items():
        if not val[0]:
            requestDict.pop(key,None)
        else:
            requestDict[key]=val[0]
    matches = table.objects.filter(**requestDict)
    return render(request, page, {'table':matches})




