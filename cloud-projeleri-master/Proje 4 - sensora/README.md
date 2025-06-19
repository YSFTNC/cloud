# IoT Gerçek Zamanlı Veri İşleme Sistemi

Bu proje, **Google Cloud Platform (GCP)** üzerinde gerçek zamanlı IoT sensör verilerinin toplanması, işlenmesi ve görselleştirilmesi için geliştirilmiştir. Sensör simülatörü her 5 saniyede bir sıcaklık ve nem verisi üretir ve **Pub/Sub** aracılığıyla sıraya alınır. **Cloud Functions (Gen2)** kullanılarak veriler filtrelenir (değişim %5’ten azsa kaydedilmez) ve hem **Firestore** (gerçek zamanlı erişim) hem de **BigQuery** (analiz) veritabanlarına kaydedilir.

Toplanan veriler, **Looker Studio** üzerinden hazırlanan canlı bir kontrol paneli (dashboard) ile izlenebilir. Sistem tamamen serverless çalışır, ölçeklenebilir yapıdadır ve GCP’nin IAM servis hesapları ile güvenlik sağlanmıştır.

Projede IoT sensör verileri, scriptle üretildiği için, datasets klasöründe data bulundurulmasına gerek yoktur.

## 🔗 Önemli Bağlantılar

- 🎥 Proje Videosu (Bora): [https://youtu.be/YTwNlZJRh4k](https://youtu.be/YTwNlZJRh4k)
- 📊 Canlı Dashboard: [Looker Studio](https://lookerstudio.google.com/reporting/95e13dc5-2708-4148-885f-037f6f775e4c/page/t2HMF)
- 🔗 Orijinal GitHub Reposu: [github.com/brckfrc/sensora](https://github.com/brckfrc/sensora)

---
