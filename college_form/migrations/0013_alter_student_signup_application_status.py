# Generated by Django 4.1.7 on 2023-05-02 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_form', '0012_student_signup_application_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_signup',
            name='application_status',
            field=models.BooleanField(default=False),
        ),
    ]
