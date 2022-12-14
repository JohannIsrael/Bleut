# Generated by Django 4.1.3 on 2022-12-12 02:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignupUser',
            fields=[
                ('id_user_django', models.OneToOneField(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cel', models.CharField(max_length=10)),
                ('imagen', models.ImageField(default='static/assets/user/25profile_default.png', null=True, upload_to='static/assets/user/')),
                ('ciudad', models.CharField(max_length=100, null=True)),
                ('calle', models.CharField(max_length=100, null=True)),
                ('num', models.IntegerField(null=True)),
                ('Es_trabajador', models.BooleanField(default=False)),
            ],
        ),
    ]
