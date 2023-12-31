# Generated by Django 4.2.3 on 2023-08-05 11:03

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.functions.text
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cata', '0002_article_author_edition_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_id',
        ),
        migrations.RemoveField(
            model_name='article',
            name='title',
        ),
        migrations.RemoveField(
            model_name='author',
            name='author_id',
        ),
        migrations.RemoveField(
            model_name='edition',
            name='edition_id',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='tag_id',
        ),
        migrations.AddField(
            model_name='article',
            name='article_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Article Name'),
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ManyToManyField(blank=True, to='cata.author'),
        ),
        migrations.AddField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='article',
            name='edition',
            field=models.ManyToManyField(blank=True, to='cata.edition'),
        ),
        migrations.AddField(
            model_name='article',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='article',
            name='notes',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Notes'),
        ),
        migrations.AddField(
            model_name='article',
            name='summary',
            field=models.CharField(blank=True, max_length=500, verbose_name='Summary'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(blank=True, to='cata.tag'),
        ),
        migrations.AddField(
            model_name='author',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.CharField(blank=True, max_length=200, verbose_name='Notes'),
        ),
        migrations.AddField(
            model_name='author',
            name='tag',
            field=models.ManyToManyField(blank=True, to='cata.tag'),
        ),
        migrations.AddField(
            model_name='edition',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='edition',
            name='publication',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='cata.publication'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='edition',
            name='publication_date',
            field=models.DateField(blank=True, default=0, verbose_name='Publication Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='tag_descriptor',
            field=models.CharField(blank=True, max_length=200, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='article',
            name='keywords',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Keywords'),
        ),
        migrations.AlterField(
            model_name='author',
            name='author_name',
            field=models.CharField(max_length=200, verbose_name="Author's Name"),
        ),
        migrations.AlterField(
            model_name='edition',
            name='edition_name',
            field=models.CharField(max_length=200, verbose_name='Name of Edition'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='publication_name',
            field=models.CharField(max_length=200, verbose_name="Publication's Name"),
        ),
        migrations.AlterField(
            model_name='publication',
            name='publication_notes',
            field=models.CharField(blank=True, max_length=200, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(max_length=20, verbose_name='Tag'),
        ),
        migrations.AddConstraint(
            model_name='tag',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('tag_name'), name='tag_name_unique'),
        ),
    ]
