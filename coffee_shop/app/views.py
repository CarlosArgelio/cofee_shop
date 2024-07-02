from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def my_view(req):
    car_list = [
        { "title": "BMW"},
        { "title": "Mazda"},
        { "title": "Chevrolet"},
    ]

    context = {
        "car_list": car_list
    }

    return render(req, "app/car_list.html", context)

class CarListView(TemplateView):
    template_name = "app/car_list.html"

    def get_context_data(self):
        car_list = [
            { "title": "BMW"},
            { "title": "Mazda"},
            { "title": "Chevrolet"},
        ]

        context = {
            "car_list": car_list
        }

        return context

def my_test_view(req, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse("")