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
    book_ref = models.ForeignKey('Booking', on_delete=models.CASCADE)
    passenger_id = models.PositiveIntegerField()
    passenger_name = models.CharField(max_length=50)
    contact_data = models.TextField(max_length=50)

    def __str__(self):
        return f"{self.ticket_no}, {self.book_ref}, {self.passenger_id}, {self.passenger_name}, {self.contact_data}"


class Airport(models.Model):
    airport_code = models.AutoField(primary_key=True)
    airport_name = models.CharField(max_length=50, unique=True)
    city = models.CharField(max_length=50)
    coordinates = models.CharField(max_length=50)
    timezone = models.IntegerField()

    def __str__(self):
        return f"{self.airport_name}, {self.city}"


class Flight(models.Model):
    STASUS = (
        ("1", "На земле"),
        ("2", "Вылетел"),
        ("3", "Прибыл")

    )
    flight_id = models.AutoField(primary_key=True)
    flight_no = models.CharField(max_length=10)
    sheduled_departure = models.DateTimeField()
    sheduled_arrival = models.DateTimeField()
    departure_airport = models.ForeignKey("Airport", to_field="airport_name", on_delete=models.CASCADE, related_name="+")
    arrival_airport = models.ForeignKey("Airport", to_field="airport_name", on_delete=models.CASCADE, related_name="+")
    status = models.CharField(max_length=1, choices=STASUS)
    aircraft_code = models.ForeignKey("Aircraft", on_delete=models.CASCADE)
    actual_departure = models.DateTimeField()
    actual_arrival = models.DateTimeField()

    def __str__(self):
        return f"{self.departure_airport} - {self.arrival_airport}"


class Seat(models.Model):
    FARE_CONDITION = (
        ("1", "Эконом"),
        ("2", "Бизнес"),
        ("3", "Первый")
    )
    aircraft_code = models.ForeignKey("Aircraft", on_delete=models.CASCADE)
    seat_no = models.IntegerField()
    fare_condition = models.CharField(max_length=1, choices=FARE_CONDITION)

    def __str__(self):
        return f"{self.seat_no} - {self.fare_condition}"

    class Meta:
        unique_together = (('aircraft_code', 'seat_no'),)


class Aircraft(models.Model):
    aircraft_code = models.AutoField(primary_key=True)
    model = models.CharField(max_length=20)
    range = models.IntegerField()

    def __str__(self):
        return f"{self.model}"


class TicketFlight(models.Model):
    FARE_CONDITION = (
        ("1", "Эконом"),
        ("2", "Бизнес"),
        ("3", "Первый")
    )
    ticket_no = models.ForeignKey("Ticket", to_field="ticket_no", on_delete=models.CASCADE)
    flight_id = models.OneToOneField("Flight", on_delete=models.CASCADE)
    fare_condition = models.CharField(max_length=1, choices=FARE_CONDITION)
    amount = models.FloatField()

    def __str__(self):
        return f"{self.ticket_no}, {self.FARE_CONDITION}"

    class Meta:
        unique_together = (('ticket_no', 'flight_id'),)


class BoardingPass(models.Model):
    ticket_no = models.OneToOneField("TicketFlight", on_delete=models.CASCADE, related_name="+")
    flight_id = models.OneToOneField("TicketFlight", to_field="flight_id", on_delete=models.CASCADE, related_name="+")
    boarding_no = models.PositiveIntegerField()
    seat_no = models.OneToOneField("Seat", on_delete=models.CASCADE, related_name="+")

    def __str__(self):
        return f"{self.ticket_no}, {self.flight_id}, {self.seat_no}"

    class Meta:
        unique_together = (('ticket_no', 'flight_id'),)
        default_related_name = "BoardingPasses"
