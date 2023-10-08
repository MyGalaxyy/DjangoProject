from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

    
class BlogUser(AbstractUser):

    role_choices =(
        (1, 'User'),
        (2, 'Admin'),
        (3, 'Moderator'),
    )
    
    avatar = models.FileField(("User Avatar"), upload_to="Uploads", max_length=100,blank=True)
    role = models.PositiveSmallIntegerField(choices=role_choices, null=True, blank=True)
    isBanned =models.BooleanField(("Hesap banlandi mi"),default=False)
    isApproved = models.BooleanField(("Hesap onaylandi mi"),default=False)
    aboutme = models.TextField(max_length=800,default='Kendinizi tanitabilirsiniz!',blank=True)
    educational_process= models.CharField(max_length=255, default='Belirtilmedi',blank=True)
    birthdate = models.DateField(null=True,blank=True)
    country = models.CharField(max_length=50, default='Belirtilmedi',blank=True)
    city = models.CharField(max_length=50, default='Belirtilmedi',blank=True)
    updatedAt = models.DateTimeField(auto_now=True)
    isReported = models.BooleanField(("Hesap şikayet edildi mi"),default=False)
    


    def handleAvatar(self):
        if self.avatar:
            return self.avatar.url
        else:
            return "/Uploads/default-undefined.png"

    def is_admin(self):
        return self.is_superuser
    
    def is_moderator(self):
        role = self.groups.filter(name="Moderator").exists()
        return role

    class Meta:
        verbose_name = "Kullanici"
        verbose_name_plural = "Kullanicilar"

like_choices =(
    ('Like', 'Like'),
    ('Unlike', "Unlike"),
)

class LikeTweet(models.Model):
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    post = models.ForeignKey('QuickMsg_app.tinksPost', on_delete=models.CASCADE)
    value = models.CharField(choices=like_choices, default='Like', max_length=10)

    def __str__(self) -> str:
        return "{user}=  {post} tweet'ini begendi".format(user= self.user.username, post=self.post )
    
    class Meta:
        verbose_name = 'Beğeni'
        verbose_name_plural = 'Beğenilen Tweetler'
        
#tweet model
class tinksPost(models.Model):
    user = models.ForeignKey(BlogUser, related_name="tinksposts", on_delete=models.DO_NOTHING)
    post = models.TextField(max_length=800)
    createdAt = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField('QuickMsg_app.LikeTweet', related_name="tweet_like", blank=True)
 
# likes count
    def count_likes(self):
       return self.likes.count()
    
    def __str__(self):
        return (f"{self.user}: " f"{self.post} - " f"({self.createdAt:%Y-%m-%d %H:%M})" )
    
    class Meta:
        verbose_name = "Tweet"
        verbose_name_plural = "Kullanici Tweetleri"

#Yorum Yapma Modeli
class TweetComment(models.Model):
     user = models.ForeignKey(BlogUser, verbose_name=('Yorum Yapan'),on_delete=models.CASCADE)
     comment = models.ForeignKey(tinksPost, related_name='comments', verbose_name=('tweet'),on_delete=models.CASCADE)
     message = models.TextField(("Yorum:"))
     createdAt = models.DateTimeField(("Olusturulma Tarihi"), auto_now=True)

     def __str__(self) -> str:
         return "{user}: {tweet}".format(user = self.user.username, tweet =self.message)

     class Meta:
            verbose_name = "Yorum"
            verbose_name_plural = " Kullanici Yorumlari" 
     
# Şikayet Modeli
class ReportManagement(models.Model):
    reportedBy = models.ForeignKey(BlogUser, related_name="complainant", verbose_name=('Şikayet Eden:'), on_delete=models.CASCADE)
    reportedUser =models.ForeignKey(BlogUser, verbose_name=('Şikayet Edilen User:'), on_delete=models.CASCADE)
    reportReason =models.ForeignKey(tinksPost, related_name='reports', verbose_name=('Şikayet Edilen Tweet:'),on_delete=models.CASCADE )
    reportMessage = models.TextField(("Sebep:"), default='Şikayet Nedeninizi Buraya Yaziniz')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
         return "{reportedBy}:: {reportReason} kullanici tweet'ini şikayet etti".format(reportedBy =self.reportedBy.username, reportReason =self.reportReason)

    class Meta:
        verbose_name = "Şikayet Edilen Kullanici"
        verbose_name_plural = "Şikayet Edilen Kullanicilar"

# Ban Modeli
class BanUser(models.Model):
    authorizedPerson = models.ForeignKey("BlogUser", related_name="yetkili", verbose_name=("Banlayan:"), on_delete=models.CASCADE)
    bannedUser = models.ForeignKey("BlogUser", verbose_name=("Banlanan User:"), on_delete=models.CASCADE)
    banReason = models.TextField(("Sebep:"), max_length=100, default=None)
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.bannedUser.username
    
    class Meta:
        verbose_name = "Banli Kullanici"
        verbose_name_plural = "Banlanan Kullanicilar"

# Remove Ban Modeli
class RemoveBan(models.Model):
    authorizedUser = models.ForeignKey("BlogUser", related_name="authorized", verbose_name=("Bani Kaldiran Yetkili:"), on_delete=models.CASCADE)
    removedbanUser = models.ForeignKey("BlogUser", verbose_name=("Bani Kaldirilan User:"), on_delete=models.CASCADE)
    removebanReason = models.TextField(("Sebep:"), max_length=100, default=None)
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.removedbanUser.username
    
    class Meta:
        verbose_name = "Bani Kaldirilan Kullanici"
        verbose_name_plural = "Bani Kaldirilan Kullanicilar"


