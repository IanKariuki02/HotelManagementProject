# Generated by Django 4.2.7 on 2023-11-28 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=10, unique=True)),
                ('room_type', models.CharField(max_length=50)),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservation_number', models.AutoField(primary_key=True, serialize=False)),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('guest_name', models.CharField(max_length=255)),
                ('guest_email', models.EmailField(max_length=255)),
                ('guest_phone_number', models.CharField(max_length=20)),
                ('number_of_guests', models.IntegerField()),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.room')),
            ],
        ),
    ]
