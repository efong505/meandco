from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm, QuoteForm, EmailPostForm, \
                    QuoteEditForm
from .models import Quote, Home
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

def quote_edit(request, quote_id):
    # quote = get_object_or_404(Quote, pk=id)
    sampleadminuser = User.objects.get(username="sampleadminuser")

    if request.user == sampleadminuser:
        quote = Quote.objects.get(pk=quote_id)
        quote_edit_form = QuoteEditForm(instance=quote)
        if request.method == 'POST':
            quote_edit_form = QuoteEditForm(request.POST, request.FILES, instance=quote)
            if quote_edit_form.is_valid():
                quote_edit_form.save()
                return redirect('quotes_list')   
        context = {'quote_edit_form':quote_edit_form}
        return render(request, 'quote/quote_edit_form.html', context)

    elif request.user.is_superuser:
        quote = Quote.objects.get(pk=quote_id)
        quote_edit_form = QuoteEditForm(instance=quote)
        if request.method == 'POST':
            quote_edit_form = QuoteEditForm(request.POST, request.FILES, instance=quote)
            if quote_edit_form.is_valid():
                quote_edit_form.save()
                return redirect('quotes_list')   
        context = {'quote_edit_form':quote_edit_form}
        return render(request, 'quote/quote_edit_form.html', context)
    else:
        return redirect('home')
    
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
            message = f"Name: {cd['name']}\nFrom: {email}\n<b>Message:</b> \n{cd['message']}"
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
    sampleadminuser = User.objects.get(username="sampleadminuser")
    if request.user == sampleadminuser:
        quotes = Quote.objects.all()
    elif request.user.is_superuser:
        quotes = Quote.objects.all()
    else:
        quotes =  Quote.objects.filter(requester=request.user)
    
    paginator = Paginator(quotes, 4)
    page_number = request.GET.get('page', 1)
    page_range = paginator.get_elided_page_range(number=page_number)
    try:
        quotes = paginator.page(page_number)
    except PageNotAnInteger:
        # if page not an integer server first page
        quotes = paginator.page(1)
    except EmptyPage:
        # if page_number is out of range deliver last page of results
        quotes = paginator.page(paginator.num_pages)
    context = {'quotes':quotes,'quotes':quotes}
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

