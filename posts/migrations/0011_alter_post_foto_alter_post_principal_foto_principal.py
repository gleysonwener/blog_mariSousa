# Generated by Django 4.0.5 on 2022-06-23 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_alter_post_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='staticfiles/%Y/%m/%d', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='post_principal',
            name='foto_principal',
            field=models.ImageField(blank=True, null=True, upload_to='staticfiles_principal/%Y/%m/%d', verbose_name='Imagem Principal'),
        ),
    ]