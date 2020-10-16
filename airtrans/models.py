from django.db import models

# Create your models here.


class Booking(models.Model):
    book_ref = models.AutoField(primary_key=True)
    book_date = models.DateField()
    total_amount = models.FloatField()

    def __str__(self):
        return f"{self.book_ref}, {self.book_date}"


class Ticket(models.Model):
    ticket_no = models.AutoField(primary_key=True)
    book_ref = models.ForeignKey('Booking', on_delete=models.PROTECT)
    passenger_id = models.PositiveIntegerField()
    passenger_name = models.CharField(max_length=50)
    contact_data = models.TextField(max_length=50)

    def __str__(self):
        return f"{self.ticket_no}, {self.book_ref}, {self.passenger_id}, {self.passenger_name}, {self.contact_data}"
