# Generated by Django 2.0.4 on 2018-04-11 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bolao', '0002_auto_20180411_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='estadio',
            name='cidadeEstadio',
            field=models.CharField(default=2, max_length=25),
            preserve_default=False,
        ),
    ]
