# Generated by Django 3.0.4 on 2020-07-02 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
    ]
