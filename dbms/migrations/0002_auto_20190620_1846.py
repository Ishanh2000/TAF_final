# Generated by Django 2.2.2 on 2019-06-20 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='data',
            name='aadhar',
            field=models.CharField(default=0, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='password',
            field=models.CharField(default=0, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='residence',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='user_name',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='data',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]