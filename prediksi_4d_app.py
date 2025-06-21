import streamlit as st
import random
import math
from collections import Counter

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

st.title("🔮 Prediksi Togel 4D - Algoritma + Logaritma")

if st.button("🎲 Generate 10 Angka Acak"):
    semua_prediksi = []

    for i in range(10):
        angka_acak = random.randint(1000, 9999)
        hasil = prediksi_4d(angka_acak)
        semua_prediksi.extend(hasil)

        st.subheader(f"🎰 Angka Acak #{i+1}: {angka_acak}")
        st.write(f"• Prediksi 1: {hasil[0]}")
        st.write(f"• Prediksi 2: {hasil[1]}")
        st.write(f"• Prediksi 3: {hasil[2]}")

    semua_digit = ''.join(semua_prediksi)
    hitung_digit = Counter(semua_digit)
    ranking = hitung_digit.most_common()

    st.markdown("---")
    st.subheader("📊 Analisis Angka Dominan (0–9)")
    for digit, jumlah in ranking:
        st.write(f"• Angka {digit}: {jumlah} kali")

    angka_tertinggi = ranking[0][0]
    st.success(f"🎯 Angka paling dominan adalah: **{angka_tertinggi}**")
