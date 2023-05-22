from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name + str(self.id)

class Project(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=300)
    is_case_study = models.BooleanField(default=False)
    content = models.TextField()
    main_img_url = models.CharField(max_length=400,blank=True,null=True)
    github_url = models.CharField(max_length=400,blank=True,null=True)
    deployed_url = models.CharField(max_length=400,blank=True,null=True)
    order = models.IntegerField(default=1)
    is_published = models.BooleanField(default=False)
    technologies_used = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.title