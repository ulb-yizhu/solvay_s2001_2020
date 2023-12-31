# Generated by Django 4.2.7 on 2023-11-19 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_ukraine', '0004_establishment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('number_of_person', models.IntegerField()),
                ('establishment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_ukraine.establishment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_ukraine.user')),
            ],
        ),
    ]
