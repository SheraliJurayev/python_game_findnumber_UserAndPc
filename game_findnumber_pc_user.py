# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 22:26:56 2023

@author: Sh_Jurayeff
"""

import random

def findnumber(x=10):
    tasodifiy_son=random.randint(1, x)
    print(f"Men 1 dan {x} gacha son o'yladim siz uni topa olasizmi?")
    
    taxminlar=0
    
    while True:
        taxminlar+=1
        taxmin=int(input(">>>>"))
        
        if taxmin<tasodifiy_son:
            print("Xato.Men uylagan son bundan kattaroq. Yana harakat qiling.")
        elif taxmin>tasodifiy_son:
            print("Xato.Men uylagan son bundan kichikroq. Yana harakat qiling.")
        else:
            break 
    print(f"Tabriklaymiz topdingiz {taxminlar}  ta taxmin bilan topdingiz.")        
    return taxminlar 

def findnumber_pc(x=10):
    
    input(f" 1 dan {x} gachs son o'ylang men uni topaman. Boshlash uchun istalgan tugmani bosing. ")
    
    quyi=1
    yuqori=x 
    taxminlar=0
    while True:
            taxminlar+=1
            if quyi!=yuqori:
                taxmin = random.randint(quyi, yuqori)
            else:
                taxmin=quyi
            javob=input(f"Siz {taxmin} sonini o'yladingiz: agar to'g'ri bo'lsa (t) ,"
                        f"men o'ylagan son bundan kattaroq (+) yoki kichikroq(-)".lower())
            if javob == "-":
                yuqori=taxmin-1
            elif javob == "+" :
                quyi=taxmin+1
            else:
                break
    
    print(f"Men {taxminlar} ta taxmin bilan topdim")  
    return taxminlar
    
def  play(x=10):
    yana=True
    while yana:
        taxminlar_user=findnumber(x)
        taxminlar_pc=findnumber_pc(x)
        
        if taxminlar_user>taxminlar_pc:
            print("Men yutdim!")
        elif taxminlar_pc>taxminlar_user:
            print("Siz yutdingiz!")
        else:
            print("Durrang!")
        
        yana = int(input("Yana o'ynaysizmi ha(0) , yo'q(1)"))             
              
play()
        
        
    


















































