# Generated by Django 3.0.6 on 2020-06-07 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200505_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='duedate',
            field=models.DateField(verbose_name='期限'),
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='memo',
            field=models.TextField(verbose_name='メモ'),
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='priority',
            field=models.CharField(choices=[('danger', '高'), ('info', '中'), ('success', '低')], max_length=10, verbose_name='優先度'),
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='title',
            field=models.CharField(max_length=100, verbose_name='タイトル'),
        ),
    ]
