# Generated by Django 4.0.10 on 2024-06-03 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='News_letter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsletter_email', models.EmailField(max_length=100)),
            ],
        ),
    ]
