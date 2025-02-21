# Generated by Django 4.2.16 on 2024-11-18 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eveonline', '0017_alliance_and_corp_names_are_not_unique'),
        ('hrapplications_two', '0007_auto_20200918_1412'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'permissions': (('approve_application', 'Can approve applications'), ('access_application', 'Can access HR application'))},
        ),
        migrations.CreateModel(
            name='ApplicationAcceptedFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('filter_corp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eveonline.evecorporationinfo')),
            ],
            options={
                'verbose_name': 'Smart Filter: Accepted Application for Corp',
                'verbose_name_plural': 'Smart Filter: Accepted Application for Corp',
            },
        ),
    ]
