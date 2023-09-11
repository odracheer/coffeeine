from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Ricardo Palungguk Natama',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
