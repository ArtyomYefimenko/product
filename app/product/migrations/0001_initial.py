# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=85, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438')),
                ('slug', models.SlugField(unique=True, max_length=85)),
                ('description', models.TextField(max_length=500, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438')),
            ],
            options={
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=85, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430')),
                ('slug', models.SlugField(unique=True, max_length=85)),
                ('description', models.TextField(max_length=500, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430')),
                ('price', models.FloatField(verbose_name='\u0426\u0435\u043d\u0430 \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='\u0418\u0437\u043c\u0435\u043d\u0435\u043d')),
                ('category', models.ForeignKey(related_name='category_products', verbose_name='\u0412 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438', to='product.Category')),
            ],
            options={
                'ordering': ('-created_at',),
                'verbose_name': '\u041f\u0440\u043e\u0434\u0443\u043a\u0442',
                'verbose_name_plural': '\u041f\u0440\u043e\u0434\u0443\u043a\u0442\u044b',
            },
        ),
    ]
