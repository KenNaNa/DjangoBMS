from django.db import models


class Publish(models.Model):
    # 出版社
    name = models.CharField(max_length=32)
    email = models.EmailField()


class AuhtorDetail(models.Model):
    # 作者简介
    addr = models.CharField(max_length=32)
    email = models.EmailField()


class Author(models.Model):
    # 作者
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    detail = models.OneToOneField('AuhtorDetail')


class Book(models.Model):
    # 书籍
    title = models.CharField(max_length=32)
    publishDate = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)  # 最大 999.99
    publish = models.ForeignKey('Publish')  # 一对多
    authors = models.ManyToManyField('Author')  # 多对多
