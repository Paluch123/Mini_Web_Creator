# Generated by Django 3.2.7 on 2022-02-24 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_section_on_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='text',
            field=models.TextField(blank=True, max_length=1024),
        ),
    ]
