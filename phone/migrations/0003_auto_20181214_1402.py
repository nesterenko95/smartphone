# Generated by Django 2.1.4 on 2018-12-14 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0002_auto_20181214_0033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='phone',
        ),
        migrations.AddField(
            model_name='phone',
            name='image',
            field=models.ImageField(default='asd', upload_to=''),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
