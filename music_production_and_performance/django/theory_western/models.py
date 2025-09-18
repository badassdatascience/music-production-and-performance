from django.db import models

# Create your models here.

class PitchClass(models.Model):
    name = models.CharField(max_length = 200, unique = True)
    chromatic_index_base_c = models.IntegerField()
    enharmonics = models.ManyToManyField('self')
    camelot_minor_number = models.IntegerField(null = True)
    camelot_major_number = models.IntegerField(null = True)
    comment = models.TextField(null = True)

    #
    # need to add a specific exception for uniqueness violation
    #
    # also, this is a static function; there might be a better design
    # pattern available...
    #
    def load_by_list_of_pitch_class_names(chromatic_scale_pitch_class_names):
        for i, pc_name in enumerate(chromatic_scale_pitch_class_names):
            try:
                pc = PitchClass(
                    name = pc_name.strip(),
                    chromatic_index_base_c = i,
                )
                pc.save()
            except:
                pass

    #
    # need to deal with specific exception for uniqueness violations
    #
    # also, this is a static function; there might be a better design
    # pattern available...
    #
    def load_enharmonics(enharmonics_map):
        for name in enharmonics_map.keys():
            enharmonic_name = enharmonics_map[name]
            pc_base = PitchClass.objects.get(name = enharmonic_name)

            # need to add a specific exception for uniqueness violation
            try:
                pc = PitchClass(
                    name = name.strip(),
                    chromatic_index_base_c = pc_base.chromatic_index_base_c,
                )
                pc.save()
                pc.enharmonics.add(pc_base),
                pc.save()
                
                pc_base.enharmonics.add(pc)
                pc_base.save()
            except:
                pass

            
    
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

    def reconstruct(self, base = 0, use_modulus = True):
        reconstructed_list = [base]
        for interval in self.series:
            if use_modulus:
                base = (base + interval) % 12
            else:
                base = base + interval
                
            reconstructed_list.append(base)
        return reconstructed_list
