# Generated by Django 3.2 on 2024-05-20 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MusicApp', '0007_auto_20240520_1036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id_album', models.AutoField(primary_key=True, serialize=False)),
                ('name_album', models.CharField(max_length=50)),
            ],
        ),
    ]