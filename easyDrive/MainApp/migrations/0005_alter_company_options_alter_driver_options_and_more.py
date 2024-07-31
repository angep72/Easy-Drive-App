# Generated by Django 5.0.7 on 2024-07-14 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_alter_company_user_alter_driver_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='driver',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='driver',
            name='status',
            field=models.CharField(choices=[('hired', 'Hired'), ('available', 'Available'), ('off_duty', 'Off Duty')], default='available', max_length=10),
        ),
        migrations.AlterField(
            model_name='company',
            name='avatar',
            field=models.ImageField(default='avatar.jpg', null=True, upload_to='company/'),
        ),
        migrations.AlterField(
            model_name='company',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='avatar',
            field=models.ImageField(default='avatar.jpg', null=True, upload_to='driver/'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='category',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
