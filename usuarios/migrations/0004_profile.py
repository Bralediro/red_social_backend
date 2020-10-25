# Generated by Django 3.1.1 on 2020-10-25 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20201025_0938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fech_nac', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=50)),
                ('imagen', models.CharField(max_length=255)),
                ('titulo', models.CharField(max_length=255)),
                ('bio', models.CharField(max_length=255)),
                ('megusta', models.TextField(null=True)),
                ('no_megusta', models.TextField(null=True)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=25)),
                ('nivel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='usuarios.level')),
                ('pais', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='usuarios.paises')),
                ('sentimental', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='usuarios.sentimental')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='usuarios.usuarios')),
            ],
        ),
    ]
