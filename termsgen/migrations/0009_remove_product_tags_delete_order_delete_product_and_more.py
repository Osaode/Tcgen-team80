# Generated by Django 4.0.5 on 2022-08-15 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('termsgen', '0008_customer_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
