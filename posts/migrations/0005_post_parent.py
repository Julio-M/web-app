# Generated by Django 3.2.9 on 2021-12-03 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20211203_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.post'),
        ),
    ]
