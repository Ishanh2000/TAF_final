# Generated by Django 2.2.2 on 2019-06-26 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbms', '0012_auto_20190626_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='accepted',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False'), ('Pending', 'Pending')], default='P', max_length=7),
        ),
    ]