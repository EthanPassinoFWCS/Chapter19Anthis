from django.db import models


class Pizza(models.Model):
    """Type of pizza the pizzeria has."""
    text = models.CharField(max_length=200) # Pizza Type
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the module."""
        return self.text


class Topping(models.Model):
    """Toppings for the Pizza."""
    topic = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text.__str__()) > 50:
            return f"{self.text[:50]}..."
        else:
            return f"{self.text}"
