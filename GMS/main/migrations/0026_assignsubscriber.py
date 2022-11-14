# GYM MANAGEMENT SYSTEM BY PEACE OLORUNTOBA C.E.O. PEASCAINC
# You can contact me on gmail @ profprincepeace@gmail.com or peascainc@gmail.com
# You can also call me or whatsapp me on +2348166846226

# Generated by Django 3.2 on 2021-08-15 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_notifuserstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignSubscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.subscriber')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.trainer')),
            ],
        ),
    ]
