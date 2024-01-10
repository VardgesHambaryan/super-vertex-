from django.db import models
from django.utils.html import format_html


class Blog(models.Model):
    img = models.ImageField('Blog Image', upload_to='media')
    title = models.CharField('Blog Title', max_length = 50)
    text = models.TextField('Blog Text')
    post_date = models.DateField('Blog Post Date')

    def __str__(self) -> str:
        return self.title
    
    def img_preview(self):
        return format_html(f'<img src="{self.img.url}" style="width : 50px"/>')

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

class OurServices(models.Model):

    text1 = models.TextField('First Text')
    text2 = models.TextField('Second Text')

    def __str__(self) -> str:
        return 'Services'
    
    class Meta:
        verbose_name = "OurServices"
        verbose_name_plural = "OurServices"


class Gallery(models.Model):
    img_small = models.ImageField('Small Image', upload_to='media')
    img_large = models.ImageField('Large Image', upload_to='media')
    title = models.CharField('Title', max_length = 30)
    name = models.CharField('Name', max_length = 30)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"
  


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "ContactUs"
        verbose_name_plural = "ContactUs"
  

class HomeBg(models.Model):
    img1 = models.ImageField('First Image' , upload_to='media')
    img2 = models.ImageField('Second Image' , upload_to='media')
    img3 = models.ImageField('Third Image' , upload_to='media')
    img4 = models.ImageField('Forth Image' , upload_to='media')


    def __str__(self):
        return "BackGround Images"

    class Meta:
        verbose_name = "BackGround Image"
        verbose_name_plural = "BackGround Images"


