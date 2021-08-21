from django.db import models


# Create your models here.


class Mooddata(models.Model):
    moodnum = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)

    def register(self):
        self.save()

    def __str__(self):
        return self.moodnum

    @staticmethod
    def get_all_mooddata():
        return Mooddata.objects.all()

    @staticmethod
    def get_all_moodnum(moodnum):
        return Mooddata.objects.get(moodnum)
