from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import ServiceRequest, UserProfile
from django.http import HttpResponse
from .forms import ServiceRequestForm, ServiceRequestUpdateForm, UserProfileForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login

def home(request):
    if(request.user.is_authenticated):
        return redirect('customer_dashboard')
    return HttpResponse('Home page')

def custom_login(request):
    if request.user.is_authenticated:
        return redirect('customer_dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            print('User logged in')
            # Custom logic example: Remember me
            if not request.POST.get('remember_me'):
                request.session.set_expiry(0)  # Browser-length session
            
            # next_url = request.GET.get('next') or 'customer_dashboard'
            return redirect('customer_dashboard')
        else:
            # messages.error(request, 'Invalid credentials')
            return  HttpResponse('Invalid credentials')
    
    return render(request, 'registration/login.html')

def is_staff(user):
    return user.is_staff


def register(request):
    if request.method == 'POST':
        # Process form submission
        user_form = UserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            # Save user and profile
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            # Log user in
            login(request, user)
            return redirect('customer_dashboard')
    else:
        # Show empty forms for GET request
        user_form = UserCreationForm()
        profile_form = UserProfileForm()

    return render(request, 'registration/register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def customer_dashboard(request):
    requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'customer/dashboard.html', {'requests': requests})

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            req = form.save(commit=False)
            req.user = request.user
            req.save()
            return redirect('customer_dashboard')
    else:
        form = ServiceRequestForm()
    return render(request, 'customer/submit_request.html', {'form': form})

@user_passes_test(is_staff)
@login_required
def support_dashboard(request):
    requests = ServiceRequest.objects.all()
    status_filter = request.GET.get('status')
    if status_filter:
        requests = requests.filter(status=status_filter)
    return render(request, 'support/dashboard.html', {'requests': requests})

@user_passes_test(is_staff)
@login_required
def update_request(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    if request.method == 'POST':
        form = ServiceRequestUpdateForm(request.POST, instance=service_request)
        if form.is_valid():
            form.save()
            return redirect('support_dashboard')
    else:
        form = ServiceRequestUpdateForm(instance=service_request)
    return render(request, 'support/update_request.html', {'form': form, 'request': service_request})

