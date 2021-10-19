from django import forms
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection, BadHeaderError
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,  widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=100,  widget=forms.TextInput(attrs={'class': 'form-control'}))
    emailid = forms.EmailField(label='Your e-mail address',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    Telefon = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    #message = forms.CharField(required=False, widget=forms.Textarea(attrs={ 'class': 'form-control' }))
    subject = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter subject'}), required=True)
    message = forms.CharField(max_length=500, widget=forms.Textarea(
        attrs={'class': 'form-control'}))


# def contact(request):
#     submitted = False
#     if request.method == 'POST':
#         message_use = request.POST['message_use']
#         form = ContactForm(request.POST)

#         if form.is_valid():
#             cd = form.cleaned_data
#             # assert False
#             con = get_connection('django.core.mail.backends.smtp.EmailBackend')
#             send_mail(
#                 cd['message_use'],
#                 cd['message'],
#                 cd.get('email'),
#                 ['muslh17@gmail.com'],
#                 connection=con

#             )


#             return HttpResponseRedirect('/contact?submitted=True')
#     else:
#         form = ContactForm()
#         if 'submitted' in request.GET:
#             submitted = True

#     return render(request, 'KONTAKTA _OSS.html', {'form': form, 'submitted': submitted})

def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # form.save()
            # send_mail(subject, message[fname, lname, email, phonenumber, subject, message], sedner, recipient)

            subject = "Contact form inquiry"
            body = {
                'name': form.cleaned_data['name'],
                'last_name': form.cleaned_data['last_name'],
                'emailid': form.cleaned_data['emailid'],
                'Telefon': form.cleaned_data['Telefon'],
                'subject': form.cleaned_data['subject'],
                'message': form.cleaned_data['message'],
            }

            message = '\n'.join(body.values())

            sender = form.cleaned_data['emailid']
            recipient = ['bgfbdfgbg@gmail.com']

            try:
                send_mail(subject, message, sender,
                          recipient, fail_silently=True)

            except BadHeaderError:
                return HttpResponse("Ogiltig rubrik hittades.")

            messages.success(request, "Ditt svar har skickats framgångsrikt")
    context = {
        'form': form,
    }
    return render(request, 'KONTAKTA _OSS.html', context)
