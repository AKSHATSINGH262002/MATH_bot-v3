import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def company_analyse(file):
    df=pd.read_excel(file)
    df=pd.DataFrame(df)
    df.dropna(how='all',axis=1,inplace=True)
    df.dropna(how='any',axis=0,inplace=True)
    #df=df.dropna()
    return df
def csv_find(file):
    df=pd.read_csv(file)
    df=pd.DataFrame(df)
    return df
def maths(df,ct):
    stand=df[ct].std()
    man=df[ct].mean()
    med=df[ct].median()
    md=df[ct].mode()
    li=[]
    li.append(stand)
    li.append(man)
    li.append(med)
    li.append(md)
    return li


