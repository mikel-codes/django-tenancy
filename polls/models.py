from django.db import models

# Create your models here.
class Poll(models.Model):
   question = models.CharField(max_length=100, help_text='ask your question')
   created_by = models.ForeignKey('User', related_name='poll', on_delete=models.CASCADE)
   pb_date = models.DateField(auto_now=True, auto_now_add=False)


   #Metadata
   class Meta :
       ordering = ['-pb_date']

   #Methods


   def __str__(self):
       return self.created_by

class Choice(models.Model):
    """Model definition for Choice."""
    poll = models.ForeignKey('Poll', related_name='choices', on_delete=models.CASCADE)
    choice_text  = models.CharField(max_length=50)


    # TODO: Define fields here

    class Meta:
        """Meta definition for Choice."""

        verbose_name = 'Choice'
        verbose_name_plural = 'Choices'



class Vote(models.Model):
    choice = models.ForeignKey('Poll', related_name='votes', on_delete=models.CASCADE)
    poll =  models.ForeignKey('Poll', related_name='votes', on_delete=models.CASCADE)
    voted_by = models.ForeignKey('User', related_name='votes', on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('choice', 'poll')
