# Generated by Django 3.0.1 on 2020-08-04 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0026_remove_invoice_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='student',
            field=models.CharField(max_length=250),
        ),
    ]
