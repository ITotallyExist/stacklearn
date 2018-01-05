# Generated by Django 2.0.1 on 2018-01-05 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathstack', '0004_booleananswer_integeranswer'),
    ]

    operations = [
        migrations.CreateModel(
            name='BooleanQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operand1', models.IntegerField()),
                ('operand2', models.IntegerField()),
                ('operator', models.CharField(choices=[('MODULUS', '%')], max_length=2)),
                ('correct_answer', models.BooleanField()),
            ],
        ),
    ]
