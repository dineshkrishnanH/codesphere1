from django.db import models

# Create your models here.

from django.contrib.auth.models import User

from embed_video.fields import EmbedVideoField

class BaseModel(models.Model):

    created_date=models.DateTimeField(auto_now_add=True)

    updated_date=models.DateTimeField(auto_now=True)

    is_activate=models.BooleanField(auto_now=True)


class UserProfile(BaseModel):
 
   bio=models.CharField(max_length=200)

   phone=models.CharField(max_length=200)

   owner=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")

   profile_picture=models.ImageField(upload_to="profile_picture",null=True,blank=True)



   def __str__(self) -> str:
       return self.owner.username
    

class Tag(BaseModel):

    title=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title
    

class Project(BaseModel):

    title=models.CharField(max_length=200)

    description=models.TextField()

    preview_image=models.ImageField(upload_to="profile_picture",null=True,blank=True)

    price=models.PositiveIntegerField()

    developer=models.ForeignKey(User,on_delete=models.CASCADE)

    files=models.FileField(upload_to="projects",null=True,blank=True)

    tag_objects=models.ManyToManyField(Tag,null=True)

    thumbnail=EmbedVideoField()


#request.user.basket
class wishlist(BaseModel):

    owner=models.OneToOneField(User,on_delete=models.CASCADE,related_name="basket")



#requwst.user.basket.basket_item
class wishlistItem(BaseModel):

    wishlist_object=models.ForeignKey(wishlist,on_delete=models.CASCADE,related_name="basket-item")

    Project_object=models.ForeignKey(Project,on_delete=models.CASCADE)

    is_order_placed=models.BooleanField(default=False)
    
class Order(BaseModel):

    wishlist_item_objects=models.ManyToManyField(wishlistItem)

    is_paid=models.BooleanField(default=False)

    order_id=models.CharField(max_length=200,null=True)

    

    




    




