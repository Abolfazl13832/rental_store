from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=32,blank=False,null=False)
    description = models.CharField( max_length=320,blank=True,null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Categories"
        verbose_name_plural = "Categories"
class ToolType(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name
class Tool(models.Model):
    name =models.CharField(max_length=40,blank=False,null=False)
    description =models.TextField(blank=True,null=True)
    price_per_day=models.DecimalField(max_digits=10,decimal_places=2, default=100000)
    category=models.ForeignKey(Category, on_delete=models.PROTECT,related_name='Tool',blank=False,null=False)
    type = models.ForeignKey(ToolType,on_delete=models.PROTECT,related_name='Type',blank=False,null=False)
    def __str__(self):
        return self.name