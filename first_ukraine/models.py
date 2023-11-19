from django.db import models


class User(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    owner = models.BooleanField(default=False)
    phone = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('X', 'X'),
    )

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.firstname + ' ' + self.lastname


class Establishment(models.Model):
    name = models.CharField(max_length=50)
    HOTEL = "HO"
    CAFE = "CA"
    RESTAURANT = "RE"
    choices = [(HOTEL, "Hotel"), (CAFE, "Cafe"), (RESTAURANT, "Restaurant")]
    establishment_type = models.CharField(max_length=2, choices=choices, default=HOTEL)
    capacity = models.IntegerField()
    covid_hygiene = models.BooleanField(default=False)
    owner = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' ' + self.establishment_type


class Reservation(models.Model):
    establishment = models.ForeignKey('Establishment', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    number_of_person = models.IntegerField()
