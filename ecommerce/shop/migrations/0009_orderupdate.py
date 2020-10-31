# Generated by Django 3.0.6 on 2020-09-24 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_orders_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='orderupdate',
            fields=[
                ('updateid', models.AutoField(primary_key=True, serialize=False)),
                ('orderid', models.IntegerField(default='')),
                ('status', models.CharField(max_length=200)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]