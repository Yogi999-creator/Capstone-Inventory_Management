# Generated by Django 3.0.7 on 2021-04-26 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_auto_20210425_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='products',
            field=models.CharField(choices=[('Pen', 'Pen'), ('NoteBook', 'NoteBook')], default='Pen', max_length=15, null=True),
        ),
    ]
