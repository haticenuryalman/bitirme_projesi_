# bitirme_projesi_

# Emotion2Art: Duygusal Metinlerden Sanatçı Stilinde Görsel Üretim

Bu proje, kullanıcıların yazdığı **duygusal metinleri** veya yüklediği **görselleri** alarak, ünlü sanatçıların (Monet, Van Gogh, Munch) tarzlarında stilize edilmiş sanat eserleri üretmelerini sağlar. 

Proje, **GPT-4 Turbo**, **Stable Diffusion** ve **CUT (Contrastive Unpaired Translation)** modellerinin entegrasyonu ile çalışmaktadır.

🔗 GitHub Sayfası: [https://github.com/haticenuryalman/bitirme_projesi_](https://github.com/haticenuryalman/bitirme_projesi_)

---

##  Özellikler

- Duygusal veya betimleyici metinden sahne üretimi (GPT destekli)
- Stable Diffusion ile metne uygun görsel üretimi
- Monet, Van Gogh veya Munch stilinde CUT modeli ile stil aktarımı
- Kullanıcının yüklediği herhangi bir görselin sanatçı stiline dönüştürülmesi
- Kullanıcı dostu Flask web arayüzü

---
## Kurulum

1. Projeyi GitHub'dan klonlayın:
git clone https://github.com/haticenuryalman/bitirme_projesi_.git
cd bitirme_projesi_

2. Gerekli dosyaları Drive'dan indirin:
Proje boyutu kısıtlamalarından dolayı gerekli olan tüm dosyalar GitHub’a yüklenememiştir. Eksik dosyalar için aşağıdaki Google Drive bağlantısını kullanabilirsiniz:

📁 Drive Linki:
https://drive.google.com/drive/folders/1DISV_y1VAWoDyVXgU8dsC7gF5Nq-v23-?usp=sharing

3.Sanal ortam oluşturun (isteğe bağlı):
python -m venv venv
source venv/bin/activate  # (Windows için: venv\Scripts\activate)

4. Gereksinimleri yükleyin:
pip install -r requirements.txt

5. OpenAI API anahtarını .env dosyasına ekleyin:
OPENAI_API_KEY=your_openai_key_here

6. Uygulamayı başlatın:
python app.py

Tarayıcıda şu adrese giderek uygulamayı kullanabilirsiniz:

http://localhost:5000
---

## 🧠 Model Eğitimi

Bu projede Monet, Van Gogh ve Munch için **CUT (Contrastive Unpaired Translation)** modeli kullanılarak stil transferi gerçekleştirilmiştir.

### 🎯 Eğitim Ortamı

Eğitim işlemleri aşağıdaki özelliklere sahip bir ortamda gerçekleştirilmiştir:

- **RunPod üzerinde 1 x NVIDIA A100 SXM GPU**
- 16 vCPU, 251 GB RAM
- Pytorch 2.1, CUDA 11.8, Ubuntu 22.04
- Depolama: 20 GB disk + 20 GB pod volume
- Eğitim ortamı: **On-Demand – Secure Cloud**
- SSH bağlantısı: VS Code üzerinden
- 
### 🗂️ Eğitim Verisi

- `trainA`: Gerçek hayat görselleri (manzara, portre, doğa sahneleri vb.).
- `trainB`: Sanatçının tabloları
- Görsel boyutu: 512×512 piksel
- 
### ⚙️ Eğitim Parametreleri (örnek)
Monet ve Munch için:
```bash
--dataroot ./datasets/monet_style \
--name cut_monet_final \
--model cut \
--n_epochs 150 \
--n_epochs_decay 150 \
--batch_size 2 \
--load_size 512 --crop_size 512 \
--lambda_identity 0.5 \
--gpu_ids 0

Van Gogh için: 
```bash
--dataroot ./datasets/monet_style \
--name cut_monet_final \
--model cut \
--n_epochs 150 \
--n_epochs_decay 150 \
--batch_size 2 \
--load_size 512 --crop_size 512 \
--lambda_identity 1 \
--gpu_ids 0



Dosyaları bu drive’dan aldıktan sonra proje dizinine yerleştirerek aşağıdaki adımlarla devam edebilirsiniz.

Proje boyutu kısıtlamalarından dolayı gerekli olan her şey GitHub’a yüklenememiştir. Dosyalara bu drive linkinden ulaşabilirsiniz: https://drive.google.com/drive/folders/1DISV_y1VAWoDyVXgU8dsC7gF5Nq-v23-?usp=sharing

Drive dan projeyi çektikten sonra 
python app.py 
komutu ile kolayca projeyi çalıştırabilirsiniz.
