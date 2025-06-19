# Telefon Fiyat Tahmini: Makine Öğrenmesi ve AWS Entegrasyonu

Bu proje kapsamında, 20 farklı telefon özelliği içeren gerçek bir veri kümesi kullanılarak bir **makine öğrenmesi modeli** eğitilmiş ve **Amazon Web Services (AWS)** altyapısında dağıtılarak canlı tahmin sistemi oluşturulmuştur.

Veri analiz süreci Python ortamında gerçekleştirilmiş, veri temizliği ve özellik mühendisliği tamamlandıktan sonra eğitim ve test verileri **Amazon S3** bucket'ına yüklenmiştir. Model eğitimi **Amazon SageMaker** üzerinde yapılmış, eğitim sonrası model bir **endpoint** olarak yayına alınmıştır.

Tahmin sistemine erişim sağlamak amacıyla **AWS Lambda fonksiyonu** oluşturulmuş ve bu fonksiyon **API Gateway** üzerinden dış dünyaya açılmıştır. API aracılığıyla alınan tahmin sonuçları ise **MongoDB veritabanına** kaydedilmektedir.

Projede kullanılan datasetler, root klasöründeki datasets klasörünün içinde bulunmaktadır.

## 🔗 Önemli Bağlantılar

- 🎥 Proje Videosu (Bora): [https://youtu.be/P8G7fpsn-ig](https://youtu.be/P8G7fpsn-ig)
- 🔗 GitHub Reposu: [https://github.com/hsyntinaztepe/mlproject](https://github.com/hsyntinaztepe/mlproject)

---

Bu proje, uçtan uca veri analizi, model eğitimi, API oluşturma ve bulut altyapısı entegrasyonu içeren gerçek bir uygulamayı kapsamaktadır.
