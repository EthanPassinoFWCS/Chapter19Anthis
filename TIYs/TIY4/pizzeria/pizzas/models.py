from django.db import models


class Pizza(models.Model):
    """Type of pizza the pizzeria has."""
    text = models.CharField(max_length=200) # Pizza Type

    def __str__(self):
        """Make a string representation of the module."""
        return self.text


class Topping(models.Model):
    topic = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text.__str__()) > 50:
            return f"{self.text[:50]}..."
        else:
            return f"{self.text}"
