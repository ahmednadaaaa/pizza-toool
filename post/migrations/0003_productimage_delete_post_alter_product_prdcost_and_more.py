# Generated by Django 4.1.5 on 2023-01-30 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRDIImage', models.ImageField(upload_to='Product/', verbose_name='Image')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDCost',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='cost'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDCreated',
            field=models.DateTimeField(verbose_name='created At'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDDesc',
            field=models.TextField(verbose_name='product Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDName',
            field=models.CharField(max_length=100, verbose_name='product name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDPrice',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='price'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='PRDIProduct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.product', verbose_name='product'),
        ),
    ]