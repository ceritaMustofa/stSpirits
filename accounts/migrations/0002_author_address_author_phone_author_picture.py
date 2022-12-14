# Generated by Django 4.1.3 on 2022-11-24 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='author',
            name='phone',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='author',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
