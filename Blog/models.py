from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(
    "Category",
    on_delete=models.SET_NULL,
    null=True,
    blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100, default='Visiteur')
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Commentaire(models.Model):
    texte = models.TextField(max_length=500)
    auteur = models.CharField(max_length=100, default='Visiteur')
    post = models.ForeignKey(
        to='Post', 
        on_delete=models.CASCADE,  # si le post est supprimé, ses commentaires aussi
        related_name='commentaires'
        )
    created_at = models.DateTimeField(auto_now_add=True)  # utile pour trier

    def __str__(self):
        return self.auteur


class Contact(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

