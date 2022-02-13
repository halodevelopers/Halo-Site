# Generated by Django 4.0.2 on 2022-02-13 14:35

from django.db import migrations
import mapbox_location_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=mapbox_location_field.models.LocationField(blank=True, map_attrs={'center': (17.031645, 51.106715), 'style': 'mapbox://styles/mightysharky/cjwgnjzr004bu1dnpw8kzxa72'}, null=True),
        ),
    ]