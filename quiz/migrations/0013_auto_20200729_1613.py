# Generated by Django 3.0.1 on 2020-07-29 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0012_merge_20200729_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='student',
            name='prev_marksheet',
        ),
        migrations.RemoveField(
            model_name='student',
            name='school_id',
        ),
        migrations.AlterField(
            model_name='question',
            name='img1',
            field=models.ImageField(null=True, upload_to='option1/', verbose_name='Image1'),
        ),
        migrations.AlterField(
            model_name='question',
            name='img2',
            field=models.ImageField(null=True, upload_to='option2/', verbose_name='Image2'),
        ),
        migrations.AlterField(
            model_name='question',
            name='img3',
            field=models.ImageField(null=True, upload_to='option3/', verbose_name='Image3'),
        ),
        migrations.AlterField(
            model_name='question',
            name='img4',
            field=models.ImageField(null=True, upload_to='option4/', verbose_name='Image4'),
        ),
    ]
