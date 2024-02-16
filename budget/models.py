from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    budget = models.IntegerField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)


    def budget_remaining(self):
        expense_list = Expense.objects.filter(project=self)
        total_expense = 0
        for expense in expense_list:
            total_expense += expense.cost
        
        return self.budget - total_expense


    def total_cost(self):
        expense_list = Expense.objects.filter(project=self)
        return len(expense_list)


class Category(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

class Expense(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='expenses')
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)

    class Meta:
        ordering = ('-cost',)