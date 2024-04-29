import streamlit as st 


#Tampilan Halaman Web
st.title("Kalkulator Normalitas dan Molaritas")

#Input Data
mg = st.number_input("Masukkan nilai massa titrat (mg)", min_value= 0.01)
mL = st.number_input("Masukkan nilai volume titran (mL)", min_value= 0.01)
fp = st.number_input("Masukkan nilai faktor pengali", min_value= 0.01 ) 
BE = st.number_input("Masukkan nilai bobot ekuivalen (mg/mgrek)", min_value= 0.01)
BM = st.number_input("Masukkan nilai bobot molekul (mg/mmol)", min_value= 0.01)

#Menghitung Normalitas 
if st.button("Normalitas"):
    Normalitas_Larutan = (mg / fp) / (BE * mL)
    st.success (f"Normalitas Larutan Adalah =  {Normalitas_Larutan} N")
        
#Halaman Molaritas
if st.button("Molaritas"):
    Molaritas_Larutan = (mg / fp) / (BM * mL)
    st.success (f"Molaritas Larutan Adalah = {Molaritas_Larutan} M")
    

