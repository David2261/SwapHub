# Generated by Django 4.2.7 on 2024-02-28 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_thing_images_thing_image_delete_thingimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent_id',
        ),
        migrations.RemoveField(
            model_name='thing',
            name='image',
        ),
        migrations.AddField(
            model_name='thing',
            name='images',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.image'),
        ),
    ]