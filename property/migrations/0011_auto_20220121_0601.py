# Generated by Django 2.2.24 on 2022-01-21 03:01

from django.db import migrations, models


def create_relations(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for owner in Owner.objects.all():
        flats = Flat.objects.filter(owner=owner.name)
        owner.flats.set(flats)
        print(flats)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20220118_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='owner',
            field=models.CharField(db_index=True, max_length=200, verbose_name='ФИО владельца'),
        ),
        migrations.RunPython(create_relations),
    ]
