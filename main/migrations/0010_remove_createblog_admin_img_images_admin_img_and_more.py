# Generated by Django 4.1.6 on 2023-09-05 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_createblog_admin_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createblog',
            name='admin_img',
        ),
        migrations.AddField(
            model_name='images',
            name='admin_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='images',
            name='logo_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='images',
            name='post_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
