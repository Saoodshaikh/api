# Generated by Django 4.0.7 on 2022-09-12 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('about', models.TextField()),
                ('position', models.CharField(choices=[('manager', 'manager'), ('software developer', 'sd'), ('project leader', 'pd')], max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
        ),
    ]
