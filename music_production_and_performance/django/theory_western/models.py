from django.db import models

# Create your models here.

class PitchClass(models.Model):
    name = models.CharField(max_length = 200, unique = True)
    chromatic_index_base_c = models.IntegerField()
    enharmonics = models.ManyToManyField('self')
    comment = models.TextField(null = True)

# need a uniqueness constraint
class Fifths(models.Model):
    pitch_class_below = models.ForeignKey(
        PitchClass,
        on_delete = models.CASCADE,
        related_name = 'pitch_class_fifth_below',
    )
    
    pitch_class = models.ForeignKey(PitchClass, on_delete = models.CASCADE)

    pitch_class_above = models.ForeignKey(
        PitchClass,
        on_delete = models.CASCADE,
        related_name = 'pitch_class_fifth_above',
    )
