# DjangoProject

# QuickMsg App
QuickMsg uygulaması kullanıcıların anlık mesaj, post paylaşıp, yorum atabildikleri bir uygulamadır.

## Amacı
Amacı insanların kolay üye olup paylaşmak istedikleri postları , düşünceleri anlık olarak paylaşabilmelerini sağlamak ve bu şekilde giderek büyütülebilecek bir sosyal iletişim ağı oluşturmaktır.

## İçerdiği Özellikler;

* Giriş yapma , Kayıt olma sistemi
* Kullanıcı profil bilgileri
* Kullanıcı profil bilgileri güncellemek (değiştirmek)
* Kullanıcı hesap silme(aktifsizleştirme)
* Post paylaşabilmek,silebilmek,düzenleyebilmek,beğeni ve yorum yapabilmek
* Yapılan yorumları düzenleyebilmek ve silebilmek
* Rahatsız olunan tweet paylaşımları için şikayet oluşturabilmek
* Anasayfa da kullanıcıların isimlerine tıklayarak onların tweetlerine ulaşım sağlayabilmek
* Admin Paneli
* Admin tarafından kullanıcı onaylama
* Admin ve Moderator özel html'leri, tüm postları,yorumları görebilir,silebilir ve düzenleyebilir
* Kullanıcı Banlama (sadece Admin ve Moderator tarafından kullanabilir)
* Admin kendi seçtiği kullanıcıyı moderator olarak atayabilir

## Not

* Kaydı onaylanmayan kullanıcı tweetleri okuma hariç diğer uygulama özelliklerini kullanamaz(post göndermekte dahil). Kullanabilmesi için admin tarafından kayıt onayı gereklidir.

* Şikayet edilen kullanici, şikayet edilen tweet ve neden, şikayet eden kullanıcı admin sisteminde gözükür.

* Şikayet form kısmında kullanıcı sadece kendi yaptığı şikayetleri görebilir ve silebilir(Başka kullanıcıların şikayetlerini veya kendisine yapılan şikayetleri göremez) , bütün şikayetleri total sayısı da dahil olmak üzere görebilme ve silebilme yetkisi sadece admin ve moderator e aittir. 

* Banlanan kullanıcı sistemden atılır.


* Hesabını silen kullanıcı hesabı aktifsizleştirmiş olur.

* Iconlar internette online olunmazsa gözükmez.


## Görsel Örnek
### Anasayfa
![Anasayfa](https://github.com/MyGalaxyy/DjangoProject/assets/132202847/55cdd932-88d5-4def-a5c2-8ba020be9104)

### Şikayet Bildiri Sayfası
![ŞikayetBildiri](https://github.com/MyGalaxyy/DjangoProject/assets/132202847/ea1ff3aa-b99e-4e0a-a418-f274aaab795a)

### Kullanıcını kendi tweetlerini gösteren sayfa 
![Usertweet](https://github.com/MyGalaxyy/DjangoProject/assets/132202847/06e5627e-63df-4693-8f47-264f46b2d2e4)

### Yorum Yapma
![YorumYapma](https://github.com/MyGalaxyy/DjangoProject/assets/132202847/df01063d-fcae-401a-9ae6-54360745fefc)

