# Generated by Django 4.1.6 on 2023-09-06 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_images_post_img_createblog_post_img'),
    ]

    operations = [
        migrations.DeleteModel(
            name='images',
        ),
        migrations.AddField(
            model_name='createblog',
            name='admin_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='createblog',
            name='logo_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
