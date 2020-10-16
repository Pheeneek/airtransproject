# Generated by Django 3.1.2 on 2020-10-16 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('book_ref', models.AutoField(primary_key=True, serialize=False)),
                ('book_date', models.DateField()),
                ('total_amount', models.PositiveIntegerField()),
            ],
        ),
    ]