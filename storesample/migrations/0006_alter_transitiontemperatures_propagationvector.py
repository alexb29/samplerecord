# Generated by Django 3.2.12 on 2022-02-16 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storesample', '0005_auto_20220216_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transitiontemperatures',
            name='PropagationVector',
            field=models.JSONField(blank=True, default={'K1': '[1/2,1/2,1/2]'}, null=True, verbose_name='Propagation Vector'),
        ),
    ]
