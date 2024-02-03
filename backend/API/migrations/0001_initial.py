# Generated by Django 4.2.7 on 2024-02-01 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dialog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_on', models.DateTimeField()),
                ('user_A_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dialog_user_A', to=settings.AUTH_USER_MODEL)),
                ('user_B_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dialog_user_B', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('rating', models.IntegerField(null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user_side', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=175)),
            ],
        ),
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('images', models.ImageField(upload_to='../media/images')),
                ('category_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.category')),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.location')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('closed_on', models.DateTimeField()),
                ('feedback_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.feedback')),
                ('participant_A_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trade_user_A', to=settings.AUTH_USER_MODEL)),
                ('participant_B_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trade_user_B', to=settings.AUTH_USER_MODEL)),
                ('thing_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.thing')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('dialog_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dialog')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
