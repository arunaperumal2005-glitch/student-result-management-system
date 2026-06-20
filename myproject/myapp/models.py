from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    tamil = models.IntegerField()
    english = models.IntegerField()
    maths = models.IntegerField()
    science = models.IntegerField()
    social = models.IntegerField()

    def total(self):
        return self.tamil + self.english + self.maths + self.science + self.social

    def grade(self):
        avg = self.total() / 5
        if avg >= 90:
            return 'A+'
        elif avg >= 75:
            return 'A'
        elif avg >= 60:
            return 'B'
        elif avg >= 35:
            return 'C'
        else:
            return 'F'

    def status(self):
        if self.tamil >= 35 and self.english >= 35 and self.maths >= 35 and self.science >= 35 and self.social >= 35:
            return 'Pass'
        return 'Fail'