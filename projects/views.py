from django.shortcuts import render
from django.http import HttpResponse


projectsList = [
    {
        'id': '1',
        'title': "Ecommerce Website",
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': "Portfolio Website",
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '3',
        'title': "Social Network",
        'description': 'Fully functional ecommerce website'
    },

]

def projects(request):
    page = 'projects'
    number = 10 
    context = {'page':page, 'number':number, 'projects':projectsList}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    return render(request, 'projects/single-project.html')
