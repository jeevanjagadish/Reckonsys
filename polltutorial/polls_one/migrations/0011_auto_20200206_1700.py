# Generated by Django 3.0.2 on 2020-02-06 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls_one', '0010_auto_20200206_1658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='client_num',
            new_name='client_id',
        ),
    ]
