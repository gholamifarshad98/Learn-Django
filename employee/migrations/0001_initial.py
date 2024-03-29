# Generated by Django 4.0.10 on 2024-02-07 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('salary', models.IntegerField()),
                ('post', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
