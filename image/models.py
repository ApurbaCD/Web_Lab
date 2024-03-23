from django.db import models

# Create your models here.

class Image (models.Model):
    description=models.CharField(max_length=100, default="")
    tree_name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="img/%y")
    def __str__(self):
        return self.tree_name

    # def get_details(self):
    # # Returns a dictionary containing caption and description of the image.
    #     return {
    #         "caption": self.caption,
    #         "description": self.description
    #     }
