# Generated by Django 4.1.6 on 2023-09-05 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_createblog_admin_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createblog',
            name='admin_img',
            field=models.ImageField(blank=True, upload_to='', verbose_name='admin_img'),
        ),
    ]
