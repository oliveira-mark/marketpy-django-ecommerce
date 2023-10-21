from django.shortcuts import render

def dashboard(request):
    title_page = "Dashboard"
    return render(request, 'dashboard/global/pages/dashboard.html', {'title_page': title_page})