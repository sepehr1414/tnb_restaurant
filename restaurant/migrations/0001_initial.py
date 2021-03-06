# Generated by Django 3.2.5 on 2021-07-18 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('established', models.DateField(blank=True)),
                ('grade', models.IntegerField()),
                ('city', models.CharField(max_length=500)),
                ('address', models.TextField()),
            ],
            options={
                'ordering': ['-grade'],
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('grade', models.IntegerField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('description', models.TextField(blank=True, null=True)),
                ('food_type', models.CharField(choices=[('SA', 'salad'), ('BE', 'beverages'), ('DE', 'desert'), ('MC', 'main course'), ('PG', 'pish_ghaza')], max_length=2)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant')),
            ],
            options={
                'ordering': ['-grade'],
            },
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.food')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
