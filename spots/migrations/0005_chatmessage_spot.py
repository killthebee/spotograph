# Generated by Django 3.0.3 on 2020-11-27 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spots', '0004_auto_20201127_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='spot',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='spots.Spot', verbose_name='Спот'),
            preserve_default=False,
        ),
    ]
