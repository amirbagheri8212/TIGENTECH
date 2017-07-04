from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from accountmanagement.forms import SignUpForm
from django.contrib.auth.models import User
from accountmanagement.tokens import account_activation_token
from store.models import money

@login_required(login_url="login/")
def home(request):
    return render(request,"mainpage/indexs.html")
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data.get('username')
            user.raw_password = form.cleaned_data.get('password1')
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('accountmanagement/account_activation_email.html', {'user': user, 'domain': current_site.domain,
                                                                                           'uid': urlsafe_base64_encode(force_bytes(user.pk)),                                                          'token': account_activation_token.make_token(user), })
            Email_Subject = "Email Verification TIGEN TECH"
            Email_Message = message
            Email_From = settings.EMAIL_HOST_USER
            Email_ToList = [user.email]
            import smtplib
            send_mail(Email_Subject, Email_Message, "noreply@tigentech.com", Email_ToList, fail_silently=False)
            #send_mail(Email_Subject, Email_Message, Email_From, Email_ToList, fail_silently=False)
            #email = EmailMessage('Tigen Tech Email Confirmation',message,to = [user.email])
            #email.send()
            return redirect('account_activation_sent')

        return render_to_response('accountmanagement/signup.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'accountmanagement/signup.html', {'form': form})
def account_activation_sent(request):
    return render(request, 'accountmanagement/account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        Money = money(moneynow=0, Person=user)
        Money.save()
        user.save()
        login(request, user)
        return redirect('mainpage:homepage')
    else:
        return render(request, 'accountmanagement/account_activation_invalid.html')
