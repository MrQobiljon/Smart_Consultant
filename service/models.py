from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Header(models.Model):
    """Eng yuqoridagi logotiplarni matnini chiqarish uchun"""
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Logotip"
        verbose_name_plural = "Logotiplar"


class GalleryHeader(models.Model):
    """Header modeliga tegishli"""
    image = models.ImageField(upload_to='header/')
    header = models.ForeignKey(Header, on_delete=models.PROTECT)



class Service(models.Model):
    """Hizmat ko'rsatish turlari"""
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    logo = models.ImageField(upload_to='service/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Hizmat ko'rsatish turi"
        verbose_name_plural = "Hizmat ko'rsatish turlari"



class Category(models.Model):
    """Galereyadagi rasmlarni chiqarish uchun kategoriya"""
    title = models.CharField(max_length=155, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Katalog"
        verbose_name_plural = "Kataloglar"


class GalleryCategory(models.Model):
    """Kategoriya modeliga tegishli"""
    image = models.ImageField('category/')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)



class Blog(models.Model):
    """Bloglarni chiqarish"""
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    view = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Bloglar"



class Message(models.Model):
    """Foydalanuvchi habar yuborishi uchun model"""
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=25)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Xabar"
        verbose_name_plural = "Xabarlar"



class About(models.Model):
    """Kompaniya haqidagi ma'lumot uchun model"""
    about_us = models.TextField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.about_us

    class Meta:
        verbose_name = "Biz haqimizda"
        verbose_name_plural = "Biz haqimozda"


class EmailAbout(models.Model):
    """About modeli uchun"""
    email = models.EmailField()
    about = models.ForeignKey(About,on_delete=models.CASCADE)


class PhoneAbout(models.Model):
    """About modeli uchun"""
    phone = models.CharField(max_length=22)
    about = models.ForeignKey(About, on_delete=models.CASCADE)



class SocialSet(models.Model):
    """Itimoiy tarmoqlardagi accountlar uchun"""
    youtube = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    telegram = models.CharField(max_length=255, null=True, blank=True)