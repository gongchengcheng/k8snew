# Generated by Django 2.0.2 on 2018-08-03 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20180802_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='GongShangXinXi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gong_shang_ming_chen', models.CharField(max_length=200, verbose_name='供商名称')),
                ('lian_xi_ren', models.CharField(max_length=200, verbose_name='联系人')),
                ('lian_xi_dian_hua', models.CharField(max_length=200, verbose_name='联系电话')),
                ('lian_xi_di_zhi', models.CharField(max_length=200, verbose_name='联系地址')),
                ('bei_zhu', models.CharField(max_length=200, verbose_name='备注')),
            ],
        ),
        migrations.CreateModel(
            name='ke_hu_xin_xi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ke_hu_bian_hao', models.CharField(max_length=200, verbose_name='客户编号')),
                ('qu_yu', models.CharField(max_length=200, verbose_name='区域')),
                ('ke_hu_ming_chen', models.CharField(max_length=200, verbose_name='客户名称')),
                ('fu_ze_ren', models.CharField(max_length=200, verbose_name='负责人')),
                ('fu_ze_dian_hua', models.CharField(max_length=200, verbose_name='负责电话')),
                ('tiao_liao_yuan', models.CharField(max_length=200, verbose_name='调料员')),
                ('dian_hua', models.CharField(max_length=200, verbose_name='电话')),
                ('di_zhi', models.CharField(max_length=200, verbose_name='地址')),
                ('ye_wu', models.CharField(max_length=200, verbose_name='业务')),
                ('xin_yong_e_du', models.CharField(max_length=200, verbose_name='信用额度')),
                ('bei_zhu', models.CharField(max_length=200, verbose_name='备注')),
            ],
        ),
        migrations.CreateModel(
            name='ShuiNiXinXi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shui_ni_bian_hao', models.CharField(max_length=200, verbose_name='水泥编号')),
                ('chang_jia', models.CharField(max_length=200, verbose_name='厂家')),
                ('pin_pai', models.CharField(max_length=200, verbose_name='品牌')),
                ('xing_hao', models.CharField(max_length=200, verbose_name='型号')),
                ('gui_ge', models.CharField(max_length=200, verbose_name='规格')),
                ('bei_zhu', models.CharField(max_length=200, verbose_name='备注')),
            ],
        ),
        migrations.CreateModel(
            name='zhuang_xie_gong_xin_xi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zhuang_xie_gong', models.CharField(max_length=200, verbose_name='装卸工')),
                ('dianhua1', models.CharField(max_length=200, verbose_name='联系电话1')),
                ('dianhua2', models.CharField(max_length=200, verbose_name='联系电话2')),
                ('bei_zhu', models.CharField(max_length=200, verbose_name='备注')),
            ],
        ),
    ]