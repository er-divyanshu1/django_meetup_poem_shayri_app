# Generated by Django 4.2.3 on 2023-08-13 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('reader_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('masssage', models.TextField()),
                ('userdate', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.RemoveField(
            model_name='post',
            name='url',
        ),
    ]
