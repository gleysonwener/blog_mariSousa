# Generated by Django 4.0.5 on 2022-06-22 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_rename_imagem_post_post_foto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='foto',
            new_name='imagem_foto',
        ),
    ]