# Generated by Django 4.0 on 2022-09-25 22:01

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=30)),
                ('created', models.DateTimeField()),
                ('last_modified', models.DateTimeField()),
                ('difficulty_rating', models.IntegerField(choices=[1, 2, 3])),
                ('problem_description', models.BinaryField()),
                ('hints', models.BinaryField()),
                ('solution', models.BinaryField()),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
