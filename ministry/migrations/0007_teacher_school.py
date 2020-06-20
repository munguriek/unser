# Generated by Django 2.2.6 on 2019-12-02 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ministry', '0006_schoolteacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='school',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ministry.School', verbose_name='Current School'),
            preserve_default=False,
        ),
    ]