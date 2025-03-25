import streamlit as st
from PIL import Image
from pytesseract import pytesseract 
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
            


uploaded_file=st.sidebar.file_uploader(label="math_solver",type=["jpeg","png","jfif","jpg"])

if uploaded_file is not None:
            
                col1,col2=st.columns(2)
                with col1:
                    image=Image.open(uploaded_file)
                    st.image(image)
                    text=pre.extract(image)
        #arr=text.split()
                    extracted_text=pre.extract(image)
                    d={'extracted_text':extracted_text}
                    df=pd.DataFrame(d)
                    st.dataframe(df)

        
                    if len(extracted_text)==0:
                        st.write("sorry nothing is extracted from image please provide other image \n OR")
            # Display the extracted text
                    ne=st.text_input('ENTER THE FUNCTION YOU WANT')
                    extracted_text.append(ne)
                    st.write("Extracted Text:")
                    st.text(extracted_text) 
            
        #print(arr)
                if st.sidebar.button("EXPLORE"):
                    
                        for i in extracted_text:
    
                            x=np.linspace(0,2*np.pi,100)
                            n=np.linspace(-2 * np.pi, 2 * np.pi, 1000)
                            s=np.linspace(0.1, 10, 1000)
                            t=np.linspace(-2, 2, 1000)
                            if(i=="sin" or i=="Sin"or i=="sin(x)" or i=="sine" or i=="sin x" or i=="SIN"):

                                y_sin=np.sin(x)
                                fig,ax=plt.subplots()
                                ax.plot(x,y_sin,label='sin x',color='red',linewidth=2)
                                plt.xlabel('x')
                                plt.title('sin x graph')
                                st.pyplot(fig)
                    #break
               

                            elif(i=="cos"or i=="Cos" or i=="cos(x)" or i=="cosine"or i=="cosx" or i=="COS"):

                                y_cos=np.cos(x)
                                fig,ax=plt.subplots()
                                ax.plot(x,y_cos,label='cos x',color='red',linewidth=2)
                                plt.xlabel('x')
                                plt.title('cos x graph')
                                st.pyplot(fig)
                    #break
                

    
                            elif(i=="tan"or i=="Tan" or i=="tan(x)" or i=="tangent"or i=="tanx" or i=="TAN"):
                
                                y_tan=np.tan(n)
                                fig,ax=plt.subplots()
                                ax.plot(n,y_tan,label='tan(x)',color='blue')
                                plt.xlabel('x')
                                plt.ylabel('tan(x)')
                                plt.title('tan(x) graph')
                                plt.ylim(-10,10)
                                ax.grid(True)
                                ax.legend()
                                st.pyplot(fig)
                    #break
    
                            elif(i=="cosec"or i=="Cosec" or i=="cosec(x)" or i=="COSEC"):

                                y_cosec=1/np.sin(n)
                                fig,ax=plt.subplots()
                                ax.plot(n,y_cosec,label='cosec(x)',color='green',linewidth=2)
                                plt.xlabel('x')
                                plt.ylabel('cosex(x)')
                                plt.title('cosec(x) graph')
                                plt.ylim(-10,10)
                                st.pyplot(fig)
                    #break

            
                            elif(i=="sec"or i=="Sec" or i=="sec(x)"or i=="SEC"):

                                y_sec=1/np.cos(n)
                                fig,ax=plt.subplots()
                                ax.plot(n,y_sec,label='sec(x)',color='green',linewidth=2)
                                st.pyplot(fig)
                    #break
            
                            elif(i=="log" or i=="LOG"):
                

                                y=np.log(s)
                                fig,ax=plt.subplots()
                                ax.plot(s,y,label='log(x)',color='orange')
                                st.pyplot(fig)

                    #break
                            elif(i=="e^x"):
                                y_exp=np.exp(t)
                                fig,ax=plt.subplots()
                                ax.plot(t,y_exp,label='exponential',color='orange')
                                ax.title('exponential')
                                ax.xlabel('x')
                                ax.ylabel('exponential')
                                st.pyplot(fig)
                    
                            else:
                                flag=1
                if(flag==1):
                        print("no more function found")




      


    
    
    








