# Generated by Django 2.2.4 on 2019-08-28 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('telweb', '0004_auto_20190828_0840'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filial', models.CharField(db_index=True, max_length=50, verbose_name='Филиал')),
            ],
            options={
                'verbose_name': 'Филиал',
                'verbose_name_plural': 'Филиалы',
                'ordering': ['filial'],
            },
        ),
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(db_index=True, max_length=4, verbose_name='Номер комнаты')),
                ('org', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='telweb.Organization', verbose_name='Филиал')),
            ],
            options={
                'verbose_name': 'Кабинет',
                'verbose_name_plural': 'Кабинеты',
                'ordering': ['room'],
            },
        ),
        migrations.AddField(
            model_name='intel',
            name='in_room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='telweb.Cabinet', verbose_name='Номер кабинета'),
        ),
    ]
