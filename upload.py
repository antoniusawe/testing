#!/usr/bin/env python
# coding: utf-8

# In[6]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Judul aplikasi
st.title("File Uploader App")

# Fungsi untuk mengunggah file
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "txt"])

# Jika file sudah diunggah
if uploaded_file is not None:
    # Cek apakah file CSV
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
        st.write("File CSV berhasil diunggah:")
        st.write(df)
    # Cek apakah file Excel
    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)
        st.write("File Excel berhasil diunggah:")
        st.write(df)
    # Cek apakah file TXT
    elif uploaded_file.name.endswith('.txt'):
        string_data = uploaded_file.read().decode("utf-8")
        st.write("File TXT berhasil diunggah:")
        st.text(string_data)
    else:
        st.write("Jenis file tidak didukung")

    # Menampilkan dua tombol setelah file diunggah
    if st.button('Visualisasi'):
        if 'Usia' in df.columns:  # Contoh visualisasi untuk kolom Usia
            st.write("Visualisasi Histogram Usia:")
            fig, ax = plt.subplots()
            ax.hist(df['Usia'], bins=10, color='skyblue', edgecolor='black')
            ax.set_xlabel('Usia')
            ax.set_ylabel('Jumlah')
            ax.set_title('Distribusi Usia')
            st.pyplot(fig)
        else:
            st.write("Kolom 'Usia' tidak ditemukan di data")

    if st.button('Describe Data'):
        st.write("Deskripsi Statistik Data:")
        st.write(df.describe())

