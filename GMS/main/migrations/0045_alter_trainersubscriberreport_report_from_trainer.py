# GYM MANAGEMENT SYSTEM BY PEACE OLORUNTOBA C.E.O. PEASCAINC
# You can contact me on gmail @ profprincepeace@gmail.com or peascainc@gmail.com
# You can also call me or whatsapp me on +2348166846226

# Generated by Django 3.2 on 2021-09-11 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_auto_20210911_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainersubscriberreport',
            name='report_from_trainer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='report_from_trainer_rn', to='main.trainer'),
        ),
    ]
