# Generated by Django 2.1.5 on 2019-04-04 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20190404_1412'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Uploaded image')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
    ]
