from django.db import models
class Brand(models.Model):
  name = models.TextField()
  def __str__(self):
    return self.name
class Product(models.Model):
  name = models.TextField()
  price = models.DecimalField(max_digits=10,decimal_places=2)
  added = models.DateTimeField(auto_now_add=True)
  brand = models.ForeignKey(Brand, null=True)
  description = models.TextField(null=True)
  def __str__(self):
    return self.name
