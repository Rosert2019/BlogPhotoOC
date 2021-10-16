from django.db import models
from django.conf import settings

from PIL import Image

# Create your models here.
class Photo(models.Model):
    image = models.ImageField()
    caption = models.CharField(max_length=128, blank=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    IMAGE_MAX_SIZE = (800, 800)
    
    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        # sauvegarde de l’image redimensionnée dans le système de fichiers
        # ce n’est pas la méthode save() du modèle !
        image.save(self.image.path)

    #Surchage de la méthode save, les photos seront redimentionnées directement à leur sauvegarde
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()    

class Blog(models.Model):
    photo = models.ForeignKey(Photo, null=True, on_delete=models.SET_NULL, blank=True)
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=5000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    starred = models.BooleanField(default=False)
    word_count = models.IntegerField(null=True)

    def _get_word_count(self):
        return len(self.content.split(' '))

    def save(self, *args, **kwargs):
        self.word_count = self._get_word_count()
        super().save(*args, **kwargs)


"""
Imaginons qu’un développeur senior ait décidé que le fait de calculer le nombre de mots pour chaque billet individuel au fil de l’eau était trop intensif d’un point de vue informatique. Il estime que ces informations devraient être stockées en tant que champ dans le modèle  Blog  . Ce champ devrait alors se mettre à jour automatiquement, dès que l’on apporte des changements à l’instance de  Blog 
"""        