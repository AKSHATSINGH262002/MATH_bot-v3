import streamlit as st
from PIL import Image
#from pytesseract import pytesseract 
import  matplotlib.pyplot as plt
import numpy as np
import pre
import pandas as pd
import company as cp
from pathlib import Path
import time
import mapping as mp


streaming=""" Hello Users Welcome to MATH_BOT  """
flag=0
img=Image.open('MATHION.png')
st.set_page_config(page_title="MATH-BOT",page_icon=img,layout="wide")

st.title(":grey[--MATHEMATICS-BOT--]")

#st.header("HOW CAN I HELP YOU FRIEND ?")
st.logo('MATHION.png')
def stream_data():
    for word in streaming.split(" "):
        yield word + " "
        time.sleep(0.30)
st.write(stream_data)
st.sidebar.title("Hiii ! select your option here")
st.header(":grey-background[Hello,let me work with you!]",divider="orange")
with st.spinner('Wait I am responding...'):
                time.sleep(4)
st.success('START YOUR WORK')


#if st.sidebar.button("Data_analysis"):

upload=st.sidebar.file_uploader(label="DATA ANALYSIS",type=["xlsx","csv","txt"])
if upload is not None:
        if upload.type=='csv':
                
                df=cp.csv_find(upload)
                st.dataframe(df)
            
        else:
            st.header("--HERE IS YOUR DATAFRAME--")
            df=cp.company_analyse(upload)
            st.dataframe(df)
                  
            clist=mp.graph_data(df)
            ct=st.sidebar.selectbox("select column",clist,index=None)
            if ct is not None:
                try:
                    col1,col2,col3,col4=st.columns(4)
                    l=cp.maths(df,ct)
                    with col1:
                        st.header("--Standard Deviation--")
                        st.info(l[0])
                    with col2:
                        st.header("--Mean--") 
                        st.info(l[1])
                    with col3:
                        st.header("--Median")
                        st.info(l[2])
                    with col4:
                        st.header("--mode--")
                        st.info(l[3])
                except:
                    st.info(":red[you selected the wrong coloumn please select the integer type coloumn]")
            else:
                streams="""See the options in sidebar for data analysis tasks"""
                def stream_data():
                    for word in streams.split(" "):
                        yield word + " "
                        time.sleep(0.30)
                st.write(stream_data)
                
                #st.info("for graphs see below option")
            # code for the bar,pie and linear graph
            st.sidebar.header("--FOR GRAPHS SELECT OPTION--")
            col_list=mp.graph_data(df)
            
            SELECTED1=st.sidebar.selectbox("COLUMNS LIST1",col_list,index=None)
            SELECTED2=st.sidebar.selectbox("COLUMN LIST2",col_list,index=None)
            fig,ax=plt.subplots()
            plt.figure(figsize=(10,6))
            
            l=mp.graphs_list()

            if st.sidebar.button(":green[piechart]"):
            
                  #ax.plot(df[SELECTED1],label=df[SELECTED2],autopct='%1.1f%%')
                  #st.pyplot(fig)
                  plt.figure(figsize=(6,6))
                  plt.pie(df[SELECTED1],labels=df[SELECTED2], autopct='%1.1f%%')
                  plt.axis('equal')
                  st.pyplot(plt)
                  

            if st.sidebar.button(":green[linear]"):
            
                  ax.plot(df[SELECTED1],df[SELECTED2],linewidth=3,marker="o")
                  
                  st.pyplot(fig)
            if st.sidebar.button(":green[bar]"):  
                    ax.bar(df[SELECTED1],df[SELECTED2],edgecolor="red",alpha=0.5)
                    st.pyplot(fig)
            
            if st.sidebar.button(":green[Scatter plot]"):
                plt.scatter(df[SELECTED1],df[SELECTED2],color="red")
                st.pyplot(plt)
            


#uploaded_file=st.sidebar.file_uploader(label="math_solver",type=["jpeg","png","jfif","jpg"])

#if uploaded_file is not None:
            
                




      


    
    
    








