from django.db import models


class Borrowings(models.Model):
    borrow_date = models.DateTimeField()
    expected_return_date = models.DateTimeField()
    actual_return_date = models.DateTimeField(blank=True)
    book_id = models.IntegerField(help_text="id of borrowed book")
    user_id = models.IntegerField(help_text="user's id, borrowed book")

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
