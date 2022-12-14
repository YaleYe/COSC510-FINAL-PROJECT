# Generated by Django 4.1.3 on 2022-11-26 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productID', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('category', models.CharField(choices=[('NFT', 'NFT'), ('BlockChain', 'BlockChain'), ('MetaVerse', 'MetaVerse'), ('Land', 'Land'), ('COOPERATION', 'COOPERATION'), ('Planet', 'Planet'), ('Vehicle', 'Vehicle'), ('Camera', 'Camera'), ('Lenses', 'Lenses'), ('Computer', 'Computer'), ('Collab', 'Collab')], max_length=20)),
                ('title', models.CharField(max_length=30)),
                ('image', models.ImageField(default=None, upload_to='')),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('currentHolder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='holder', to=settings.AUTH_USER_MODEL)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BiddingItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TransactionID', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('CurrentPrice', models.FloatField()),
                ('PlaceBidTime', models.DateTimeField(auto_now_add=True)),
                ('CurrentBidder', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ItemId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IHOB.product')),
            ],
        ),
    ]
