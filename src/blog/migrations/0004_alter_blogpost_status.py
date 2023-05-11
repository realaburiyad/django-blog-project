# Generated by Django 4.2.1 on 2023-05-09 14:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_alter_blogpost_options_alter_category_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="status",
            field=models.CharField(
                choices=[
                    ("draft", "Draft"),
                    ("pending", "Pending"),
                    ("published", "Publish"),
                ],
                default="draft",
                max_length=10,
            ),
        ),
    ]
