# Generated by Django 2.0.6 on 2018-11-23 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='payment', to='groups.Groups'),
        ),
    ]