from django.db import models

class Singer(models.Model):
	stageName = models.CharField(max_length=128)
	name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128, null=True)
	image = models.ImageField(null=True,blank=True, upload_to="images/")
	nationality = models.CharField(max_length=128, null=True)
	
class Genre(models.Model):
	description = models.CharField(max_length=128)
class Album(models.Model):
	name = models.CharField(max_length=128)
	genre = models.ForeignKey(Genre, related_name='albumgenre', on_delete=models.CASCADE)
	singer = models.ForeignKey(Singer, related_name='albumsinger', on_delete=models.CASCADE)
	realeaseDate = models.DateTimeField(auto_now_add=True, null=True)
	#songs = models.ForeignKey(Songs, related_name='albumsongs', on_delete=models.CASCADE)
	price = models.DecimalField(max_digits = 6, decimal_places = 2)
	stock = models.DecimalField(max_digits = 6, decimal_places = 2)
	images = models.ImageField(null=True,blank=True, upload_to="images/")


	
	
class Songs(models.Model):
	name = models.CharField(max_length=128)
	singer = models.ForeignKey(Singer, related_name='songsinger', on_delete=models.CASCADE)
	realeaseDate = models.DateTimeField(auto_now_add=True, null=True)
	album = models.ForeignKey(Album, related_name='songsalbum', on_delete=models.CASCADE)
	duration = models.DecimalField(max_digits = 6, decimal_places = 2)
	completeFile = models.CharField(max_length=128)
	previewFile = models.CharField(max_length=128)
	price = models.DecimalField(max_digits = 6, decimal_places = 2)


# Create your models here.
