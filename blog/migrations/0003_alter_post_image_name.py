# Generated by Django 3.2.6 on 2021-10-13 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_name',
            field=models.ImageField(null=True, upload_to='posts'),
        ),
    ]
