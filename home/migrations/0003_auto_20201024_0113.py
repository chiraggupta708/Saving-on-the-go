# Generated by Django 3.1.2 on 2020-10-23 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_addmoney_info_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='addmoney_info',
            name='updated_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='addmoney_info',
            name='Date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
