# Generated by Django 3.2.8 on 2021-12-08 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dokumen',
            fields=[
                ('kd_dokumen', models.IntegerField(primary_key=True, serialize=False)),
                ('nama_dokumen', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='file/')),
            ],
        ),
    ]
