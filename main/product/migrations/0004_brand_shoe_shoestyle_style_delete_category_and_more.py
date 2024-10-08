# Generated by Django 5.1.1 on 2024-09-24 09:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_category_alter_product_type_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Brand',
            },
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'Shoe',
            },
        ),
        migrations.CreateModel(
            name='ShoeStyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'ShoeStyle',
            },
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=20)),
                ('size', models.IntegerField()),
                ('type', models.CharField(max_length=20)),
                ('material', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Style',
            },
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='product_type',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='default description'),
        ),
        migrations.AlterModelTable(
            name='product',
            table='Product',
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='product.brand'),
        ),
        migrations.AddField(
            model_name='shoe',
            name='product',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AddField(
            model_name='shoestyle',
            name='shoe',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='product.shoe'),
        ),
        migrations.AddField(
            model_name='style',
            name='shoe',
            field=models.ManyToManyField(through='product.ShoeStyle', to='product.shoe'),
        ),
        migrations.AddField(
            model_name='shoestyle',
            name='style',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='product.style'),
        ),
        migrations.AlterUniqueTogether(
            name='style',
            unique_together={('color', 'size', 'material')},
        ),
        migrations.AlterUniqueTogether(
            name='shoestyle',
            unique_together={('shoe', 'style')},
        ),
    ]
