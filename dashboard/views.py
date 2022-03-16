from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
  # TODO Figure out a way to serve this file and have the bundle load
  return render(request, 'fe_dashboard.html')
