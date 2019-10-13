# Generated by Django 2.2.6 on 2019-10-13 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('br_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('badgenumber', models.IntegerField(blank=True, db_column='badgeNumber', null=True)),
                ('firstname', models.CharField(db_column='firstName', max_length=45)),
                ('lastname', models.CharField(db_column='lastName', max_length=45)),
                ('city', models.CharField(blank=True, max_length=45, null=True)),
                ('numberstars', models.IntegerField(blank=True, db_column='numberStars', null=True)),
                ('profile_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'officer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('u_profile_id', models.IntegerField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(blank=True, db_column='firstName', max_length=45, null=True)),
                ('lastname', models.CharField(blank=True, db_column='lastName', max_length=45, null=True)),
                ('username', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Officers',
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='br_app.User')),
                ('stars', models.IntegerField()),
            ],
            options={
                'db_table': 'review',
                'managed': False,
            },
        ),
    ]
