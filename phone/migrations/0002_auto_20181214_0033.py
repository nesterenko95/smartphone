# Generated by Django 2.1.4 on 2018-12-14 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterModelOptions(
            name='phone',
            options={'verbose_name': 'Мобильный телефон', 'verbose_name_plural': 'Мобильный телефон'},
        ),
        migrations.AlterModelOptions(
            name='price',
            options={'verbose_name': 'Цена', 'verbose_name_plural': 'Цена'},
        ),
        migrations.AddField(
            model_name='image',
            name='phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phone.Phone'),
        ),
    ]
