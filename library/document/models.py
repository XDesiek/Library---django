from django.db import models

# Create your models here.
class Reporter(models.Model):
    first_name = models.CharField( max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

   
    def __str__(self):
        return "{}, {}".format(self.name, self.last_name)

class Article(models.Model):
    """Model definition for Article."""

    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline

    
