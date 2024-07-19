from django.db import models

# this model will determine how todo items or task items should be stored in db to decribe 3 propertites - title, description and completed(boolean)

class Todo(models.Model):
    title=models.CharField(max_length=120)
    description=models.CharField(max_length=500)
    completed=models.BooleanField(default=False)

    def __str__(self):
        return self.title
    


