from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

def index(request):
    if request.method == 'POST':
        Student.objects.create(
            name=request.POST['name'],
            tamil=request.POST['tamil'],
            english=request.POST['english'],
            maths=request.POST['maths'],
            science=request.POST['science'],
            social=request.POST['social'],
        )
        return redirect('results')
    return render(request, 'myapp/index.html')

def results(request):
    query = request.GET.get('search', '')
    if query:
        students = Student.objects.filter(name__icontains=query)
    else:
        students = Student.objects.all()
    return render(request, 'myapp/results.html', {'students': students, 'query': query})

def edit(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.tamil = request.POST['tamil']
        student.english = request.POST['english']
        student.maths = request.POST['maths']
        student.science = request.POST['science']
        student.social = request.POST['social']
        student.save()
        return redirect('results')
    return render(request, 'myapp/edit.html', {'student': student})

def delete(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('results')