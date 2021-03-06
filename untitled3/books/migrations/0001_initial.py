# Generated by Django 2.0.5 on 2019-12-24 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='书籍名称')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击数')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='封面图片')),
                ('autor', models.CharField(max_length=12, verbose_name='作者')),
                ('book_desc', models.CharField(max_length=256, verbose_name='书籍介绍')),
            ],
            options={
                'verbose_name': '书籍列表',
                'verbose_name_plural': '书籍列表',
            },
        ),
    ]
