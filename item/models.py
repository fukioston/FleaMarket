from django.db import models


# Create your models here.
class Items(models.Model):
    gname = models.CharField(verbose_name="商品名", max_length=1000)
    userid = models.IntegerField(verbose_name="用户id")
    price = models.DecimalField(verbose_name="价格", max_digits=5, decimal_places=2)
    intro_txt = models.CharField(verbose_name="介绍文本", max_length=1000)
    img_index = models.CharField(verbose_name="图片路径", max_length=100)
    phone = models.CharField(verbose_name="电话号码", max_length=100)