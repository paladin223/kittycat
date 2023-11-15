from django.shortcuts import render

# from cats.models import Cat


def homepage(request):
    context = {}
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    print(num_visits)
    return render(request, "homepage/main.html", context)
