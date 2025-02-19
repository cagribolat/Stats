import tkinter as tk
from tkinter import filedialog
import subprocess

# Başlangıç fonksiyonu
def convert_video():
    input_file = entry_input.get()
    output_file = entry_output.get()
    crf_value = crf_slider.get()
    bitrate_value = bitrate_slider.get()

    if not input_file or not output_file:
        label_status.config(text="Lütfen hem giriş dosyasını hem de çıkış dosyasını belirtin.", fg="red")
        return

    # FFmpeg komutunu oluştur
    command = [
        "ffmpeg", 
        "-i", input_file, 
        "-c:v", "h264_amf", 
        "-crf", str(crf_value),  # CRF değeri kullanıcıdan alınıyor
        "-pix_fmt", "yuv420p", 
        "-b:v", f"{bitrate_value}k",  # Bitrate değeri kullanıcıdan alınıyor
        "-c:a", "copy", 
        output_file
    ]

    try:
        subprocess.run(command, check=True)
        label_status.config(text="Dönüştürme işlemi başarılı!", fg="green")
    except subprocess.CalledProcessError:
        label_status.config(text="Bir hata oluştu. Lütfen dosya yolunu kontrol edin.", fg="red")

# Dosya seçme fonksiyonu
def select_input_file():
    file_path = filedialog.askopenfilename(title="Select Input File", filetypes=(("MKV Files", "*.mkv"), ("All Files", "*.*")))
    entry_input.delete(0, tk.END)
    entry_input.insert(0, file_path)

def select_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".mkv", title="Select Output File", filetypes=(("MKV Files", "*.mkv"), ("All Files", "*.*")))
    entry_output.delete(0, tk.END)
    entry_output.insert(0, file_path)

# Ana pencere
root = tk.Tk()
root.title("FFmpeg Video Converter ")
root.geometry("500x400")
root.config(bg="#2d2d2d")

# Başlık
label_title = tk.Label(root, text=" ", font=("Arial", 16, "bold"), fg="white", bg="#2d2d2d")
label_title.pack(pady=10)

# Giriş dosyası için etiket ve kutu
label_input = tk.Label(root, text="Select Input File:", font=("Arial", 12), fg="white", bg="#2d2d2d")
label_input.pack(pady=5)
entry_input = tk.Entry(root, width=50, font=("Arial", 10))
entry_input.pack(pady=5)
button_browse_input = tk.Button(root, text="Dosya Seç", command=select_input_file, bg="#4CAF50", fg="white", font=("Arial", 10))
button_browse_input.pack(pady=5)

# Çıkış dosyası için etiket ve kutu
label_output = tk.Label(root, text="Select output location:", font=("Arial", 12), fg="white", bg="#2d2d2d")
label_output.pack(pady=5)
entry_output = tk.Entry(root, width=50, font=("Arial", 10))
entry_output.pack(pady=5)
button_browse_output = tk.Button(root, text="Dosya Seç", command=select_output_file, bg="#4CAF50", fg="white", font=("Arial", 10))
button_browse_output.pack(pady=5)

# CRF seçici (kaydırıcı)
label_crf = tk.Label(root, text="CRF Rating (Video Quality):", font=("Arial", 12), fg="white", bg="#2d2d2d")
label_crf.pack(pady=5)
crf_slider = tk.Scale(root, from_=0, to_=51, orient="horizontal", length=400, tickinterval=10, sliderlength=15)
crf_slider.set(28)  # Varsayılan CRF değeri
crf_slider.pack(pady=5)

# Bitrate seçici (kaydırıcı)
label_bitrate = tk.Label(root, text="Bitrate (kbps):", font=("Arial", 12), fg="white", bg="#2d2d2d")
label_bitrate.pack(pady=5)
bitrate_slider = tk.Scale(root, from_=500, to_=5000, orient="horizontal", length=400, tickinterval=500, sliderlength=15)
bitrate_slider.set(1500)  # Varsayılan bitrate değeri
bitrate_slider.pack(pady=5)

# Dönüştürme butonu
button_convert = tk.Button(root, text="Convert", command=convert_video, bg="#008CBA", fg="white", font=("Arial", 12, "bold"))
button_convert.pack(pady=20)

# Durum etiketi
label_status = tk.Label(root, text="", font=("Arial", 12), fg="white", bg="#2d2d2d")
label_status.pack(pady=10)

# Pencereyi başlat
root.mainloop()
