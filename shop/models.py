from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Product(models.Model):

    name = models.CharField(
        max_length=100, verbose_name=("أسم المنتج "), db_index=True)
    slug = models.SlugField(max_length=200, db_index=True,
                            unique=True, blank=True, null=True)
    descrip = RichTextUploadingField(
        verbose_name=("وصف المنتج"), blank=True, null=True)
    product_info = RichTextUploadingField(verbose_name=(
        "الوصف القصير"), default="", blank=True, null=True)
    pro_image = models.ImageField(
        upload_to='Produkten/', verbose_name=("صور"), blank=True, null=True)
    price = models.DecimalField(
        max_digits=7, decimal_places=0, verbose_name=("سعر المنتج"))
    Discountprice = models.DecimalField(
        max_digits=7, decimal_places=0, default="0", verbose_name=("سعر عند وجود خصم"))
    created = models.DateTimeField(verbose_name=("تاريخ الاضافة"))
    updated = models.DateTimeField(
        auto_now=True, verbose_name=("تاريخ الاضافة"))

    available = models.BooleanField(
        default=False, verbose_name=("توصيه مسيقا"))
    special = models.BooleanField(default=False, verbose_name=("خصم"))
    new = models.BooleanField(
        default=False, verbose_name=("وجود في سياره التوزيع"))

    class meta:
        index_together = (('id', 'slug'),)
        verbos_name = ('Product')
        verbos_name_plural = ('Products')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # [self.id,self.slug]) #args
        return reverse('ost:one_prodcut', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

class ProImag(models.Model):
    product = models.ForeignKey( Product, on_delete=models.CASCADE, verbose_name=("produktnamn"))
    image = models.ImageField(
        upload_to='Produkten/', default="0", blank=True, verbose_name=("produktbild"))

    def __str__(self):
        return str(self.product)

# class PlatsSalu(models.Model):
#     plats = RichTextUploadingField(verbose_name=("مناطق التوزيع"), blank=True, null=True)

    # def __str__(self):
    #     return str(self.plats)

class ProductReview(models.Model):
    product = models.ForeignKey(
        Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='reviews', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    stars = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)


class PlatsSalu(models.Model):
    stan = models.CharField(max_length=100 , verbose_name=("أسم المدينة "), db_index=True)
    adress = models.CharField(max_length=100, verbose_name=("العنوان "), db_index=True)

    map_plats = models.CharField(max_length=100, verbose_name=("رابط العنوان "), db_index=True)
    datom = models.DateField(
        verbose_name=("التاريخ"), null=True, blank=True)
    start_time = models.TimeField(
        auto_now=False, verbose_name=("ساعة البداء"))
    end_time = models.TimeField(
        auto_now=False, verbose_name=("ساعة المغادرة"))


    def __str__(self):
        return str(self.stan)


class PlatsReview(models.Model):
    # stan = models.ForeignKey(
    #     PlatsSalu, related_name='plat_reviews', null=True, on_delete=models.CASCADE)
    #     # stan = models.CharField(max_length=100, db_index=True)
    user = models.ForeignKey(
        User, related_name='plat_reviews', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.user)

        # def save(self, *args, **kwargs):
        #     if  self:
        #         self = (self. contentt)
        #     super(PlatsReview, self).save(*args, **kwargs)


class Home_images(models.Model):

    image_1 = models.ImageField(
        upload_to='Produkten/', default="0", blank=True, verbose_name=("الصورة الرئيسية الاولى"))
    image_2 = models.ImageField(
        upload_to='Produkten/', default="0", blank=True, verbose_name=("الصورة الرئيسية الثانيه"))
    image_3 = models.ImageField(
        upload_to='Produkten/', default="0", blank=True, verbose_name=("الصورة الرئيسية الثالثة"))

    def __str__(self):
        return str(self.image_1)


class Gallery(models.Model):
    gallery_image_1 = models.ImageField(
        upload_to='Produkten/', default="0", blank=True, verbose_name=("الصورة"))
    
    def __str__(self):
        return str(self.gallery_image_1)
