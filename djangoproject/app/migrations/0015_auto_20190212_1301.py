# Generated by Django 2.1.5 on 2019-02-12 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20190212_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='image',
            field=models.ImageField(default='images/no-image.png', upload_to='images/'),
        ),
    ]