from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, ProImag, PlatsSalu, ProductReview, PlatsReview, Home_images, Gallery
from django.core.paginator import Paginator
from django.utils import translation
from django.utils.translation import gettext_lazy as _
from django.conf import settings

def all_prodcut(request):
    all_prodcut = Product.objects.all()

    imagess = Home_images.objects.all()
    products = Product.objects.filter(available=True)
    paginator = Paginator(all_prodcut, 16)
    page_number = request.GET.get('page')
    all_prodcut = paginator.get_page(page_number)
    # products = products.filter()
    gallery = Gallery.objects.all()
    plats = PlatsSalu.objects.all()

    if request.method == 'POST' and request.user.is_authenticated:
        content = request.POST.get('content', '')
        # stan = request.POST.get('all_prodcut_object_stan')
        # PlatsReview.stan = PlatsSalu.objects.filter(stan=stan)
        plat_reviews = PlatsReview.objects.create(
            user=request.user,  content=content)

        return redirect(".", id=id)

    # if request.method == 'POST' and request.user.is_authenticated:

    #     #stan = plats.objects.filter(stan=id)
    #     content = request.POST.get('content', '')
    #     #contentt = PlatsReview(contentt=request.POST)
    #     plat_review = PlatsReview.objects.create(
    #         stan=PlatsSalu.id, user=request.user,  content=content)

    #     return redirect(".", request)
    plat_reviews = PlatsReview.objects.all()
    con = {'all_prodcut': all_prodcut,
           'plats': plats,
           'products': products,
           'imagess': imagess,
           'plat_reviews': plat_reviews,
           'gallery': gallery,
           }
    return render(request, 'all_product.html', con)


def one_prodcut(request, slug):
    product = get_object_or_404(Product, slug=slug)  # available=True
    one_prodcut = Product.objects.get(slug=slug)
    images = ProImag.objects.filter(product=product)
    if request.method == 'POST' and request.user.is_authenticated:
        stars = request.POST.get('stars', 3)
        content = request.POST.get('content', '')

        review = ProductReview.objects.create(
            product=product, user=request.user, stars=stars, content=content)

        return redirect(".", slug=slug)
    con = {'one_prodcut': one_prodcut,
           'product': product,
           'images': images,

           }
    return render(request, 'one_product.html', con)


def selectlanguage(request):
    if request.method == 'POST':  # check post
        cur_language = translation.get_language()
        lasturl = request.META.get('HTTP_REFERER')
        lang = request.POST['language']
        translation.activate(lang)
        request.session[translation.LANGUAGE_SESSION_KEY] = lang
        #return HttpResponse(lang)
        return HttpResponseRedirect("/"+lang)



def about_us(request):
    return render(request, 'about.html')
