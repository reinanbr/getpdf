#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Reinan Br. fev 2 03:22 2022
# getpdf project
# MIT LICENSE


from googlesearch import search
from requests import get
import os
import time
import sys


def search_pdf(param:str,n:int=20):
    """[summary]

    Args:
        param (str): [param for searching in the Google]
        n (int, optional): [number of results minimum]. Defaults to 20.
    """
    param = f'{param} filetype:pdf'
    results = []
    result_search = search(param,num_results=n)
    result_search = [link for link in result_search if 'http' in link]
    print('size search',len(result_search))
    for link in result_search:
        name_file = link.split('/')[-1] if '.pdf' in link.split('/')[-1] else  f"{link.split('/')[-1]}.pdf"
        
        #content = get(link).content
        #size_content = len(content)/(1024**2)
        result = {'name':name_file,'link':link}
        results.append(result)
    
    return results


def getpdf(param:str,n:int=20,dir:str='pdf'):
    """[getpdf]

    Args:
        param (str): [param for searching in the Google]
        n (int, optional): [number of results]. Defaults to 20.
        dir (str, optional): [direcotry for download]. Defaults to ''.
    """
    dir_base = dir
    result_search = search_pdf(param=param,n=n)
    
    param = '_'.join(param.split(' '))
    if not os.path.isdir(dir):
        os.system(f'mkdir {dir}')
    
    dir = f'{dir}/{param}'
    if not os.path.isdir(dir):
        os.system(f'mkdir {dir}')
    
    i=0
    init=time.perf_counter()
    
    list_toc = [0]
    size = len(result_search)
    for result in result_search:
        i+=1
        try:
            tic = time.perf_counter()
            content_pdf = get(result['link']).content
            size_content = len(content_pdf)/(1024**2)
            toc = time.perf_counter()-tic
            list_toc.append(toc)
            file_name = f'{dir}/{result["name"]}'
            with open(file_name,'wb') as file_pdf:
                file_pdf.write(content_pdf)
                
            end = time.perf_counter()-init
            #list_end.append(end)
            end_min = end//60
            end_sec = int(end%60)
            eta = (sum(list_toc)/len(list_toc))*(size-i)
            eta_min = eta//60
            eta_sec = int(eta%60)

            print('',f'[{i}/{size}] [{int(end_min)}min:{end_sec}sec | ETA: {int(eta_min)}min:{eta_sec}sec]','')

            print(file_name,f'{size_content:.2f} MB','saved!',f'[ping: {(toc*100):.1f} ms]','\n')
        except:
            end = time.perf_counter()-init
            #list_end.append(end)
            end_min = end//60
            end_sec = int(end%60)
            eta = (sum(list_toc)/len(list_toc))*(size-i)
            eta_min = eta//60
            eta_sec = int(eta%60)
            print('',f'[{i}/{size}] [{int(end_min)}m:{end_sec} s | ETA: {int(eta_min)}m:{eta_sec} s]','')
            print('error in link',result['link'],'error:',sys.exc_info()[0],'\n')
            
            pass
        