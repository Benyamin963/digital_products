from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE,blank=True, null=True)
    title = models.CharField(_('title'),max_length=100)
    description = models.TextField(_('description'),blank=True)
    avatar = models.ImageField(_('avatar'),upload_to='categories/',blank=True,null=True)
    is_enable = models.BooleanField(_('is enable'),default=True)
    created_time = models.DateTimeField(_('created time'),auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'),auto_now=True)
    class Meta:
        db_table = 'categories'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

class Product(models.Model):
    title = models.CharField(_('title'),max_length=100)
    description = models.TextField(_('description'),blank=True)
    avatar = models.ImageField(_('avatar'),upload_to='products/',blank=True,null=True)
    is_enable = models.BooleanField(_('is enable'),default=True)
    categories = models.ManyToManyField('Category',verbose_name=_('categories'),blank=True)
    created_time = models.DateTimeField(_('created time'),auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'),auto_now=True)
    class Meta:
        db_table = 'products'
        verbose_name = _('product')
        verbose_name_plural = _('products')
class File(models.Model):
    product = models.ForeignKey('Product',verbose_name=_('product'),on_delete=models.CASCADE)
    title = models.CharField(_('title'),max_length=100)
    file = models.FileField(_('file'),upload_to='files/%y/%m/%d/')
    is_enable = models.BooleanField(_('is enable'),default=True)
    created_time = models.DateTimeField(_('created time'),auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'),auto_now=True)
    class Meta:
        db_table = 'files'
        verbose_name = _('file')
        verbose_name_plural = _('files')