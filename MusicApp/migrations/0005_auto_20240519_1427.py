# Generated by Django 3.2 on 2024-05-19 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MusicApp', '0004_auto_20240518_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id_role', models.AutoField(primary_key=True, serialize=False)),
                ('name_role', models.CharField(choices=[('USER', 'User'), ('COMPOSER', 'Composer')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id_singer', models.AutoField(primary_key=True, serialize=False)),
                ('name_singer', models.CharField(max_length=200)),
                ('phone_singer', models.CharField(max_length=20)),
                ('email_singer', models.CharField(max_length=50)),
                ('genre_singer', models.CharField(max_length=50)),
                ('sex_singer', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id_tran', models.AutoField(primary_key=True, serialize=False)),
                ('price_tran', models.FloatField(default=0)),
                ('type_tran', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('name_user', models.CharField(max_length=200)),
                ('user', models.CharField(max_length=200)),
                ('pass_user', models.CharField(max_length=200)),
                ('phone_user', models.CharField(max_length=20)),
                ('email_user', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id_vote', models.AutoField(primary_key=True, serialize=False)),
                ('comment_vote', models.CharField(max_length=50)),
                ('report_vote', models.CharField(max_length=50)),
                ('num_vote', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='music',
            old_name='image',
            new_name='image_music',
        ),
        migrations.RenameField(
            model_name='music',
            old_name='name_singer',
            new_name='name_singer_music',
        ),
        migrations.RenameField(
            model_name='music',
            old_name='release_year',
            new_name='release_year_music',
        ),
        migrations.RemoveField(
            model_name='music',
            name='genre',
        ),
        migrations.AddField(
            model_name='music',
            name='genre_music',
            field=models.CharField(choices=[('POP', 'Pop'), ('ROCK', 'Rock'), ('JAZZ', 'Jazz'), ('CLASSICAL', 'Classical'), ('HIPHOP', 'Hip-Hop'), ('REMIX', 'Remix'), ('ROMANCE', 'Romance'), ('BOLERO', 'Bolero')], default='Pop', max_length=100),
        ),
        migrations.AddField(
            model_name='music',
            name='price_music',
            field=models.FloatField(default=0),
        ),
    ]
