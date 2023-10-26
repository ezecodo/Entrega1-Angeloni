# Generated by Django 4.2.6 on 2023-10-26 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mensajeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='mensaje_original',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='respuestas', to='mensajeria.mensaje'),
        ),
    ]
