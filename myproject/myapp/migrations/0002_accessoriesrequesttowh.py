# Generated by Django 4.2.3 on 2023-07-19 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessoriesRequestToWh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style_po_id', models.PositiveIntegerField()),
                ('style_po', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('request_qty', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=100)),
                ('request_by', models.CharField(blank=True, max_length=100, null=True)),
                ('accept_by', models.CharField(blank=True, max_length=100, null=True)),
                ('request_status', models.CharField(max_length=100)),
                ('request_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
