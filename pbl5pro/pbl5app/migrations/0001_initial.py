# Generated by Django 4.1.7 on 2023-04-21 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(max_length=5)),
                ('password', models.CharField(max_length=255)),
                ('fullname', models.CharField(blank=True, max_length=255, null=True)),
                ('url_video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]