# Generated by Django 2.2.16 on 2022-10-30 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_image'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_subscription',
        ),
    ]
