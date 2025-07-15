

# StyleFusionAI

This project enables users to create stylized artworks in the styles of famous painters (Monet, Van Gogh, Munch) by either generating visual scenes from emotional or descriptive text or uploading their own images.

The system integrates GPT-4 Turbo, Stable Diffusion, and CUT (Contrastive Unpaired Translation) models to perform style transfer and image generation tasks.


## Features

-Text-to-scene generation from emotional or descriptive input (GPT-powered)
-Visual scene creation using Stable Diffusion
-Style transfer using CUT model in Monet, Van Gogh, or Munch styles
-Style transformation of user-uploaded images
-User-friendly web interface built with Flask

## Style Transfer Model Training

Style transfer is implemented using the CUT model trained separately for each artist: Monet, Van Gogh, and Munch.



## Training Environment

Model training was conducted on the following environment:

-1 x NVIDIA A100 SXM GPU (RunPod)
-16 vCPUs, 251 GB RAM
-PyTorch 2.1, CUDA 11.8, Ubuntu 22.04
-Storage: 20 GB disk + 20 GB pod volume
-Environment: On-Demand – Secure Cloud
-SSH access via Visual Studio Code


## Training Data

- `trainA`: Real-world images (landscapes, portraits, nature scenes, etc.)
- `trainB`: Paintings of the selected artist
-  Image resolution: 512×512 pixel
  


## Training Parameters

For Monet and Munch:
bash
--dataroot ./datasets/monet_style \
--name cut_monet_final \
--model cut \
--n_epochs 150 \
--n_epochs_decay 150 \
--batch_size 2 \
--load_size 512 --crop_size 512 \
--lambda_identity 0.5 \
--gpu_ids 0

For Van Gogh:
bash
--dataroot ./datasets/monet_style \
--name cut_monet_final \
--model cut \
--n_epochs 150 \
--n_epochs_decay 150 \
--batch_size 2 \
--load_size 512 --crop_size 512 \
--lambda_identity 1 \
--gpu_ids 0

##  Setup Instructions

1. Clone the repository:

bash
git clone https://github.com/haticenuryalman/bitirme_projesi_.git
cd bitirme_projesi_

2. Download required files from Google Drive:
Due to GitHub file size limitations, some files are stored externally.
Access the missing files here:  
https://drive.google.com/drive/folders/1DISV_y1VAWoDyVXgU8dsC7gF5Nq-v23-?usp=sharing

3.(Optional) Create a virtual environment:
python -m venv venv
source venv/bin/activate  # (On Windows : venv\Scripts\activate)

4. Install dependencies:
pip install -r requirements.txt

5. Add your OpenAI API key to a .env file:
OPENAI_API_KEY=your_openai_key_here

6. Run the application:
python app.py

Visit the app at:  
http://localhost:5000







