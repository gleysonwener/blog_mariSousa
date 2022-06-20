from django.shortcuts import render

def principal(request):
    template_name = 'home/principal.html'
    context = {}
    return render(request, template_name, context)
