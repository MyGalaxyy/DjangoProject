"""
URL configuration for QuickMsg project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from QuickMsg_app.views import *

# url image ve video config.
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('base',basePage,name='basepage'),

    # Nav işlem pathleri
    path('',HomePage,name="homepage"),
    path('login',signIn,name='loginpage'),
    path('logout',signOut,name='logoutpage'),
    path('signup',signUp,name='signupPage'),

    # profil işlem pathleri
    path('profile/<userId>',userProfile,name='userprofile'),
    path('profile/<userId>/remove',removeAccount,name='profile_remove'),
    path('profilesettings',profileSettings,name='profilesettings'),

    # hata sayfası pathleri
    path('404error',notFound,name='404page'),
    path('403error',permissionDenied,name='403page'),

    # user tweet işlem pathleri
    path('usertweet/<userId>',usertweet,name='usertweet'),
    path('tweets/createtweet',createTweet,name='create_tweet'),
    path('usertweet/<tweetId>/delete',deleteTweet,name='delete_tweet'),
    path('updatetweet/<tweetId>/update',updateTweet,name='update_tweet'),

    # user yorum işlem pathleri
    path('createcomment/<tweetId>/comment',createComment,name='create_comment'),
    path('comment/<commentId>/update',updateComment,name='update_comment'),
    path('comment/<tweetId>/delete/<commentId>',deleteComment,name='delete_comment'),

    # begeni path i
    # path('tweetlike/<int:pk>',tweetLike,name='tweet_like'),

    # şikayet işlem pathleri
    path('reportuser/<tweetId>/report/<userId>',reportUser,name='report_user'),
    path('reportuser/<tweetId>/reportdelete/<reportId>',deleteReport,name='delete_report'),

    # ban işlem pathleri
    path('banuser/<userId>/ban',banProfile,name='ban_user'),
    path('removebanuser/<userId>/removeban',removeBan,name='remove_ban'),

    #mod alani
    path('promote',promoteModerator,name='promotemod'),

     # begeni api path'i
    path("api/v1/tweets/<int:pk>/like", likeTweet, name="tweet_like" ),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

