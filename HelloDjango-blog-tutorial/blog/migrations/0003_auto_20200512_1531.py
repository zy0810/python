# Generated by Django 2.2.3 on 2020-05-12 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200326_0933'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_time'], 'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(),
        ),
    ]
