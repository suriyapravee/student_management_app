# Generated by Django 4.2.6 on 2023-10-14 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=20)),
                ('sid', models.IntegerField()),
                ('dept_name', models.IntegerField()),
                ('did', models.IntegerField()),
                ('college_name', models.CharField(max_length=50)),
            ],
        ),
    ]
