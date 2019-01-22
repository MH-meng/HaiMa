from django.db import models


class News(models.Model):
    title = models.CharField(max_length=32, verbose_name='标题')
    content = models.TextField(verbose_name='文章内容', )
    introduction = models.CharField(max_length=100, verbose_name='引言', )
    time = models.DateTimeField(verbose_name='创建实时间')
    author = models.CharField(max_length=32)
    status = models.CharField(max_length=2, default='0')

    class Meta:
        db_table = 'News'
        verbose_name_plural = '新闻'

    def __str__(self):
        return self.title



class Price(models.Model):
    departure = models.CharField(verbose_name='出发地', max_length=32)
    destination = models.CharField(verbose_name='目的地',max_length=32)
    status_choice = (
        (0, '下线'),
        (1, '上线')
    )
    status = models.IntegerField(verbose_name='状态', choices=status_choice, default=1)
    type = models.CharField(verbose_name='车辆类型',max_length=64)
    price = models.CharField(verbose_name='价格', max_length=255)
    time = models.DateTimeField(verbose_name='时间')
    content = models.CharField(verbose_name='货物介绍', max_length=90)
    author = models.CharField(max_length=32, default='海马')


    class Meta:
        db_table = 'Price'
        verbose_name_plural = '求车'
        ordering = ['-time']

    def __str__(self):
        return self.author

