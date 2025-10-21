# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 08:40:42 2025
@author: adity
"""

#!/usr/bin/env python3
"""
Aplikasi GUI Steganografi Gambar (LSB)
Fitur:
 - Menyembunyikan teks ke dalam gambar (Encode)
 - Membaca teks tersembunyi dari gambar (Decode)
"""

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

# =======================
# Fungsi bantu bit <-> byte
# =======================
def to_bits(data_bytes):
    bits = []
    for b in data_bytes:
        for i in range(7, -1, -1):
            bits.append((b >> i) & 1)
    return bits

def from_bits(bits):
    out = bytearray()
    for i in range(0, len(bits), 8):
        byte = 0
        for j in range(8):
            byte = (byte << 1) | bits[i + j]
        out.append(byte)
    return bytes(out)

# =======================
# Encode LSB
# =======================
def embed_lsb(cover_path, stego_path, message):
    img = Image.open(cover_path).convert('RGBA')
    pixels = list(img.getdata())

    payload_bytes = message.encode('utf-8')
    payload_len = len(payload_bytes)

    # header 4 byte = panjang pesan
    header = payload_len.to_bytes(4, 'big')
    all_bytes = header + payload_bytes
    bits = to_bits(all_bytes)

    capacity = len(pixels) * 3
    if len(bits) > capacity:
        raise ValueError("Pesan terlalu besar untuk gambar ini!")

    new_pixels = []
    bit_idx = 0
    for (r, g, b, a) in pixels:
        if bit_idx >= len(bits):
            new_pixels.append((r, g, b, a))
            continue
        r_new = (r & ~1) | bits[bit_idx]; bit_idx += 1
        g_new = (g & ~1) | (bits[bit_idx] if bit_idx < len(bits) else 0); bit_idx += 1
        b_new = (b & ~1) | (bits[bit_idx] if bit_idx < len(bits) else 0); bit_idx += 1
        new_pixels.append((r_new, g_new, b_new, a))

    stego_img = Image.new(img.mode, img.size)
    stego_img.putdata(new_pixels)
    stego_img.save(stego_path, 'PNG')
    return stego_path

# =======================
# Decode LSB
# =======================
def extract_lsb(stego_path):
    img = Image.open(stego_path).convert('RGBA')
    pixels = list(img.getdata())

    bits = []
    for (r, g, b, a) in pixels:
        bits.extend([r & 1, g & 1, b & 1])

    header_bits = bits[:32]
    header_bytes = from_bits(header_bits)
    payload_len = int.from_bytes(header_bytes, 'big')

    payload_bits = bits[32:32 + payload_len * 8]
    payload_bytes = from_bits(payload_bits)

    try:
        message = payload_bytes.decode('utf-8')
    except UnicodeDecodeError:
        message = "<data biner tidak terbaca>"
    return message

# =======================
# GUI
# =======================
def pilih_gambar_encode():
    path = filedialog.askopenfilename(
        title="Pilih Gambar untuk Disisipi",
        filetypes=[("Gambar PNG", "*.png"), ("Gambar BMP", "*.bmp"), ("Semua File", "*.*")]
    )
    if path:
        entry_encode_path.delete(0, tk.END)
        entry_encode_path.insert(0, path)

def pilih_gambar_decode():
    path = filedialog.askopenfilename(
        title="Pilih Gambar yang Mengandung Pesan Rahasia",
        filetypes=[("Gambar PNG", "*.png"), ("Gambar BMP", "*.bmp"), ("Semua File", "*.*")]
    )
    if path:
        entry_decode_path.delete(0, tk.END)
        entry_decode_path.insert(0, path)

def proses_encode():
    cover = entry_encode_path.get().strip()
    pesan = text_pesan.get("1.0", tk.END).strip()
    if not cover:
        messagebox.showwarning("Peringatan", "Pilih gambar terlebih dahulu.")
        return
    if not pesan:
        messagebox.showwarning("Peringatan", "Masukkan pesan yang ingin disembunyikan.")
        return
    try:
        hasil = embed_lsb(cover, "foto_tersisip.png", pesan)
        messagebox.showinfo("Berhasil", f"Pesan disisipkan!\nGambar disimpan sebagai:\n{hasil}")
    except Exception as e:
        messagebox.showerror("Error", f"Gagal menyisipkan pesan:\n{e}")

def proses_decode():
    stego = entry_decode_path.get().strip()
    if not stego:
        messagebox.showwarning("Peringatan", "Pilih gambar yang ingin dibaca pesannya.")
        return
    try:
        pesan = extract_lsb(stego)
        text_hasil.delete("1.0", tk.END)
        text_hasil.insert(tk.END, pesan)
    except Exception as e:
        messagebox.showerror("Error", f"Gagal membaca pesan:\n{e}")

# =======================
# Tampilan GUI
# =======================
root = tk.Tk()
root.title("Aplikasi Steganografi Gambar (LSB) - Encode & Decode")
root.geometry("520x520")
root.resizable(False, False)

# ------------------ Bagian Encode ------------------
frame1 = tk.LabelFrame(root, text="🔐 SISIPKAN PESAN (Encode)", font=("Arial", 10, "bold"))
frame1.pack(fill="both", expand=True, padx=10, pady=5)

tk.Label(frame1, text="Pilih Gambar:").pack(anchor="w", padx=10, pady=3)
frame_file1 = tk.Frame(frame1)
frame_file1.pack(padx=10)
entry_encode_path = tk.Entry(frame_file1, width=45)
entry_encode_path.pack(side=tk.LEFT, padx=5)
tk.Button(frame_file1, text="Browse", command=pilih_gambar_encode).pack(side=tk.LEFT)

tk.Label(frame1, text="Pesan Rahasia:").pack(anchor="w", padx=10, pady=3)
text_pesan = tk.Text(frame1, height=5, width=55)
text_pesan.pack(padx=10, pady=5)

tk.Button(frame1, text="Sisipkan Pesan", command=proses_encode,
          bg="#007acc", fg="white", font=("Arial", 10, "bold")).pack(pady=5)

# ------------------ Bagian Decode ------------------
frame2 = tk.LabelFrame(root, text="🔎 BACA PESAN (Decode)", font=("Arial", 10, "bold"))
frame2.pack(fill="both", expand=True, padx=10, pady=5)

tk.Label(frame2, text="Pilih Gambar:").pack(anchor="w", padx=10, pady=3)
frame_file2 = tk.Frame(frame2)
frame_file2.pack(padx=10)
entry_decode_path = tk.Entry(frame_file2, width=45)
entry_decode_path.pack(side=tk.LEFT, padx=5)
tk.Button(frame_file2, text="Browse", command=pilih_gambar_decode).pack(side=tk.LEFT)

tk.Button(frame2, text="Baca Pesan Rahasia", command=proses_decode,
          bg="#28a745", fg="white", font=("Arial", 10, "bold")).pack(pady=5)

tk.Label(frame2, text="Hasil Pesan:").pack(anchor="w", padx=10)
text_hasil = tk.Text(frame2, height=5, width=55)
text_hasil.pack(padx=10, pady=5)

root.mainloop()

