# Generated by Django 4.0.2 on 2023-04-26 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_meat_finalprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='FMCGBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='fmcg',
            name='Brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dashboard.fmcgbrand'),
            preserve_default=False,
        ),
    ]
