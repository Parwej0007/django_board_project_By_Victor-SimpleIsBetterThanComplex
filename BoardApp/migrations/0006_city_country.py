# Generated by Django 2.2.5 on 2019-12-19 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BoardApp', '0005_auto_20191216_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_country', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_city', models.CharField(blank=True, max_length=100)),
                ('population', models.PositiveIntegerField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='citys', related_query_name='city', to='BoardApp.Country')),
            ],
        ),
    ]
