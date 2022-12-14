# Generated by Django 4.1 on 2022-09-06 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blogging", "0002_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
        migrations.RemoveField(
            model_name="category",
            name="description",
        ),
        migrations.RemoveField(
            model_name="category",
            name="posts",
        ),
        migrations.AddField(
            model_name="post",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="blogging.category",
            ),
        ),
    ]
