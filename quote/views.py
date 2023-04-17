from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm, QuoteForm, EmailPostForm, \
                    QuoteEditForm
from .models import Quote, Home
from django.core.mail import send_mail
from django.contrib.auth.models import User

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
        form = QuoteForm(request.POST, request.FILES)
        if form.is_valid():
            quote_request = form.save(commit=False)
            form.instance.requester = request.user
            quote_request.save()
            context = {'quote_request':quote_request}
            return render(request, 'quote/quote_submit_done.html', context)
    else:
        quote_request = QuoteForm() 
        context = {'quote_request':quote_request}
        return render(request, 'quote/quote_form.html', context)
    
@login_required(login_url='login')
def quote_edit(request):
    if request.method == 'POST':
        quote_form = QuoteEditForm(instance=request.quote,
                                  data=request.POST)
        if quote_form.is_valid():
            quote_form.save()
    else:
        quote_form = QuoteEditForm(instance=request.quote)
    context = {'quote_form':quote_form}
    return render(request, 'quote/quote_edit_form.html', context)
    
def contact_form_email_send(request):
    sent = False
    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            #Form Fields passed validation
            cd = form.cleaned_data
            email = f"{cd['email']}"
            subject = f"{cd['subject']}--from {cd['name']}"
            message = f"Name: {cd['name']}\nFrom: {email}\nMessage: \n{cd['message']}"
            send_mail(subject, message, 'hawaiianintucson@gmail.com', 
                      ['hawaiianintucson@gmail.com'])
            sent = True

    else:
        form = EmailPostForm()
    context = {'form': form, 'sent':sent}
    return render(request, "quote/contact.html", context)

@login_required(login_url='login')
def quotes_list(request):
    # if request.user_name.is_authenticated():
    if request.user.is_superuser:
        quotes = Quote.objects.all()
    else:
        quotes =  Quote.objects.filter(requester=request.user)
    
    
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
    text = Home.objects.all()
    context = {'section': 'home', 'text': text}
    return render(request, 'quote/home.html', context)


# def contact(request):
#     return render(request, 'quote/contact.html')

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

