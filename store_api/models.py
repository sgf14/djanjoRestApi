from django.db import models

# Product should have been capitalied- its a Class
class product(models.Model):
    part_no = models.CharField(max_length=100)
    product_desc = models.CharField(max_length=100)
    product_cost = models.FloatField(help_text="(in $)")

