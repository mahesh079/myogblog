# Generated by Django 3.0.6 on 2020-10-30 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogcomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('email', models.CharField(default='', max_length=40)),
                ('phone', models.CharField(default='', max_length=50)),
                ('message', models.CharField(default='', max_length=500)),
            ],
        ),
    ]