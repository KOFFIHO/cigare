from django.db import models

# Create your models here.

from unittest.util import _MAX_LENGTH

# Create your models here.

class Produit(models.Model):
    type_de_produit= models.CharField(max_length=100)
    poids = models.CharField(blank=True,null=True ,max_length=50)
    quantite = models.IntegerField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    prix= models.IntegerField()
    imageProduit1= models.ImageField(upload_to='img1')
    imageProduit2= models.ImageField(upload_to='img2' ,blank=True,null=True)
    imageProduit3= models.ImageField(upload_to='img3' ,blank=True,null=True)
    numero = models.CharField(max_length=10)
    date_ajout = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_ajout']  # L'ordre est inversé ici
    # def __str__(self) :
    # 		return "{self.type_de_produit}"
    
    def get_all_produits():
    		return Produit.objects.all()
    
class Promotion(models.Model):
    promo_sur=models.CharField(blank=True,null=True, max_length=100)
    reduction=models.IntegerField(blank=True,null=True) 
    date_fin_promo=models.DateField(blank=True,null=True) 
    quantite = models.IntegerField(blank=True,null=True) 