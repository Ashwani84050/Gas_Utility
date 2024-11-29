from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required
def dashboard(request):
    requests = ServiceRequest.objects.filter(customer=request.user.customer)
    return render(request, 'customer_service/dashboard.html', {'requests': requests})

@login_required
def create_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user.customer
            service_request.save()
            return HttpResponseRedirect(reverse('dashboard'))
    else:
        form = ServiceRequestForm()
    return render(request, 'customer_service/create_request.html', {'form': form})

@login_required
def request_details(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk, customer=request.user.customer)
    return render(request, 'customer_service/request_details.html', {'service_request': service_request})

def index(request):
    return render(request, 'customer_service/index.html')