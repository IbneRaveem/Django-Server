# Generated by Django 4.2.1 on 2023-05-25 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0012_auto_20230525_1602"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="category",
            field=models.CharField(
                choices=[
                    ("Jobs", "Jobs"),
                    ("Cars", "Cars"),
                    ("Electronics", "Electronics"),
                    ("Furniture", "Furniture"),
                    ("Fashion", "Fashion"),
                    ("Mobiles", "Mobiles"),
                    ("Property", "Property"),
                    ("Books&Sports", "Books&Sports"),
                    ("Bikes", "Bikes"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="listing",
            name="state",
            field=models.CharField(
                choices=[
                    ("GJ", "Gujarat"),
                    ("TN", "Tamil Nadu"),
                    ("TR", "Tripura"),
                    ("MP", "Madhya Pradesh"),
                    ("MH", "Maharashtra"),
                    ("AS", "Assam"),
                    ("NL", "Nagaland"),
                    ("PB", "Punjab"),
                    ("MN", "Manipur"),
                    ("UP", "Uttar Pradesh"),
                    ("BR", "Bihar"),
                    ("CG", "Chhattisgarh"),
                    ("TS", "Telangana"),
                    ("RJ", "Rajasthan"),
                    ("MI", "Sikkim"),
                    ("JH", "Jharkhand"),
                    ("OD", "Odisha"),
                    ("AP", "Andhra Pradesh"),
                    ("ML", "Meghalaya"),
                    ("UK", "Uttarakhand"),
                    ("KL", "Kerala"),
                    ("HP", "Haryana"),
                    ("WB", "West Bengal"),
                    ("MZ", "Mizoram"),
                    ("AR", "Arunachal Pradesh"),
                    ("KA", "Karnataka"),
                    ("GA", "Goa"),
                ],
                max_length=100,
            ),
        ),
    ]
