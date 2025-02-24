# LOCAL SELF SERVICE NON-Commercial PDF to Markdown

Đây là server AI convert PDF thành Markdown không phục vụ kinh doanh thương mại, sử dụng nội bộ. 

## Yêu cầu môi trường cài đặt
- OS: Windows 10 / 11
- Có GPU Nvidia - hỗ trợ Torch GPU (GPU Nvidia phổ thông là đủ)
- Internet public để cài Torch GPU
- Python 3.12
- Cuda 12+ (12.6)

## Hướng dẫn cài đặt đối với Windows
- Phải đảm bảo đã cài đặt đầy đủ dịch vụ Nvidia cho GPU python Torch. Nếu không có đủ, thực hiện:
```base
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
```
- Copy toàn bộ models trong folder model vào `C:\Users\rd\AppData\Local\datalab\datalab\Cache\models`, thay `rd` là tên user của máy.
- Tại folder converter, thực hiện:
```base
pip install -r requirements.txt
```
- sau khi hoàn thành các bước trên thành công, có thể tắt internet và dùng mạng nội bộ để tránh update Windows và các vấn đề bảo mật.
- build exe
```commandline
pip install pyinstaller
pyinstaller --onefile --name converter_pdf_md_app main.py
```
