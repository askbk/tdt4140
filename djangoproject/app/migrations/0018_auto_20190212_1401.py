# Generated by Django 2.1.5 on 2019-02-12 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20190212_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='image',
            field=models.ImageField(default='no-image.png', upload_to='app/static/media/images/'),
        ),
    ]
