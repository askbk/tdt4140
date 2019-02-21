# Generated by Django 2.1.5 on 2019-02-21 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_auto_20190221_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Address'),
        ),
        migrations.AlterField(
            model_name='startup',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Address'),
        ),
    ]
