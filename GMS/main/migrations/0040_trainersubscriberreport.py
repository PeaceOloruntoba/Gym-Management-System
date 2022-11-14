# GYM MANAGEMENT SYSTEM BY PEACE OLORUNTOBA C.E.O. PEASCAINC
# You can contact me on gmail @ profprincepeace@gmail.com or peascainc@gmail.com
# You can also call me or whatsapp me on +2348166846226

# Generated by Django 3.2 on 2021-09-11 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0039_remove_trainermsg_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainerSubscriberReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_msg', models.TextField()),
                ('report_for_trainer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='report_for_trainer', to='main.trainer')),
                ('report_for_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='report_for_user', to=settings.AUTH_USER_MODEL)),
                ('report_from_trainer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='report_from_trainer', to='main.trainer')),
                ('report_from_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='report_from_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
