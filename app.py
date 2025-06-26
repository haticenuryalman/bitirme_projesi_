from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
import uuid
from dotenv import load_dotenv

# Yardımcı fonksiyonlar
from utils.generate_image import generate_image_from_text
from utils.style_transfer import apply_style_transfer

# Ortam değişkenlerini yükle (.env içinden HF_TOKEN vs.)
load_dotenv()

# Flask uygulaması
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['OUTPUT_FOLDER'] = 'static/outputs'

# Gerekli klasörleri oluştur
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Cümleyle mi, resimle mi üretim yapacağız?
        mode = request.form.get('mode')  # "text" ya da "image"
        artist = request.form.get('artist')  # "monet", "vangogh", "munch"

        # ✅ Cümle ile üretim
        if mode == "text":
            user_text = request.form.get('user_text')
            if not user_text:
                return render_template("index.html", output_image=None)
            output_path = generate_image_from_text(user_text, artist)

        # ✅ Görsel yükleyerek stil dönüşümü
        elif mode == "image":
            image = request.files['image']
            if not image:
                return render_template("index.html", output_image=None)

            # Dosya adını güvenli hale getir + benzersiz adlandır
            filename = secure_filename(image.filename)
            unique_filename = f"{uuid.uuid4().hex}_{filename}"
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)

            image.save(input_path)

            output_path = apply_style_transfer(input_path, artist)

        else:
            return render_template("index.html", output_image=None)

        return render_template("index.html", output_image=output_path)

    # GET isteğinde boş form göster
    return render_template("index.html", output_image=None)



@app.route("/info")
def info():
    return render_template("info.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860, debug=True)
