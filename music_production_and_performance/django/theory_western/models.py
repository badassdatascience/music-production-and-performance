from django.db import models

# Create your models here.

class PitchClass(models.Model):
    name = models.CharField(max_length = 200, unique = True)
    chromatic_index_base_c = models.IntegerField()
    enharmonics = models.ManyToManyField('self')
    camelot_minor_number = models.IntegerField(null = True)
    camelot_major_number = models.IntegerField(null = True)
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

class IntervalSeries(models.Model):
    name = models.CharField(max_length = 200, unique = True)
    series = models.JSONField()

    def reconstruct(self, base = 0):
        reconstructed_list = [base]
        for interval in self.series:
            base = (base + interval) % 12
            reconstructed_list.append(base)
        return reconstructed_list
