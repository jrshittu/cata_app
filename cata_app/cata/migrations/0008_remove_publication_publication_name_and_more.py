# Generated by Django 4.2.3 on 2023-08-05 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cata', '0007_delete_article_delete_author_delete_edition_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='publication_name',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='publication_notes',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='publication_type',
        ),
    ]