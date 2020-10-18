# Generated by Django 3.0.5 on 2020-10-16 22:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('modSourcing', '0001_initial'),
        ('modParsing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='current_user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='activity',
            name='source_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='modSourcing.Source'),
        ),
        migrations.AddField(
            model_name='activity',
            name='status_code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='modParsing.StatusCode'),
        ),
    ]
