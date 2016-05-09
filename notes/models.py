from django.conf import settings
from django.db import models

# Create your models here.

#工作分類
class Category(models.Model):
    name = models.CharField(max_length=30, blank=False)  #分類名稱

    def __str__(self):
        return self.name

#部門
class Department(models.Model):
    title = models.CharField(max_length=30, blank=False) #部門名稱

    def __str__(self):
        return self.title

#需求等級
class Reqlevel(models.Model):
    name = models.CharField(max_length=30, blank=False) #需求等級

    def __str__(self):
        return self.name


#處理方式
class Treat(models.Model):
    name = models.CharField(max_length=30, blank=False) #處理方式

    def __str__(self):
        return self.name

#需求申請單
class Document(models.Model):
    apply_date = models.DateField() #填單日期,簽核流程的關係,可能會和收件日期不一致
    category = models.ForeignKey( Category ) #需求分類
    apply_department = models.ForeignKey(Department) #申請部門
    apply_user = models.CharField(max_length=30, blank=False) #申請人員
    ext_number = models.DecimalField(max_digits=3, decimal_places=0) #分機號碼
    request_level = models.ForeignKey(Reqlevel) #需求等級
    request_descript = models.TextField(max_length=1024, blank=False) #需求描述

    #treat_method = models.ForeignKey(Treat) #處理方式
    #treat_descript = models.TextField(max_length=1024, blank=True) #處理過程說明
    create_at = models.DateTimeField( auto_now_add=True , auto_now=False) #建檔日期,收件日期
    last_update = models.DateTimeField( auto_now_add=False, auto_now=True ) #最後更新日期
    update_user = models.CharField( max_length=30, blank=True ) #更新者

class TreatDoc(models.Model):
    docs =  models.ForeignKey( Document ) #需求申請單
    treat_method = models.ForeignKey(Treat) #處理方式
    treat_descript = models.TextField(max_length=1024, blank=True) #處理過程說明

    create_at = models.DateTimeField( auto_now_add=True , auto_now=False) #建檔日期,收件日期
    last_update = models.DateTimeField( auto_now_add=False, auto_now=True ) #最後更新日期
    update_user = models.CharField(max_length=30,blank=True ) #更新者
