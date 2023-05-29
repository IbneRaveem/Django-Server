# Generated by Django 4.2.1 on 2023-05-22 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0009_alter_listing_category_alter_listing_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Cars', 'Cars'), ('Furniture', 'Furniture'), ('Jobs', 'Jobs'), ('Property', 'Property'), ('Books&Sports', 'Books&Sports'), ('Mobiles', 'Mobiles'), ('Fashion', 'Fashion'), ('Bikes', 'Bikes'), ('Electronics', 'Electronics')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.CharField(choices=[('AR', 'Arunachal Pradesh'), ('MP', 'Madhya Pradesh'), ('HP', 'Haryana'), ('UK', 'Uttarakhand'), ('BR', 'Bihar'), ('NL', 'Nagaland'), ('MI', 'Sikkim'), ('MN', 'Manipur'), ('CG', 'Chhattisgarh'), ('TN', 'Tamil Nadu'), ('GJ', 'Gujarat'), ('AP', 'Andhra Pradesh'), ('WB', 'West Bengal'), ('MH', 'Maharashtra'), ('JH', 'Jharkhand'), ('KL', 'Kerala'), ('RJ', 'Rajasthan'), ('ML', 'Meghalaya'), ('OD', 'Odisha'), ('TS', 'Telegana'), ('TR', 'Tripura'), ('AS', 'Assam'), ('GA', 'Goa'), ('UP', 'Uttar Pradesh'), ('KA', 'Karnataka'), ('PB', 'Punjab'), ('MZ', 'Mizoram')], max_length=100),
        ),
    ]
