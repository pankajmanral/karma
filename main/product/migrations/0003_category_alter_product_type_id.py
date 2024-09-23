from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.AlterField(
            model_name='product_type',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
