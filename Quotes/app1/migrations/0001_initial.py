# Generated by Django 4.2.3 on 2023-08-11 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='Hindi Jokes', max_length=150)),
                ('decription', models.TextField()),
                ('url', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='categortImage')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('Content', models.TextField()),
                ('url', models.CharField(max_length=150)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.category')),
            ],
        ),
    ]
