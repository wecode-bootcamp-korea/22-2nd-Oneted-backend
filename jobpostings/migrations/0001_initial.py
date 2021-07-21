# Generated by Django 3.2.5 on 2021-07-21 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('description', models.TextField()),
                ('employee_count', models.IntegerField()),
                ('coordinate', models.JSONField()),
            ],
            options={
                'db_table': 'companies',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 'countries',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'jobs',
            },
        ),
        migrations.CreateModel(
            name='JobGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 'job_groups',
            },
        ),
        migrations.CreateModel(
            name='JobPostings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('image_url', models.URLField(max_length=3000, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='job_posting', to='jobpostings.company')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='job_posting', to='jobpostings.job')),
            ],
            options={
                'db_table': 'job_postings',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='TagCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
            ],
            options={
                'db_table': 'tag_categories',
            },
        ),
        migrations.CreateModel(
            name='TagJobPosting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_posting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobpostings.jobpostings')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobpostings.tag')),
            ],
            options={
                'db_table': 'tags_job_postings',
                'unique_together': {('tag', 'job_posting')},
            },
        ),
        migrations.AddField(
            model_name='tag',
            name='tag_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='jobpostings.tagcategory'),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='region', to='jobpostings.country')),
            ],
            options={
                'db_table': 'regions',
            },
        ),
        migrations.AddField(
            model_name='jobpostings',
            name='tags',
            field=models.ManyToManyField(related_name='job_posting', through='jobpostings.TagJobPosting', to='jobpostings.Tag'),
        ),
        migrations.AddField(
            model_name='job',
            name='job_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job', to='jobpostings.jobgroup'),
        ),
        migrations.AddField(
            model_name='company',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='jobpostings.region'),
        ),
    ]