from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306275935',
        'name': 'Alpha Sutha Media',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
