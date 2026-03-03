from django.shortcuts import render

def index_view(request):
    return render(request, 'core/index.html')

def about_view(request):
    return render(request, 'core/about.html')

def docs_view(request):
    return render(request, 'core/docs.html')

def demo_view(request):
    return render(request, 'core/demo.html')

def slides_view(request):
    return render(request, 'core/slides.html')

def resources_view(request):
    return render(request, 'core/resources.html')

def sitemap_view(request):
    return render(request, 'core/sitemap.html')
