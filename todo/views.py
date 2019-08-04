from rject import rject
from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.views import View
from django.views import generic


class ToDoView(View):

    def get(self, request, *args, **kwargs):

        r = rject.Rject('App')
        html = r.render()
        soup = BeautifulSoup(html, "html.parser")
        content = soup.prettify()
        return HttpResponse(content)
