#IMPORTACIONES#################################################################
import streamlit as st
import pandas as pd
import numpy as np
import datetime
import json
import time
import requests
import base64
from IPython.lib.display import FileLink
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
from PIL import Image
#CÓDIGO DE GRAFICOS############################################################
def lectura_grafico(filename):
    bd=pd.read_csv(filename,sep=";")
    eca=pd.read_csv("Limites_ECA.csv",sep=";")
   
    x1=bd["CO (ug/m3)"]
    x2=bd["H2S (ug/m3)"]
    x3=bd["NO2 (ug/m3)"]
    x4=bd["O3 (ug/m3)"]
    x5=bd["PM10 (ug/m3)"]
    x6=bd["PM2.5 (ug/m3)"]
    x7=bd["SO2 (ug/m3)"]
#CO
    eca1=eca["CO (ug/m3)"]
    eca1=np.ones(len(x1.values))*eca1.values
    data1 = {"CO (ug/m3)":x1.values,'Límite ECA':eca1}
    data_frame1 = pd.DataFrame(data1)
#H2S
    eca2=eca["H2S (ug/m3)"]
    eca2=np.ones(len(x2.values))*eca2.values
    data2 = {"H2S (ug/m3)":x2.values,'Límite ECA':eca2}
    data_frame2 = pd.DataFrame(data2)
#NO2
    eca3=eca["NO2 (ug/m3)"]
    eca3=np.ones(len(x3.values))*eca3.values
    data3 = {"NO2 (ug/m3)":x3.values,'Límite ECA':eca3}
    data_frame3 = pd.DataFrame(data3)
#O3
    eca4=eca["O3 (ug/m3)"]
    eca4=np.ones(len(x4.values))*eca4.values
    data4 = {"O3 (ug/m3)":x4.values,'Límite ECA':eca4}
    data_frame4 = pd.DataFrame(data4)
#PM10
    eca5=eca["PM10 (ug/m3)"]
    eca5=np.ones(len(x5.values))*eca5.values
    data5 = {"PM10 (ug/m3)":x5.values,'Límite ECA':eca5}
    data_frame5 = pd.DataFrame(data5)
#PM2.5
    eca6=eca["PM2.5 (ug/m3)"]
    eca6=np.ones(len(x6.values))*eca6.values
    data6 = {"PM2.5 (ug/m3)":x6.values,'Límite ECA':eca6}
    data_frame6 = pd.DataFrame(data6)
#SO2
    eca7=eca["SO2 (ug/m3)"]
    eca7=np.ones(len(x7.values))*eca7.values
    data7 = {"SO2 (ug/m3)":x7.values,'Límite ECA':eca7}
    data_frame7 = pd.DataFrame(data7)

    return data_frame1, data_frame2,data_frame3,data_frame4,data_frame5,data_frame6,data_frame7,bd
#DESCARGAR#####################################################################
def convert_df(df):
    return df.to_csv().encode('utf-8')

def cod_grafic_descargar(filename):
    x1, x2,x3,x4,x5,x6,x7,x8= lectura_grafico(filename)
    
    lista=('CO (ug/m3)', 'H2S (ug/m3)', 'NO2 (ug/m3)', 'O3 (ug/m3)', 'PM10 (ug/m3)','PM2.5 (ug/m3)','S02 (ug/m3)')
    options = st.multiselect('¿Qué parámetros desea ver?', lista)     
    
    if 'CO (ug/m3)' in options:
        st.line_chart(x1)     
    if 'H2S (ug/m3)' in options:    
        st.line_chart(x2)
    if 'NO2 (ug/m3)' in options:
        st.line_chart(x3)
    if 'O3 (ug/m3)' in options:
        st.line_chart(x4)
    if 'PM10 (ug/m3)' in options:
        st.line_chart(x5)
    if 'PM2.5 (ug/m3)' in options:
        st.line_chart(x6)
    if 'S02 (ug/m3)' in options:
        st.line_chart(x7)
    
    d1=convert_df(x8)
    st.write("**Eje de las ordenadas (y) : valores de concentración**")
    st.write("**Eje de las abscisas (x) : cantidad de datos**")
    st.download_button("Descargar {}".format(filename),d1,filename)    
#ANIMACIONES###################################################################
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
#BARRA LATERAL DE LA PÁGINA####################################################
with st.sidebar:
    selected = option_menu(
        menu_title= 'Menu principal',
        options = ['Inicio', 'Reporte 2020', 'Reporte 2021'],
        icons=['house','book','book'],
        menu_icon='cast',
        default_index=0,
        #orientation='horizontal',
    )
###############################################################################
###############################################################################    
if selected == 'Inicio':
###############################################################################
#ENCABEZADO DE LA PÁGINA#######################################################
    st.title('Calidad del aire de la Municipalidad de Miraflores')
    st.write("La base de datos del monitoreo de calidad del aire fueron realizados por la empresa QAIRA desde Julio 2020 hasta Marzo 2021.")
    st.write("QAIRA es una empresa peruana que se encarga del monitoreo constante de la calidad del aire a través de drones y módulos qHAWAX de última generación, con la finalidad de tomar acciones rápidas a favor del medio ambiente.")
############################################################################## 
    st.subheader("¿Por qué es importante la calidad del aire?") 
##############################################################################
    col1, col2 = st.columns(2)
    with col1:
        st.write("""La contaminación del aire ha cobrado reconocimiento y prominencia en las agendas globales.
                 En septiembre del 2015, la Asamblea General de las Naciones Unidas adoptó la Agenda 2030 para el Desarrollo Sostenible.""")  
        st.write("""Las partículas contaminantes pueden ingresar fácilmente a las vías respiratorias, provocando problemas crónicos a la salud. 
                 Por ello, es importante realizar un monitoreo de calidad del aire para conocer las concentraciones de los contaminantes atmosféricos y mantenrlos por dejabo de los Estándares de Calidad Ambiental para Aire.
                 """)
        st.write("**Fuente:** Calidad del aire - OPS/OMS | Organización Panamericana de la Salud. (2018). Paho.org. https://www.paho.org/es/temas/calidad-aire")

    with col2:
        st.write("Según la Organización Mundial de la Salud, 249.000 muertes prematuras podrían ser reconocidas por la contaminación del aire ambiente")
        #primera animación#############################################################   
        lottie_url_hello = "https://assets3.lottiefiles.com/packages/lf20_EyJRUV.json"
        lottie_hello = load_lottieurl(lottie_url_hello)
        st_lottie(lottie_hello)
#VIDEO REFLEXIVO###############################################################
    st.subheader("**¿Cómo afecta la contaminación del aire a nuestro cuerpo?**")    
    video_file = open('Cómo afecta la contaminación del aire a nuestro cuerpo.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    st.write("**Fuente**: BBC News Mundo. (2017). https://youtu.be/zvlHBfSBcKk")   
###############################################################################
###############################################################################         
if selected == 'Reporte 2020':       
###############################################################################
#MAPA MIRAFLORES###############################################################
    st.subheader("Puntos de muestreo")    
    st.write("**Se tomaron 5 puntos de muestreo, Av. Del Ejército, Av. José de la Riva Agüero, Av. Gral. Mendiburu, Av. Enrique Meiggs y el Tontódromo PUCP**")
    latlon=pd.read_csv("lat_lon_2020.csv",sep=";")
    df = pd.DataFrame(latlon,columns=['lat', 'lon'])
    st.map(df)
    st.write("**Leyenda**")
    st.write("""Av. Del Ejército (**AE**), 
             Av. José de la Riva Agüero (**AJ**), 
             Av. Gral. Mendiburu (**AG**), 
             Av. Enrique Meiggs (**AE**), 
             Tontódromo PUCP (**TP**)
             """)
#gif0##########################################################################
    st.subheader("Escala según ECA")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.subheader("Buena")
        file_ = open("qairito_buena.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
            
        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
            unsafe_allow_html=True,
        )     
    with col2:
        st.subheader("Moderado")
        file_ = open("qairito_moderada.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
            
        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
            unsafe_allow_html=True,
        )     
    with col3:
        st.subheader("Mala")
        file_ = open("qairito_mala.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
            
        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
            unsafe_allow_html=True,
        )    
    with col4:
        st.subheader("Cuidado")
        file_ = open("qairito_cuidado.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
            
        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
            unsafe_allow_html=True,
        )   
    st.write("**Fuente:** https://www.minam.gob.pe/wp-content/uploads/2016/07/RM-N°-181-2016-MINAM.pdf")
#BOTONES 1######################################################################
    lista1=('Julio AE', 'Agosto AE', 'Setiembre AE','Setiembre AJ', 'Octubre AG','Octubre AE', 'Noviembre AE','Noviembre AJ','Diciembre AG','Diciembre TP')
    options = st.multiselect('¿Qué mes desea ver? (eliga solo un mes)', lista1)   
################################################################################
    if "Julio AE" in options:
        st.header("Monitoreo de Julio 2020 : Av. del Ejército")
#gif1#########################################################################
        col1, col2, col3= st.columns(3)
        with col2:        
            file_ = open("qairito_moderada.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            
            st.markdown(
                f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
                unsafe_allow_html=True,
            )
###############################################################################
        cod_grafic_descargar("Monitoreo_julio_2020.csv")
###############################################################################
    if 'Agosto AE' in options:
        st.header("Monitoreo de Agosto 2020 : Av. del Ejército")
#gif2#########################################################################
        col1, col2, col3= st.columns(3)
        with col2:        
            file_ = open("qairito_moderada.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            
            st.markdown(
                f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
                unsafe_allow_html=True,
            )
############################################################################### 
        cod_grafic_descargar("Monitoreo_agosto_2020.csv")
###############################################################################        
    if 'Setiembre AE' in options:
        st.header("Monitoreo de Setiembre 2020 : Av. del Ejército")
#gif3#########################################################################
        col1, col2, col3= st.columns(3)
        with col2:        
            file_ = open("qairito_moderada.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            
            st.markdown(
                f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
                unsafe_allow_html=True,
            )
###############################################################################
        cod_grafic_descargar("Monitoreo_setiembre_2020_complejo_deportivo_manuel.csv") 
###############################################################################
    if 'Setiembre AJ' in options:
        st.header("Monitoreo de Setiembre 2020 : Av. José de la Riva Agüero")
#gif4#########################################################################
        col1, col2, col3= st.columns(3)
        with col2:        
            file_ = open("qairito_moderada.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            
            st.markdown(
                f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
                unsafe_allow_html=True,
            )
############################################################################### 
        cod_grafic_descargar("Monitoreo_setiembre_2020_ovalo_miraflores.csv") 
###############################################################################        
    if 'Octubre AG' in options:
        st.header("Monitoreo de Octubre 2020 : Av. Gral. Mendiburu")
#gif5#########################################################################
        col1, col2, col3= st.columns(3)
        with col2:        
            file_ = open("qairito_moderada.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            
            st.markdown(
                f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
                unsafe_allow_html=True,
            )
###############################################################################
        cod_grafic_descargar("Monitoreo_octubre_2020_complejo_deportivo_manuel.csv")
###############################################################################
    if 'Octubre AE' in options:        
        st.header("Monitoreo de Octubre 2020 : Av. Enrique Meiggs")
#gif6#########################################################################
        col1, col2, col3= st.columns(3)
        with col2:        
            file_ = open("qairito_mala.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            
            st.markdown(
                f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
                unsafe_allow_html=True,
            )
###############################################################################  
        cod_grafic_descargar("Monitoreo_octubre_2020_ovalo_miraflores.csv")   
###############################################################################        
    if 'Noviembre AE' in options:
        st.header("Monitoreo de Noviembre 2020 : Av. del Ejército")
#gif7#########################################################################
        col1, col2, col3= st.columns(3)
        with col2:        
            file_ = open("qairito_mala.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            
            st.markdown(
                f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
                unsafe_allow_html=True,
            )
###############################################################################
        cod_grafic_descargar("Monitoreo_Noviembre_2020_complejo_deportivo_manuel.csv") 
###############################################################################
    if 'Noviembre AJ' in options:        
        st.header("Monitoreo de Noviembre 2020 : Av. José de la Riva Agüero")
#gif8#########################################################################
        col1, col2, col3= st.columns(3)
        with col2:
            file_ = open("qairito_mala.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
             
            st.markdown(
                f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
                unsafe_allow_html=True,
                )
############################################################################### 
        cod_grafic_descargar("Monitoreo_Noviembre_2020_ovalo_miraflores.csv") 
###############################################################################        
    if 'Diciembre AG' in options:
        st.header("Monitoreo de Diciembre 2020 : Av. Gral. Mendiburu")
#gif9#########################################################################
        col1, col2, col3= st.columns(3)
        with col2:        
            file_ = open("qairito_moderada.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            
            st.markdown(
                f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
                unsafe_allow_html=True,
            )
###############################################################################
        cod_grafic_descargar("Monitoreo_Diciembre_2020_complejo_deportivo_manuel.csv")   
###############################################################################
    if 'Diciembre TP' in options:        
        st.header("Monitoreo de Diciembre 2020 : Tontódromo PUCP")
#gif10#########################################################################
        col1, col2, col3= st.columns(3)
        with col2:        
            file_ = open("qairito_mala.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            
            st.markdown(
                f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
                unsafe_allow_html=True,
            )
###############################################################################
        cod_grafic_descargar("Monitoreo_Diciembre_2020_ovalo_miraflores.csv") 
############################################################################### 
###############################################################################     
if selected == 'Reporte 2021':
    #st.title(f"{selected}")
#MAPA MIRAFLORES###############################################################
    st.subheader("Puntos de muestreo")    
    st.write("**Se tomaron 2 puntos de muestreo, Av. Del Ejército y Av. José de la Riva Agüero**")
    latlon=pd.read_csv("lat_lon_2021.csv",sep=";")
    df = pd.DataFrame(latlon,columns=['lat', 'lon'])  
    st.map(df)
    st.write("**Leyenda**")
    st.write("""Av. Del Ejército (**AE**), 
             Av. José de la Riva Agüero (**AJ**)
             """)
#gif0##########################################################################
    st.subheader("Escala según ECA")    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.subheader("Buena")
        file_ = open("qairito_buena.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
            
        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
            unsafe_allow_html=True,
        )     
    with col2:
        st.subheader("Moderado")
        file_ = open("qairito_moderada.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
            
        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
            unsafe_allow_html=True,
        )     
    with col3:
        st.subheader("Mala")
        file_ = open("qairito_mala.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
            
        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
            unsafe_allow_html=True,
        )    
    with col4:
        st.subheader("Cuidado")
        file_ = open("qairito_cuidado.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
            
        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
            unsafe_allow_html=True,
        )
    st.write("**Fuente:** https://www.minam.gob.pe/wp-content/uploads/2016/07/RM-N°-181-2016-MINAM.pdf")
#BOTONES 2######################################################################
    lista2=('Enero AE','Enero AJ','Febrero AJ','Marzo AE')
    options = st.multiselect('¿Qué mes desea ver? (eliga solo un mes)', lista2)   
################################################################################
    if 'Enero AE' in options:
        st.header("Monitoreo de Enero 2021 : Av. del Ejército")
#gif11#########################################################################
        col1, col2, col3= st.columns(3)
        with col2:        
            file_ = open("qairito_moderada.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            
            st.markdown(
                f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
                unsafe_allow_html=True,
            )
###############################################################################
        cod_grafic_descargar("Monitoreo_Enero_2021_complejo_deportivo_manuel.csv")
################################################################################
    if 'Enero AJ' in options:        
        st.header("Monitoreo de Enero 2021 : Av. José de la Riva Agüero")
#gif12#########################################################################
        col1, col2, col3= st.columns(3)
        with col2:        
            file_ = open("qairito_mala.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            
            st.markdown(
                f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
                unsafe_allow_html=True,
            )
###############################################################################
        cod_grafic_descargar("Monitoreo_Enero_2021_ovalo_miraflores.csv")
################################################################################        
    if 'Febrero AJ' in options:
        st.header("Monitoreo de Febrero 2021 : Av. José de la Riva Agüero")
#gif13#########################################################################
        col1, col2, col3= st.columns(3)
        with col2:        
            file_ = open("qairito_buena.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            
            st.markdown(
                f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
                unsafe_allow_html=True,
            )
###############################################################################
        cod_grafic_descargar("Monitoreo_Febrero_2021_ovalo_miraflores.csv")
##############################################################################        
    if 'Marzo AE' in options:
        st.header("Monitoreo de Marzo 2021 : Av. Enrique Meiggs")
#gif14#########################################################################
        col1, col2, col3= st.columns(3)
        with col2:        
            file_ = open("qairito_mala.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            
            st.markdown(
                f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
                unsafe_allow_html=True,
            )
###############################################################################
        cod_grafic_descargar("Monitoreo_Marzo_2021_ovalo_miraflores.csv")
###############################################################################   
