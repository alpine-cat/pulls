# Generated by Django 2.2.7 on 2019-11-28 15:24

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={},
        ),
        migrations.AlterModelManagers(
            name='book',
            managers=[
                ('man', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='author',
            unique_together=set(),
        ),
        migrations.AlterModelTable(
            name='author',
            table=None,
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=150)),
                ('object_id', models.IntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.RemoveField(
            model_name='author',
            name='last_name',
        ),
    ]
