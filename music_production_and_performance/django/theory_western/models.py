from django.db import models

# Create your models here.


#
# need to add a uniqueness constraint
#
class PitchClass(models.Model):
    name = models.CharField(max_length = 200, unique = True)
    chromatic_index_base_c = models.IntegerField()
    enharmonics = models.ManyToManyField('self')
    comment = models.TextField(null = True)

