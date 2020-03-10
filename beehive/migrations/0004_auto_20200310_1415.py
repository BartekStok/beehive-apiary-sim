# Generated by Django 2.2.7 on 2020-03-10 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beehive', '0003_auto_20200310_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beefamily',
            name='bee_mother',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='beehive.BeeMother'),
        ),
        migrations.AlterField(
            model_name='beehive',
            name='type',
            field=models.CharField(choices=[('Wielkopolski', 'Wielkopolski'), ('Dadant', 'Dadant'), ('Warszawski', 'Warszawski'), ('Inny', 'Inny')], max_length=64),
        ),
        migrations.AlterField(
            model_name='beemother',
            name='bee_type',
            field=models.CharField(choices=[('Kraińska', 'Kraińska'), ('Kaukaska', 'Kaukaska'), ('CT13', 'CT13')], max_length=64),
        ),
    ]