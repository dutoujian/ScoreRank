from django.db import models
# from db.base_model import BaseModel

# Create your models here.
class ClientInfo(models.Model):
    client_name=models.CharField(max_length=150,verbose_name='客户端名称')
    score=models.IntegerField(verbose_name='分数')
    create_time=models.DateTimeField(verbose_name='创建时间')
    update_time = models.DateTimeField(verbose_name='更新时间')
    is_valid = models.CharField(max_length=1, default=1, verbose_name='是否有效')

    class Meta:
        db_table = 'client_score'
        verbose_name = '分数信息'
        verbose_name_plural = verbose_name


