# Generated by Django 4.2.3 on 2023-08-13 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_category_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('masssage', models.TextField()),
                ('userdate', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
