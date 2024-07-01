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