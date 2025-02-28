# Generated by Django 4.0.4 on 2022-05-30 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_1902', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('profile', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='seller/photos/')),
            ],
        ),
        migrations.RenameField(
            model_name='cloth',
            old_name='rating',
            new_name='price',
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('photo', models.ImageField(upload_to='product/photos/')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='App_1902.seller')),
            ],
        ),
    ]
