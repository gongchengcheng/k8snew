# Generated by Django 2.0.2 on 2018-08-04 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20180804_1322'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ZhuangXieGongXinXi',
            new_name='ZhuangXieGong',
        ),
        migrations.RenameField(
            model_name='cheliang',
            old_name='zhuang_xie_gong',
            new_name='che_hao',
        ),
    ]
