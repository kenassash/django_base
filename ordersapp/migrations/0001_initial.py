# Generated by Django 3.2 on 2022-01-03 05:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0004_auto_20211213_2257'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('FM', 'формируется'), ('STP', 'отправлено в обработку'), ('PRD', 'обработано'), ('PD', 'оплачено'), ('CNL', 'отменено'), ('DN', 'завершено')], default='FM', max_length=3)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=0, verbose_name='Колличество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitems', to='ordersapp.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product', verbose_name='Продукт')),
            ],
        ),
    ]
