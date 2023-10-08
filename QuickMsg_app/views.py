from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .form import *
from .models import *
# Create your views here.

from django.contrib.auth.models import Group

# Anasayfa
def HomePage(request):
    posts = tinksPost.objects.all().order_by("-likes")
    
    return render(request,'homepage.html', {"posts":posts})

# Navbar Hesap Islem Alani 
# Giris Yap
def signIn(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:

            user = authenticate(request,username=username, password=password)

            if user:
                if user.isBanned:
                    messages.error(request,"Hesabiniz Askiya alindi.Lütfen Sayfa Admini ile iletisime geciniz.")
                    return redirect('loginpage')
                
                login(request,user)
                return redirect('homepage')
            
            else:
                messages.error(request,"Böyle bir kullanici bulunmamaktadir.")
                return redirect('loginpage')

    else:
        return render(request, 'sign_in.html')
    
# Cikis Yap 
def signOut(request):

        logout(request)
        return redirect('homepage')
    
# Kayit ol
def signUp(request):
    context ={}
    if request.method == 'POST':
        
        formData = RegisterForm(request.POST)

        if formData.is_valid():

            user = formData.save(commit=False)
            user.set_password(formData.cleaned_data["password"])
            user.save()
            
            login(request,user)
            return redirect('homepage')

        else:
            return redirect('signupPage')
        
    else:
        context['regform'] = RegisterForm()
        return render(request, 'sign_up.html', context)

# User Profile-Kisisel Bilgiler baslangic
@login_required(login_url="loginpage")
def userProfile(request, userId):

    user = BlogUser.objects.filter(id=userId).first()
    if request.user.id == user.id and request.user.is_authenticated:
        context ={}

        

        if user :
            context['user']=user
            context['profileData']=UserUpdateProfileForm(user)
            return render(request,'user_profile.html',context)
    
        else:
            return redirect('403page')
    else:
        return redirect('403page')
    
# User-Profile Güncelleme
@login_required(login_url='loginpage')
def profileSettings(request):
    context ={}
    if request.user.is_authenticated:
        user = BlogUser.objects.filter(id=request.user.id).first()

        if user:
            context['updateprofile'] = UserUpdateProfileForm(instance=user)
        
        else:
            return redirect('404page')

        if request.method == 'POST':
            password = request.POST.get('password')
            
            updateprofile = UserUpdateProfileForm(request.POST, instance=user)

            if updateprofile.is_valid():
                
                messages.add_message(request,messages.SUCCESS,"Bilgileriniz basarili bir sekilde güncellendi")
                updateprofile.save()
                
                if password:
                    user.set_password(password)
                    updateprofile.save()
                return redirect('userprofile',request.user.id)
            
            else:
                return redirect('404page')
        
        else:
            return render(request, 'profile_settings.html',context)
    
    else: 
        return redirect('loginpage')
        
# User Hesabini sil
def removeAccount(request, userId):
    
    if request.user.is_authenticated and request.user.is_admin() or request.user.is_moderator():
        
        user = BlogUser.objects.filter(id = int(userId)).first()

        if user:
            user.is_active = False
            user.save()
            return redirect('homepage')

        else:
            return redirect('userprofile',userId)
    else:
        return redirect('403page')
    
# Userın kendi tweetleri ve profili
@login_required(login_url="loginpage")
def usertweet(request,userId):
    context={}
    if request.user.is_authenticated and request.user.isApproved:

        user = BlogUser.objects.filter(id=userId).first()
        tweet=tinksPost.objects.filter(user_id=user.id)
         
        if user:
            context['user'] = user
            context['isBanned'] = user.isBanned

            if not request.user.is_authenticated:
                return redirect('403page')
        
        if tweet:
            context['post'] = tweet

        else:
            return redirect('404page')

         
        return render(request, 'user_tweets.html',context)
    else:
        return redirect('403page')
    
# Tweet(post) olusturma
@login_required(login_url='loginpage')
def createTweet(request):

    if request.user.is_authenticated and request.user.isApproved:
    
        if request.method == 'POST':
        
            tweet_olustur = request.POST.get('tweet_olustur')

            if tweet_olustur: 

                tinksPost.objects.create(
                    user = request.user,
                    post= tweet_olustur
                )
                return redirect('homepage')
        
            else:
                return redirect('404page')
    
        else:
            return redirect('404page')
    else:
        return redirect('403page')
    
# Tweet(post) silme
@login_required(login_url='loginpage')
def deleteTweet(request, tweetId):

    if request.user.is_authenticated and request.user.isApproved or request.user.id == tweetId or request.user.is_superuser or request.user.is_moderator():
    
        tweet_sil= tinksPost.objects.filter(id=tweetId).first()
    
        if  tweet_sil:
            messages.add_message(request,messages.SUCCESS,"Tweet'iniz başarili bir şekilde silindi.")
            tweet_sil.delete()

            return redirect('homepage')
    
        else:
            return redirect('404page')
    else:
        return redirect('403page')
    
# Tweeti düzenle
@login_required(login_url='loginpage')
def updateTweet(request,tweetId):
    context ={}
    
    tweet=tinksPost.objects.filter(id=tweetId).first()
    
    if tweet and request.user.id == tweet.user.id or (request.user.is_superuser or request.user.is_moderator):
            
            tweetform = UpdateTweetForm(instance=tweet)
            context['onetweet'] = tweet
            context['updateform'] = tweetform
           
            if not request.user.is_authenticated or not request.user.isApproved:

                return redirect('403page')     
    else:
        return redirect('403page')
    
    if request.method == 'POST':
        
        tweetform = UpdateTweetForm(request.POST, instance=tweet)

        if tweetform.is_valid(): 
            messages.add_message(request,messages.SUCCESS,"Tweet'iniz başarili bir şekilde düzenlendi.")
            tweetform.save()

            return redirect('update_tweet',tweetId)

        else:
            return redirect('404page')

    else:
        return render(request, 'update_tweet.html',context)

# Tweet Begen     
# def tweetLike(request, pk):

#     if request.user.is_authenticated and request.user.isApproved:
        
#         if request.method == 'POST':
#             post_id = request.POST.get('tweet_id')
#             user = request.user
            
#             tweet = tinksPost.objects.filter(id=pk).first() 
            
#             if user in tweet.likes.all():
#                 tweet.likes.remove(user)
#             else:
#                 tweet.likes.add(user)

#             like, created = LikeTweet.objects.get_or_create(user=user, post_id = post_id)
            
#             if not created:
#                 if like.value == 'Like':
#                     like.value = 'Unlike'
#                 else:
#                     like.value = 'Like'

#                 return redirect('homepage')
            
#             else:
#                 return redirect('homepage')
#         else:
#             return redirect ('404page')

#     else:
#         return redirect('403page')

# Yorum Yap
@login_required(login_url='loginpage')
def createComment(request, tweetId):
    
    if request.user.is_authenticated and request.user.isApproved or request.user.is_superuser or request.user.is_moderator():
        context={}

        post=tinksPost.objects.filter(id=tweetId).first()
    
        if post is None:
                        
            return redirect('403page')
    
        if request.method == 'POST':
        
            form = CreateCommentForm(request.POST)

            if form.is_valid():

                form = form.save(commit=False)
                form.user = request.user
                form.comment = post
                form.save()

                return redirect('create_comment',tweetId)
        
        else:   
                context['post'] = post
                context['commentform'] = CreateCommentForm()
            
                return render(request, 'create_comment.html',context)
    else:
        return redirect('403page')

# Yorum güncelle
@login_required(login_url='loginpage')
def updateComment(request,commentId):
    
    if request.user.is_authenticated or request.user.isApproved or request.user.is_superuser or request.user.is_moderator():

        context ={}
    
        comment = TweetComment.objects.filter(id=commentId).first()
    
        if comment:
            
                commentform = UpdateCommentForm(instance=comment)
                context['onecomment'] = comment
                context['commentupdateform'] = commentform
            
        else:
            return redirect('403page')
    
        if request.method == 'POST':
        
            commentform = UpdateCommentForm(request.POST, instance=comment)

            if commentform.is_valid(): 
                messages.add_message(request,messages.SUCCESS,"Yorumunuz başarili bir şekilde düzenlendi.")
                commentform.save()

                return redirect('update_comment',commentId)

            else:
                return redirect('404page')

        else:
            return render(request, 'update_comment.html',context)
    else:
        return redirect('403page')

# Yorum sil
@login_required(login_url='loginpage')
def deleteComment(request,tweetId,commentId):

    if request.user.is_authenticated or request.user.isApproved or request.user.is_superuser or request.user.is_moderator():

        tweet = tinksPost.objects.filter(id=tweetId).first()

        if tweet:

            comment = TweetComment.objects.filter(id=commentId).first()

            if comment and request.user.isApproved and request.user.id == comment.user.id and tweet.user.id or request.user.is_superuser or request.user.is_moderator:
                messages.add_message(request,messages.SUCCESS,"Yorumunuz başarili bir şekilde silindi.")
                comment.delete()
            

                return redirect('create_comment',tweetId)
        
            else:
                return redirect('403page')
        
        else:
            return redirect('404page')
    else:
        return redirect('403page')

# Tweet şikayet et 
def reportUser(request, userId, tweetId):

    if request.user.is_authenticated or request.user.is_admin() or request.user.is_moderator():

        context={}
        tweet = tinksPost.objects.filter(id=tweetId).first()
        user = BlogUser.objects.filter(id=tweet.user.id).first()
    
        if tweet is None:
            return redirect('404page')
        
        else:
            if request.method == 'POST':
            
                form = ReportUserForm(request.POST)
            
                if form.is_valid():
                    form = form.save(commit=False)
                    form.reportedBy = request.user
                    form.reportedUser = user
                    form.reportReason = tweet
                    form.save()
                
                    return redirect('report_user',tweetId,userId)
            
                else:
                    return redirect('404page')
        
            else:
                context['tweet'] = tweet
                context['reportform'] = ReportUserForm()
            
                return render(request, 'report_user.html',context)
    else:
        return redirect('403page')

def deleteReport(request,tweetId,reportId):
    
    tweet = tinksPost.objects.filter(id=tweetId).first()

    if tweet:

        report = ReportManagement.objects.filter(id=reportId).first()

        if report and request.user.isApproved and request.user.id and tweet.user.id or request.user.is_superuser or request.user.is_moderator:
           
            messages.add_message(request,messages.SUCCESS,"Şikayet başarili bir şekilde silindi.")
            report.delete()
            

            return redirect('report_user',tweetId,reportId)
        
        else:
            return redirect('403page')
        
    else:
        return redirect('404page')       
# # User Banlama sistemi
@login_required(login_url='loginpage')
def banProfile(request,userId):

    if request.user.is_authenticated and request.user.is_admin() or request.user.is_moderator():
    
        context={}
        user=BlogUser.objects.filter(id=userId).first()
    
        if user is None:
         return redirect('403page')
    
        else:
            if request.method == 'POST':
                form = BanUserForm(request.POST)
            
                if form.is_valid():
                
                    form = form.save(commit=False)
                    form.authorizedPerson = request.user
                    form.bannedUser = user
                    user.isBanned = True
                    user.save()
                    form.save()
            
                    return redirect('usertweet',userId)
        
            else:   
                    context['user'] = user
                    context['banform'] = BanUserForm()

        if request.user.isBanned:
            return redirect('loginpage')
        
        else:
            return render(request, 'ban_user.html',context)
    else: 
        return redirect('403page')
 
# # Bani kaldirma Sistemi
@login_required(login_url='loginpage')
def removeBan(request,userId):

    if request.user.is_authenticated and request.user.is_admin() or request.user.is_moderator():
        context = {}

        user = BlogUser.objects.filter(id=userId).first()
    
        if user is None:
            return redirect('404page')
    
        else:
            if request.method == 'POST':
                form = RemoveBanForm(request.POST)
            
                if form.is_valid:

                    form = form.save(commit=False)
                form.authorizedUser = request.user
                form.removedbanUser = user
                user.isBanned = False
                user.save()
                form.save()

                return redirect('usertweet', userId)

    
            else:
                context['user'] = user
                context['removebanform'] = RemoveBanForm()
        
            return render(request,'remove_ban.html',context)
    else:
        return redirect('403page')    


# Bulunamayan sayfa hatası
def notFound(request):

    return render(request,'404.html')

# Yetersiz yetki ve izinsiz giriş hatası
def permissionDenied(request):

    return render(request,'403.html')

# Moderator rolü ekleme alani
def promoteModerator(request):

    user = BlogUser.objects.filter(id=request.user.id).first()

    modrole, id = Group.objects.get_or_create(name="Moderator")

    if user:
        user.groups.add(modrole)

        return redirect('homepage')

# API like versiyonu
def likeTweet(request, pk):
    
    response = {}
    if not request.user.is_authenticated:
        response['message'] = "User is not authenticated"
        return JsonResponse(response)
 
    tweet = tinksPost.objects.filter(id=pk).first()

    is_liked = tweet.likes.filter(user=request.user, post=tweet).first()

    if is_liked:
        tweet.likes.remove(is_liked)
        is_liked.delete()
        response['action'] = "unlike"
        return JsonResponse(response)
    else:

        liker = LikeTweet.objects.create(user = request.user,post=tweet)
        tweet.likes.add(liker)
        response['action'] = "liked"
    
        return JsonResponse(response)
