# Generated by Django 5.1.1 on 2024-09-29 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0002_alter_category_options_alter_tool_price_per_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
