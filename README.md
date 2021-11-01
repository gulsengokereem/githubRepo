# githubRepo  

**bot_nycwggk1**


  Linkte verilen [Google linki]( https://www.nytimes.com/crosswords/game/mini )
bulmacanın  "Across" ve "Down" başlıkları altında yer alan  ip uçlarının verilerini çekip işlemeye yarayan Python kodları mevcuttur.

  Öncelikle  sistem oluşturma, hata ayıklama ve çalıştırma için log kaydı yapılmıştır..Bunun için logging kütüphanesini import ediyoruz.
Web üzerindeki isteklerimizi yönetebilmemiz için Request modülünü import ediyoruz.BeautifulSoup modülü ile bir kaynak içerisindeki HTML kodlarını ayrıştırıp sadece istediğimiz alanları kesmemize yardımcı olduğu için BeautifulSoup modülünüde import ediyorz.

  Html i parçalamak için `soup=BeautifulSoup(html_icerigi,"html.parser")` kodunu kullandık.Parçalamayı url de bulunan tüm verilerden ziyade sadece istediğimiz verileri çekmek için kullanıyoruz.Parçalamadan sonra çekeceğimiz verilerin olduğu bölümün etiketini  `for i in soup.find_all("li",{"class":"Clue-li--1JoPu"}):` kodu ile belirttik.
  
  Across ve Down ayrımı için dizi oluşturulmuştur.Tüm ip uçlarının ekrana yazdırılması için de for döngüsü kullanılmıştır.
  






