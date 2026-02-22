from django.db import models
from django.db.models import F

class Counter(models.Model):
    value = models.PositiveIntegerField(default=0)

    def increment(self):
        """
        Business Logic: Logic for how a counter increases 
        lives here instead of in the view.
        """
        # We use filter().update() to stay atomic in PostgreSQL
        Counter.objects.filter(pk=self.pk).update(value=F('value') + 1)
        # Refresh from DB to get the new value back into Python
        self.refresh_from_db()

    def __str__(self):
        return f"Counter: {self.value}"