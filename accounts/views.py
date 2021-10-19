from collections import UserDict
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate
from .models import Profile
from .forms import UserForm, ProfileForm, UserCreatForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template.context_processors import csrf
from django.utils import translation
from django.http.response import HttpResponse, HttpResponseRedirect


def signup(request
           ):
    if request.method == 'POST':
        form = UserCreatForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')

    else:
        form = UserCreatForm()

    context = {'form': form}
    return render(request, 'registration/Signup.html', context)


@login_required(login_url='/accounts/login/')
def profile(request, slug):
    profile = get_object_or_404(Profile, slug=slug)

    context = {'profile': profile}

    return render(request, 'accounts/profile.html', context)


def view_profile(request, pk=None):
    profile = get_object_or_404(Profile)
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user,
            'profile': profile,

            }
    return render(request, 'profile.html', args)


def selectlanguage1(request):
    if request.method == 'POST':  # check post
        cur_language = translation.get_language()
        lasturl = request.META.get('HTTP_REFERER')
        lang = request.POST['language']
        translation.activate(lang)
        request.session[translation.LANGUAGE_SESSION_KEY] = lang
        #return HttpResponse(lang)
        return HttpResponseRedirect("/"+lang)
