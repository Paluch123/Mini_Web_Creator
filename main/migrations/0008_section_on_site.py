# Generated by Django 3.2.7 on 2022-02-24 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_rename_enable_info_section_enable_info_tab'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='on_site',
            field=models.BooleanField(default=True),
        ),
    ]
