# GYM MANAGEMENT SYSTEM BY PEACE OLORUNTOBA C.E.O. PEASCAINC
# You can contact me on gmail @ profprincepeace@gmail.com or peascainc@gmail.com
# You can also call me or whatsapp me on +2348166846226

# GYM MANAGEMENT SYSTEM BY PEACE OLORUNTOBA C.E.O. PEASCAINC
# You can contact me on gmail @ profprincepeace@gmail.com or peascainc@gmail.com
# You can also call me or whatsapp me on +2348166846226

# Generated by Django 3.2 on 2021-08-20 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_trainersalary'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trainersalary',
            options={'verbose_name_plural': 'Trainer Salary'},
        ),
        migrations.AlterField(
            model_name='trainersalary',
            name='remarks',
            field=models.TextField(blank=True),
        ),
    ]
