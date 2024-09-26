#!/usr/bin/env python
# coding: utf-8

# In[7]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul aplikasi
st.title("Silahkan Upload Data Karyawan")

# Fungsi untuk mengunggah file
uploaded_file = st.file_uploader("Pilih File", type=["csv", "xlsx", "txt"])

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

    # Tombol untuk menampilkan dashboard
    if st.button('Dashboard'):
        # Total number of employees
        total_employees = len(df)

        # Distribution by Employment Status
        employment_status_distribution = df['Employmentstatus'].value_counts()

        # Gender distribution
        gender_distribution = df['Gender'].value_counts()

        # Job Grade distribution
        job_grade_distribution = df['JG'].value_counts()

        # Work location distribution
        work_location_region_distribution = df['Region'].value_counts()

        # Tenure Calculation: Convert 'Join Date' to datetime and calculate tenure in years
        df['Join Date'] = pd.to_datetime(df['Join Date'], errors='coerce')
        df['Tenure (Years)'] = (pd.Timestamp.today() - df['Join Date']).dt.days / 365
        tenure_avg = df['Tenure (Years)'].mean()
        tenure_median = df['Tenure (Years)'].median()

        # Creating the dashboard

        st.subheader(f"Total Employees: {total_employees}")

        # Employment Status Distribution
        st.write("Distribution by Employment Status")
        fig, ax = plt.subplots()
        employment_status_distribution.plot(kind='pie', autopct='%1.1f%%', ax=ax, colors=sns.color_palette("Set2"))
        ax.set_ylabel('')
        # ax.set_title('Employment Status Distribution')
        st.pyplot(fig)

        # Gender Distribution
        st.write("Gender Distribution")
        fig, ax = plt.subplots()
        gender_distribution.plot(kind='bar', color=sns.color_palette("Set3"), ax=ax)
        ax.set_xlabel('Gender')
        ax.set_ylabel('Number of Employees')
        # ax.set_title('Gender Distribution')
        st.pyplot(fig)

        # Job Grade Distribution
        st.write("Job Grade Distribution")
        fig, ax = plt.subplots()
        job_grade_distribution.plot(kind='bar', color=sns.color_palette("Set1"), ax=ax)
        ax.set_xlabel('Job Grade')
        ax.set_ylabel('Number of Employees')
        # ax.set_title('Job Grade Distribution')
        st.pyplot(fig)

        # Work Location Distribution
        st.write("Work Location Distribution (Region)")
        fig, ax = plt.subplots()
        work_location_region_distribution.plot(kind='bar', color=sns.color_palette("Set2"), ax=ax)
        ax.set_xlabel('Region')
        ax.set_ylabel('Number of Employees')
        # ax.set_title('Work Location Distribution')
        st.pyplot(fig)

        # Tenure Distribution
        st.write("Distribution of Employee Tenure (Years)")
        fig, ax = plt.subplots()
        sns.histplot(df['Tenure (Years)'].dropna(), bins=20, color='green', ax=ax)
        ax.set_xlabel('Years of Tenure')
        ax.set_ylabel('Number of Employees')
        ax.set_title('Tenure Distribution')
        st.pyplot(fig)

        # Display average and median tenure
        st.write(f"Average Tenure: {tenure_avg:.2f} years")
        st.write(f"Median Tenure: {tenure_median:.2f} years")

    if st.button('Describe Data'):
        st.write("Deskripsi Statistik Data:")
        st.write(df.describe())

