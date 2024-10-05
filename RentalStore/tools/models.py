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
class MyManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs)
    def actives(self,*args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(is_active = True)
    

class Tool(models.Model):
    name =models.CharField(max_length=40,blank=False,null=False)
    description =models.TextField(blank=True,null=True)
    price_per_day=models.DecimalField(max_digits=10,decimal_places=2, default=100000)
    category=models.ForeignKey(Category, on_delete=models.PROTECT,related_name='Tool',blank=False,null=False)
    type = models.ForeignKey(ToolType,on_delete=models.PROTECT,related_name='Type',blank=False,null=False)
    is_active = models.BooleanField(default=True)
    default_manager = models.Manager()
    second_manager = MyManager()
    
    def __str__(self):
        return self.name


class ToolImages(models.Model):
    tool = models.ForeignKey(Tool,on_delete=models.CASCADE)
    image = models.ImageField(blank=True,null=True,upload_to='tool')

    def __str__(self):
        return f"{self.tool}"