from rject import rject
import os
from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.views import View
from django.views import generic

class ToDoView(generic.TemplateView):

    template_name = 'index.html'

    def content(self):
        r = rject.Rject(os.path.join('fe', 'App'))
        html = r.render()
        soup = BeautifulSoup(html, "html.parser")
        content = soup.prettify()
        return content
