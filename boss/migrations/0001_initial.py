# Generated by Django 4.1 on 2022-10-09 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('workArea', '0002_alter_work_area_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('salary', models.IntegerField()),
                ('phone', models.CharField(max_length=13)),
                ('dni', models.CharField(max_length=10)),
                ('image', models.ImageField(default='images.jpeg', upload_to='boss')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('boss_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workArea.work_area')),
            ],
        ),
    ]