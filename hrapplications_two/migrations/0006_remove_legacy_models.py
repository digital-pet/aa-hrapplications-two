# Generated by Django 1.11.2 on 2017-06-08 02:54

from django.db import migrations


def delete_permissions(apps, schema_editor):
    HRApplication = apps.get_model('hrapplications_two', 'HRApplication')
    HRApplicationComment = apps.get_model('hrapplications_two', 'HRApplicationComment')
    ContentType = apps.get_model('contenttypes', 'ContentType')
    Permission = apps.get_model('auth', 'Permission')
    ct1 = ContentType.objects.get_for_model(HRApplication)
    ct2 = ContentType.objects.get_for_model(HRApplicationComment)
    Permission.objects.filter(content_type__in=[ct1, ct2]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('hrapplications_two', '0005_sorted_questions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hrapplication',
            name='corp',
        ),
        migrations.RemoveField(
            model_name='hrapplication',
            name='reviewer_character',
        ),
        migrations.RemoveField(
            model_name='hrapplication',
            name='reviewer_inprogress_character',
        ),
        migrations.RemoveField(
            model_name='hrapplication',
            name='reviewer_user',
        ),
        migrations.RemoveField(
            model_name='hrapplication',
            name='user',
        ),
        migrations.RemoveField(
            model_name='hrapplicationcomment',
            name='application',
        ),
        migrations.RemoveField(
            model_name='hrapplicationcomment',
            name='commenter_character',
        ),
        migrations.RemoveField(
            model_name='hrapplicationcomment',
            name='commenter_user',
        ),
        migrations.RunPython(delete_permissions, migrations.RunPython.noop),
        migrations.DeleteModel(
            name='HRApplication',
        ),
        migrations.DeleteModel(
            name='HRApplicationComment',
        ),
    ]
