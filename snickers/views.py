from django.views.generic import TemplateView


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'    

class TestView(TemplateView):
    template_name = 'test.html'    