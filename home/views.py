from django.shortcuts import render

def home(request):
    is_logged_in = 'user_id' in request.session
    context = {'is_logged_in': is_logged_in}
    return render(request, 'home.html', context)
