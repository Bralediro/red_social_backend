# Generated by Django 3.1.1 on 2020-10-25 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=255)),
                ('nivel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='usuarios.level')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='usuarios.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descripcion', models.TextField(null=True)),
                ('nivel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='usuarios.level')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='usuarios.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=255)),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='usuarios.album')),
                ('nivel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='usuarios.level')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='usuarios.usuarios')),
            ],
        ),
    ]
