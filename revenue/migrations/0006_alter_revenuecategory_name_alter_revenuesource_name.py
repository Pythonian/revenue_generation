# Generated by Django 4.2.4 on 2023-08-09 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revenue', '0005_alter_revenuetransaction_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revenuecategory',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='revenuesource',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
