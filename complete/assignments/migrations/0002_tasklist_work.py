# Generated by Django 2.1.3 on 2018-11-18 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20181118_1710'),
        ('assignments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasklist',
            name='work',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.Todolist'),
            preserve_default=False,
        ),
    ]
