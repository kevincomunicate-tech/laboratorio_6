from django.shortcuts import render
from django.http import HttpResponse # Puedes mantenerlo si aún usas HttpResponse en otras vistas

def home(request):
    context = {
        "welcome_message": "Explore learning resources and project ideas.",
    }
    return render(request, "pages/home.html", context)

def resources(request):
    context = {
        "resources": [
            {
                "title": "Python basics",
                "category": "Programming",
                "available": True,
            },
            {
                "title": "Git and GitHub",
                "category": "Collaboration",
                "available": True,
            },
            {
                "title": "Django models",
                "category": "Web development",
                "available": False,
            },
        ],
    }
    return render(request, "pages/resources.html", context)

# Si ya estás en este punto, también puedes dejar lista la vista 'about'
def about(request):
    context = {
        "purpose": "Practice URL routing, views, and templates.",
    }
    return render(request, "pages/about.html", context)
