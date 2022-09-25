from django.db import models
from taggit.managers import TaggableManager

#choices for difficulty
class DIFFICULTY_CHOICES(models.IntegerChoices):
    EASY = 1
    MEDIUM = 2
    HARD = 3

class Content(models.Model):
    title = models.CharField(max_length=100)
    tags = TaggableManager()
    author = models.CharField(max_length=30,null=True)
    created = models.DateTimeField(null=True)
    last_modified = models.DateTimeField(null=True)
    difficulty_rating = models.IntegerField(choices=DIFFICULTY_CHOICES.choices)
    problem_description = models.TextField()
    hints = models.TextField()
    solution = models.TextField()

    def __str__(self):
        return f'{self.title} : {self.difficulty_rating}\n{self.problem_description}\n'

