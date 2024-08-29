# Generated by Django 5.1 on 2024-08-29 08:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('subscribed_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('unsubscribed_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Newsletter Subscription',
                'verbose_name_plural': 'Newsletter Subscriptions',
            },
        ),
    ]
