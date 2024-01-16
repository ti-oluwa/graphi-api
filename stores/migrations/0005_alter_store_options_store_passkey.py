# Generated by Django 5.0.1 on 2024-01-15 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_store_default_currency'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='store',
            options={'ordering': ('name', '-created_at')},
        ),
        migrations.AddField(
            model_name='store',
            name='passkey',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
