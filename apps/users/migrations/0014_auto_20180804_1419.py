# Generated by Django 2.0.2 on 2018-08-04 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20180804_1411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='danwei',
            old_name='zhuang_xie_gong',
            new_name='dan_wei_ming_cheng',
        ),
    ]