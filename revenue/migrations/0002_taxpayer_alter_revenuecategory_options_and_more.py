# Generated by Django 4.2.4 on 2023-08-08 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revenue', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaxPayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Business name or Personal name', max_length=200)),
                ('address', models.TextField()),
                ('tin', models.CharField(help_text='Tax Identification Number', max_length=20, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Tax Payers',
                'ordering': ['-created'],
            },
        ),
        migrations.AlterModelOptions(
            name='revenuecategory',
            options={'ordering': ['-created'], 'verbose_name_plural': 'Revenue Categories'},
        ),
        migrations.AlterModelOptions(
            name='revenuesource',
            options={'ordering': ['-created'], 'verbose_name_plural': 'Revenue Sources'},
        ),
    ]
