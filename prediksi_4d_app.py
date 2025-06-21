import streamlit as st
import random
import math
from collections import Counter
import io

def prediksi_4d(angka_4d):
    hasil_digit = []
    for i, digit_char in enumerate(str(angka_4d)):
        digit = int(digit_char)
        log_value = math.log(digit) if digit != 0 else 0
        nilai = (log_value + (i + 1)) * 7
        dua_digit_akhir = int(str(int(nilai))[-2:].zfill(2))
        hasil_digit.append(str(dua_digit_akhir).zfill(2))

    prediksi1 = ''.join(hasil_digit)
    prediksi2 = ''.join(hasil_digit[::-1])
    prediksi3 = hasil_digit[1] + hasil_digit[3] + hasil_digit[0] + hasil_digit[2]

    return [prediksi1, prediksi2, prediksi3]

# UI
st.title("🔮 Prediksi Togel 4D - Algoritma + Logaritma")

user_input = st.text_input("Masukkan angka 4D (opsional, misal: 7345):", max_chars=4)

semua_angka = []
semua_hasil = []

if st.button("🔮 Prediksi"):
    st.markdown("### Hasil Prediksi")
    if user_input and user_input.isdigit() and len(user_input) == 4:
        angka_manual = int(user_input)
        hasil = prediksi_4d(angka_manual)
        semua_angka.append(angka_manual)
        semua_hasil.append(hasil)

        st.subheader(f"🎰 Prediksi untuk angka: {angka_manual}")
        st.write(f"• Prediksi 1: {hasil[0]}")
        st.write(f"• Prediksi 2: {hasil[1]}")
        st.write(f"• Prediksi 3: {hasil[2]}")

    else:
        for i in range(10):
            angka_acak = random.randint(1000, 9999)
            hasil = prediksi_4d(angka_acak)
            semua_angka.append(angka_acak)
            semua_hasil.append(hasil)

            st.subheader(f"🎲 Angka Acak #{i+1}: {angka_acak}")
            st.write(f"• Prediksi 1: {hasil[0]}")
            st.write(f"• Prediksi 2: {hasil[1]}")
            st.write(f"• Prediksi 3: {hasil[2]}")

    # Analisis
    semua_prediksi = [item for sublist in semua_hasil for item in sublist]
    semua_digit = ''.join(semua_prediksi)
    hitung_digit = Counter(semua_digit)
    ranking = hitung_digit.most_common()
    angka_tertinggi = ranking[0][0] if ranking else "-"

    st.markdown("---")
    st.subheader("📊 Analisis Angka Dominan")
    for digit, jumlah in ranking:
        st.write(f"• Angka {digit} muncul sebanyak {jumlah} kali")
    st.success(f"🎯 Angka paling dominan: {angka_tertinggi}")

    # Tombol simpan file
    if st.button("⬇️ Simpan Hasil ke File (.txt)"):
        buffer = io.StringIO()
        buffer.write("=== HASIL PREDIKSI 4D ===\n\n")
        for i, angka in enumerate(semua_angka):
            hasil = semua_hasil[i]
            buffer.write(f"[{i+1}] Angka Asal : {angka}\n")
            buffer.write(f"     Prediksi 1: {hasil[0]}\n")
            buffer.write(f"     Prediksi 2: {hasil[1]}\n")
            buffer.write(f"     Prediksi 3: {hasil[2]}\n\n")
        buffer.write("=== ANALISIS ANGKA DOMINAN ===\n")
        for digit, jumlah in ranking:
            buffer.write(f"Angka {digit}: {jumlah} kali\n")
        buffer.write(f"\nAngka Paling Dominan: {angka_tertinggi}\n")

        st.download_button("📥 Download Hasil", buffer.getvalue(), file_name="prediksi4d.txt")
