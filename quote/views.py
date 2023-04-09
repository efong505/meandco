from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm, QuoteForm
from .models import Quote

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'],)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authentication successfull!')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'quote/login.html', context)

@login_required(login_url='login')
def quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote_request = form.save(commit=False)
            quote_request.save()
            context = {'quote_request':quote_request}
            return render(request, 'quote/quote_submit_done.html', context)
    else:
        quote_request = QuoteForm() 
        context = {'quote_request':quote_request}
        return render(request, 'quote/quote_form.html', context)

@login_required(login_url='login')
def quotes_list(request):
    quotes =  Quote.objects.all()
    context = {'quotes':quotes}
    return render(request, 'quote/quotes_list.html', context)

@login_required(login_url='login')
def quote_detail(request, quote_id):
    # quote = Quote.objects.get(pk=quote_detail)
    
    quote = get_object_or_404(Quote, pk=quote_id)
    context = {'quote': quote}
    return render(request, 'quote/quote_detail.html', context)

# @login_required()
def home(request):
    context = {'section': 'home'}
    return render(request, 'quote/home.html', context)

@login_required(login_url='login')
def contact(request):
    return render(request, 'quote/contact.html')

# Register account
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Customer.objects.create(user=new_user)
            return render(request,
                          'quote/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'quote/register.html',
                  {'user_form': user_form})