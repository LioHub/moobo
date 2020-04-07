<<<<<<< HEAD
# Generated by Django 2.2.7 on 2020-04-07 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('designer', '0003_auto_20200324_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('quantity_of_workers', models.IntegerField(default=0, verbose_name='Количество работников')),
                ('job', models.CharField(choices=[('Исполнитель', 'Исполнитель')], max_length=20, verbose_name='Профессия')),
                ('city', models.CharField(blank=True, max_length=30, verbose_name='Город')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.AlterField(
            model_name='project',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель'),
        ),
        migrations.AlterField(
            model_name='statement',
            name='application_room',
            field=models.CharField(choices=[('Все комнаты', 'Все комнаты'), ('Зал', 'Зал'), ('Гостинная', 'Гостинная'), ('Прихожая', 'Прихожая'), ('Ванная', 'Ванная'), ('Санузел', 'Санузел'), ('Гостевой санузел', 'Гостевой санузел'), ('Гостеванная ванная', 'Гостеванная ванная'), ('Главная ванная', 'Главная ванная'), ('Гардероб', 'Гардероб'), ('Спальня', 'Спальня'), ('Главная спальня', 'Главная спальня'), ('Детская', 'Детская'), ('Балкон', 'Балкон'), ('Лоджия', 'Лоджия'), ('Кабинет', 'Кабинет'), ('Кухня', 'Кухня'), ('Летняя кухня', 'Летняя кухня'), ('Котельная', 'Котельная'), ('Хозяйственной помещение', 'Хозяйственной помещение'), ('Прачечная', 'Прачечная')], default='', max_length=25, verbose_name='Комнаты'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
=======
# Generated by Django 2.2.7 on 2020-04-07 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('designer', '0003_auto_20200324_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('quantity_of_workers', models.IntegerField(default=0, verbose_name='Количество работников')),
                ('job', models.CharField(choices=[('Исполнитель', 'Исполнитель')], max_length=20, verbose_name='Профессия')),
                ('city', models.CharField(blank=True, max_length=30, verbose_name='Город')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.AlterField(
            model_name='project',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель'),
        ),
        migrations.AlterField(
            model_name='statement',
            name='application_room',
            field=models.CharField(choices=[('Все комнаты', 'Все комнаты'), ('Зал', 'Зал'), ('Гостинная', 'Гостинная'), ('Прихожая', 'Прихожая'), ('Ванная', 'Ванная'), ('Санузел', 'Санузел'), ('Гостевой санузел', 'Гостевой санузел'), ('Гостеванная ванная', 'Гостеванная ванная'), ('Главная ванная', 'Главная ванная'), ('Гардероб', 'Гардероб'), ('Спальня', 'Спальня'), ('Главная спальня', 'Главная спальня'), ('Детская', 'Детская'), ('Балкон', 'Балкон'), ('Лоджия', 'Лоджия'), ('Кабинет', 'Кабинет'), ('Кухня', 'Кухня'), ('Летняя кухня', 'Летняя кухня'), ('Котельная', 'Котельная'), ('Хозяйственной помещение', 'Хозяйственной помещение'), ('Прачечная', 'Прачечная')], default='', max_length=25, verbose_name='Комнаты'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
>>>>>>> 41cab1c05f495a20062a33725f040476f3915cb5
