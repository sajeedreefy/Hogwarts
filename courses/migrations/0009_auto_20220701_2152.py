# Generated by Django 3.1.4 on 2022-07-01 15:52

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20220630_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='video_url',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]