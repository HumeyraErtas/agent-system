# 🤖 Tool-Calling Agent Sistemi

## 📌 Proje Açıklaması

Bu projede, kullanıcının sorusunu anlayarak gerekli araçları (tool/API) doğru sırayla çağıran ve eksik bilgi durumunda kullanıcıdan veri isteyen bir **LLM Agent sistemi** geliştirilmiştir.

Sistem:

* Kullanıcı girdisini analiz eder
* Gerekli fonksiyonları (tools) belirler
* Bağımlı çağrıları doğru sırayla gerçekleştirir
* Sonucu doğal dilde kullanıcıya açıklar

---

## 🧠 Sistem Özellikleri

### 🔹 Araç (Tool) Kullanımı

Sistem, aşağıdaki 3 temel aracı kullanır:

#### 1. `get_user_details(email)`

* Kullanıcının email adresinden:

  * user_id
  * hesap durumu
* Hatalı email → exception fırlatır

---

#### 2. `get_recent_transactions(user_id, limit)`

* Kullanıcının son işlemlerini döndürür:

  * işlem ID
  * miktar
  * durum (success / failed)

---

#### 3. `check_fraud_reason(transaction_id)`

* Başarısız işlemin neden reddedildiğini döndürür

---

## 🔗 Bağımlı İstek (Chaining) Mekanizması

Sistem aşağıdaki adımları otomatik olarak gerçekleştirir:

```text id="j2f7k1"
Kullanıcı Sorusu
      ↓
Email Extraction
      ↓
get_user_details(email)
      ↓
get_recent_transactions(user_id)
      ↓
Başarısız işlem seçimi
      ↓
check_fraud_reason(transaction_id)
      ↓
LLM ile açıklama üretimi
```

---

## ⚙️ Veri Yapısı (Mock Database)

Gerçek bir veritabanı yerine Python sözlükleri kullanılmıştır:

* kullanıcı bilgileri
* işlem kayıtları
* fraud nedenleri

Bu yapı sayesinde sistem:

* kolay test edilebilir
* dinamik veri değişikliklerine açıktır

---

## ⚙️ Kurulum

```bash id="k5p3vz"
git clone <repo-url>
cd agent-system

py -m pip install -r requirements.txt
```

---

## 🔐 Ortam Değişkeni

`.env` dosyası oluşturulmalıdır:

```env id="xk3z8v"
GOOGLE_API_KEY=your_api_key
```

API key:
👉 https://aistudio.google.com/app/apikey

---

## ▶️ Çalıştırma

```bash id="m2z9p4"
py main.py
```

---

## 🧪 Test Senaryoları

### ✔ Test 1 — Tam zincir (chaining)

```text id="1d9a6q"
ali@sirket.com hesabımla yaptığım ödeme neden reddedildi?
```

👉 Sistem:

* user bulur
* işlemleri çeker
* başarısız işlemi seçer
* nedenini açıklar

---

### ✔ Test 2 — Eksik parametre

```text id="0p3s2l"
Ödemem neden reddedildi?
```

👉 Beklenen:

* Sistem email ister

---

### ✔ Test 3 — Hata yönetimi

```text id="7n2k8d"
fake@mail.com işlemlerim neden başarısız?
```

👉 Beklenen:

* Kullanıcı bulunamadı mesajı

---

## ⚙️ Mimari Kararlar

### Neden mock veri kullanıldı?

Gerçek veritabanı yerine:

* hızlı geliştirme
* test edilebilirlik
* bağımsız çalışma

---

### Neden tool-based yapı?

* Modülerlik sağlar
* Fonksiyonlar bağımsız test edilebilir
* Gerçek sistemlere kolay entegre edilir

---

### Neden Gemini kullanıldı?

* Güçlü doğal dil üretimi
* Açıklayıcı cevap üretme
* Kullanıcıya anlaşılır sonuç sunma

---

## 🚀 Gelecek Geliştirmeler

* Gerçek veritabanı entegrasyonu (PostgreSQL)
* LangChain / LangGraph ile gerçek agent
* API servis (FastAPI)
* Logging & monitoring
* Çoklu tool seçimi (dynamic tool calling)

---

## 📌 Sonuç

Bu proje:

* Tool-calling agent mimarisi
* Bağımlı istek zinciri (chaining)
* Eksik parametre yönetimi
* Hata yakalama ve kullanıcıya açıklama

gibi modern LLM agent sistemlerinin temel prensiplerini göstermektedir.

---
