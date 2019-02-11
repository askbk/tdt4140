# Generated by Django 2.1.5 on 2019-02-10 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20190211_0025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
            ],
        ),
        migrations.RemoveField(
            model_name='startup',
            name='phase',
        ),
        migrations.AddField(
            model_name='startup',
            name='phase',
            field=models.ManyToManyField(blank=True, to='app.Phase'),
        ),
    ]
