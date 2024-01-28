# Generated by Django 5.0.1 on 2024-01-28 08:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authApi', '0002_contentgroup_creation_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.CharField(choices=[('public', 'Public'), ('private', 'Private'), ('group', 'Group')], default='private', max_length=10)),
                ('media_type', models.CharField(max_length=10)),
                ('public', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, to='authApi.contentgroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
