from django.conf import settings
from django.db import models

from book.models import Book


class Borrowing(models.Model):
    borrow_date = models.DateTimeField()
    expected_return_date = models.DateTimeField()
    actual_return_date = models.DateTimeField(blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(
                    borrow_date__lte=models.F("expected_return_date")
                ),
                name="borrow_date_lte_expected_return_date",
            ),
            models.CheckConstraint(
                check=models.Q(
                    borrow_date__lte=models.F("actual_return_date")
                ),
                name="borrow_date_lte_actual_return_date",
            ),
            models.CheckConstraint(
                check=models.Q(
                    expected_return_date__gte=models.F("borrow_date")
                ),
                name="expected_return_date_gte_borrow_date",
            ),
            models.CheckConstraint(
                check=models.Q(
                    actual_return_date__gte=models.F("borrow_date")
                ),
                name="actual_return_date_gte_borrow_date",
            ),
        ]

    @property
    def is_active(self):
        if self.actual_return_date is None:
            return True
        return False
