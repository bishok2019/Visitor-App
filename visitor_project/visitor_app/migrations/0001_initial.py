# Generated by Django 5.1.6 on 2025-02-07 08:48

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('meeting_date', models.DateField()),
                ('meeting_time', models.TimeField()),
                ('reason', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('visiting_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
