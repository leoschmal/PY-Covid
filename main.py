# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 18:23:02 2020

@author: leoschmal
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
import datetime as dt


url = 'https://docs.google.com/spreadsheets/d/16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA/export?format=csv&id=16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA&gid=0'
df = pd.read_csv(url)


urlGeo='covid19determinaciones.csv'
geo = pd.read_csv(urlGeo)
ER=geo['provincia']=='Entre Ríos'
testER=geo[ER]

cant=testER.groupby('tipo').sum()
print(cant)

print(geo.head())




def EntreRios():
    #-----------------------Entre Rios ----------------------------------------
    #Filtro los datos de Entre Ríos
    entrerios=df['osm_admin_level_4']=='Entre Ríos'
    dfEntreRios=df[entrerios]
    dfEntreRios['Acumulados']=dfEntreRios['nue_casosconf_diff'].cumsum()
    dfEntreRios['fecha']=pd.to_datetime(dfEntreRios['fecha'], dayfirst = True)
    dfEntreRios.set_index('fecha',inplace=True)
    
    #plt.style.use('ggplot')
    
    fig,ax=plt.subplots()
    ax1=ax.twinx()
    ax.bar(dfEntreRios.index, dfEntreRios['nue_casosconf_diff'])
    ax1.plot(dfEntreRios.index, dfEntreRios['Acumulados'], color='b')
    ax1.tick_params(axis='y', labelcolor='b')
    
    
    #set ticks every week
    ax.set_title('ENTRE RÍOS - Casos por Día & Acumulados', fontsize = 17)
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    #set major ticks format
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    ax.set_xlabel('Fecha')
    ax.set_ylabel('Casos Diarios', color='r')
    ax.tick_params(axis='y', labelcolor='r')
    ax.grid(False)
    
    ax1.set_ylabel('Casos Acumulados', color='b')
    ax1.set_yscale('log')
    #plt.yscale('log')
    
    plt.savefig('COVID-ER.jpg', dpi=150)
    #fig.tight_layout() 
    plt.show()


def SantaFe():
    #-----------------------Santa Fe ----------------------------------------
    #Filtro los datos de Santa Fe
    santafe=df['osm_admin_level_4']=='Santa Fe'
    dfSantaFe=df[santafe]
    dfSantaFe['Acumulados']=dfSantaFe['nue_casosconf_diff'].cumsum()
    dfSantaFe['fecha']=pd.to_datetime(dfSantaFe['fecha'], dayfirst = True)
    dfSantaFe.set_index('fecha',inplace=True)
    #plt.style.use('ggplot')
    
    fig,ax=plt.subplots()
    ax1=ax.twinx()
    ax.bar(dfSantaFe.index, dfSantaFe['nue_casosconf_diff'], color='r')
    ax1.plot(dfSantaFe.index, dfSantaFe['Acumulados'], color='b')
    ax1.tick_params(axis='y', labelcolor='b')
    
    
    #set ticks every week
    ax.set_title('SANTA FE - Casos por Día & Acumulados', fontsize = 17)
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    #set major ticks format
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    ax.set_xlabel('Fecha')
    ax.set_ylabel('Casos Diarios', color='r')
    ax.tick_params(axis='y', labelcolor='r')
    ax.grid(False)
    
    ax1.set_ylabel('Casos Acumulados', color='b')
    ax1.set_yscale('log')
    #plt.yscale('log')
    
    plt.savefig('COVID-SF.jpg', dpi=150)
    #fig.tight_layout() 
    plt.show()

def AcumStaFeEntreRios():
        #Filtro los datos de Entre Ríos
    entrerios=df['osm_admin_level_4']=='Entre Ríos'
    dfEntreRios=df[entrerios]
    dfEntreRios['Acumulados']=dfEntreRios['nue_casosconf_diff'].cumsum()
    dfEntreRios['fecha']=pd.to_datetime(dfEntreRios['fecha'], dayfirst = True)
    dfEntreRios.set_index('fecha',inplace=True)
    santafe=df['osm_admin_level_4']=='Santa Fe'
    dfSantaFe=df[santafe]
    dfSantaFe['Acumulados']=dfSantaFe['nue_casosconf_diff'].cumsum()
    dfSantaFe['fecha']=pd.to_datetime(dfSantaFe['fecha'], dayfirst = True)
    dfSantaFe.set_index('fecha',inplace=True)
    
    fig,ax=plt.subplots()
    #ax1=ax.twinx()
    ax.plot(dfEntreRios.index, dfEntreRios['Acumulados'], color='r', label='Entre Ríos')
    ax.plot(dfSantaFe.index, dfSantaFe['Acumulados'], color='b', label= 'Santa Fe')

    
    ax.set_title('SANTA FE & ENTRE RÍOS - Casos Acumulados', fontsize = 17)
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    #set major ticks format
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    ax.set_xlabel('Fecha')
    #ax.tick_params(axis='y')
    ax.grid(True)
    ax.legend(loc='upper left', shadow=True, fontsize='large', frameon='True', fancybox='True', facecolor='grey')
    ax.set_ylabel('Casos Acumulados (log)')
    ax.set_yscale('log')

    plt.savefig('COVID-SF&ER.jpg', dpi=150)
    #fig.tight_layout() 
    plt.show()
    
def CasosParana():
    parana=testER[testER['localidad']=='PARANA']
    parana['Acumulados']=parana['positivos'].cumsum()
    parana['fecha']=pd.to_datetime(parana['fecha'], dayfirst = True)
    parana.set_index('fecha',inplace=True)
    print(parana.head())
    
    
    fig,ax=plt.subplots()
    #ax1=ax.twinx()
    ax.plot(parana.index, parana['Acumulados'], color='r', label='Positivos')
    ax.tick_params(axis='y', labelcolor='b')

    #set ticks every week
    ax.set_title('PARANÁ - Casos Positivos', fontsize = 17)
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    #set major ticks format
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    ax.set_xlabel('Fecha')
    
    ax.tick_params(axis='y', labelcolor='r')
    ax.grid(True)
    ax.legend(loc='upper left', shadow=True, fontsize='large', frameon='True', fancybox='True', facecolor='grey')
    ax.set_ylabel('Casos Positivos Acumulados')

    
    plt.savefig('Parana-ER.jpg', dpi=150)
    #fig.tight_layout() 
    plt.show()
    
def Test_ContER():
        #-----------------------Entre Rios TEST----------------------------------------
    #Filtro los datos de Entre Ríos
    entrerios=df['osm_admin_level_4']=='Entre Ríos'
    dfEntreRios=df[entrerios]
    dfEntreRios['Acumulados']=dfEntreRios['nue_casosconf_diff'].cumsum()
    dfEntreRios['fecha']=pd.to_datetime(dfEntreRios['fecha'], dayfirst = True)
    dfEntreRios.set_index('fecha',inplace=True)
    
    testER['Acumulados']=testER['total'].cumsum()
    testER['fecha']=pd.to_datetime(testER['fecha'], dayfirst = True)
    testER.set_index('fecha',inplace=True)
    #plt.style.use('ggplot')
    
    fig,ax=plt.subplots()
    #ax1=ax.twinx()
    ax.plot(testER.index, testER['Acumulados'], color='r', label='Test')
    ax.plot(dfEntreRios.index, dfEntreRios['Acumulados'], color='b', label='Casos Positivos')
    ax.tick_params(axis='y', labelcolor='b')
    
    
    #set ticks every week
    ax.set_title('ENTRE RÍOS - Casos Positivos & Test Realizados', fontsize = 17)
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    #set major ticks format
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    ax.set_xlabel('Fecha')
    
    ax.tick_params(axis='y', labelcolor='r')
    ax.grid(True)
    ax.legend(loc='upper left', shadow=True, fontsize='large', frameon='True', fancybox='True', facecolor='grey')
    ax.set_ylabel('Casos Acumulados')

    
    plt.savefig('Pos&Test-ER.jpg', dpi=150)
    #fig.tight_layout() 
    plt.show()
    pass
    

print('Generar Graficas de estado de casos de Covid-19')
print('''Seleccione Región: 
      1-Entre Ríos - Casos Diarios y Acumulados
      2- Santa Fe - Casos Diarios y Acumulados
      3- Rosario''')
selector=str
selector= int(input('ingrese opcion:'))
if selector==1:
    EntreRios()
if selector ==2:
    SantaFe()
if selector == 3:
    AcumStaFeEntreRios()
if selector ==4:
    Test_ContER()
if selector == 5:
    CasosParana()