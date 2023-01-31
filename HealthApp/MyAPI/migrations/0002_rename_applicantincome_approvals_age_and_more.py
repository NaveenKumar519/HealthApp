# Generated by Django 4.1.4 on 2022-12-11 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyAPI', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='approvals',
            old_name='applicantincome',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='approvals',
            old_name='coapplicatincome',
            new_name='avg_glucose_level',
        ),
        migrations.RenameField(
            model_name='approvals',
            old_name='credithistory',
            new_name='bmi',
        ),
        migrations.RenameField(
            model_name='approvals',
            old_name='married',
            new_name='ever_married',
        ),
        migrations.RenameField(
            model_name='approvals',
            old_name='selfemployed',
            new_name='heartdisease',
        ),
        migrations.RemoveField(
            model_name='approvals',
            name='area',
        ),
        migrations.RemoveField(
            model_name='approvals',
            name='dependants',
        ),
        migrations.RemoveField(
            model_name='approvals',
            name='graduatededucation',
        ),
        migrations.RemoveField(
            model_name='approvals',
            name='loanamt',
        ),
        migrations.RemoveField(
            model_name='approvals',
            name='loanterm',
        ),
        migrations.AddField(
            model_name='approvals',
            name='hypertension',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='approvals',
            name='residence_type',
            field=models.CharField(choices=[('Urban', 'Urban'), ('Rural', 'Rural')], default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='approvals',
            name='smoking_status',
            field=models.CharField(choices=[('formerly smoked', 'formerly smoked'), ('never smoked', 'never smoked'), ('smokes', 'smokes')], default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='approvals',
            name='work_type',
            field=models.CharField(choices=[('Private', 'Private'), ('Self-employed', 'Self-employed')], default=0, max_length=15),
            preserve_default=False,
        ),
    ]
