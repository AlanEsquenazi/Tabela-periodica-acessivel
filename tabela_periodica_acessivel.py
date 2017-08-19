import pygame.mixer
import sys
import os
from pygame.mixer import *
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.quit()
pygame.mixer.init()
fpsTime = pygame.time.Clock()
fpsTime.tick(60)
try:
    pygame.mixer.music.load('welcome.ogg')
    pygame.mixer.music.play(0)
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
        #print('playing')
except Exception:
    pygame.mixer.music.load('welcome.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy(): 
        pygame.time.Clock().tick(10)
tabela_ogg = [[],['1.ogg', 'h.ogg', 'li.ogg', 'na.ogg', 'k.ogg', 'rb.ogg', 'cs.ogg', 'fr.ogg'],
['2.ogg','be.ogg', 'mg.ogg', 'ca.ogg', 'sr.ogg', 'ba.ogg', 'ra.ogg'],['3.ogg','sc.ogg', 'y.ogg',
['3,1.ogg','la.ogg', 'ce.ogg', 'pr.ogg', 'nd.ogg', 'pm.ogg', 'sm.ogg', 'eu.ogg', 'gd.ogg', 'tb.ogg', 'dy.ogg', 'ho.ogg', 'er.ogg', 'tm.ogg', 'yb.ogg', 'lu.ogg'],
['3,2.ogg','ac.ogg', 'th.ogg', 'pa.ogg', 'u.ogg', 'np.ogg', 'pu.ogg', 'am.ogg', 'cm.ogg', 'bk.ogg', 'cf.ogg', 'es.ogg', 'fm.ogg', 'md.ogg', 'no.ogg', 'lr.ogg']],
['4.ogg','ti.ogg', 'zr.ogg', 'hf.ogg', 'rf.ogg'],['5.ogg','v.ogg', 'nb.ogg', 'ta.ogg', 'db.ogg'],['6.ogg','cr.ogg', 'mo.ogg', 'w.ogg', 'sg.ogg'],
['7.ogg','mn.ogg', 'tc.ogg', 're.ogg', 'bh.ogg'],['8.ogg','fe.ogg', 'ru.ogg', 'os.ogg', 'hs.ogg'],['9.ogg','co.ogg', 'rh.ogg', 'ir.ogg', 'mt.ogg'],
['10.ogg','ni.ogg', 'pd.ogg', 'pt.ogg', 'ds.ogg'],['11.ogg','cu.ogg', 'ag.ogg', 'au.ogg', 'rg.ogg'],['12.ogg', 'zn.ogg', 'cd.ogg', 'hg.ogg', 'cn.ogg'],
['13.ogg','b.ogg', 'al.ogg', 'ga.ogg', 'in.ogg', 'tl.ogg', 'nh.ogg'],['14.ogg','c.ogg', 'si.ogg', 'ge.ogg', 'sn.ogg', 'sn.ogg', 'pb.ogg', 'fl.ogg'],
['15.ogg', 'n.ogg', 'p.ogg', 'as.ogg', 'sb.ogg', 'bi.ogg', 'mc.ogg'],['16.ogg','o.ogg', 's.ogg', 'se.ogg', 'te.ogg', 'po.ogg', 'lv.ogg'],
['17.ogg','f.ogg', 'cl.ogg', 'br.ogg', 'i.ogg', 'at.ogg', 'ts.ogg'],['18.ogg','he.ogg', 'ne.ogg', 'ar.ogg', 'kr.ogg', 'xe.ogg', 'rn.ogg', 'og.ogg']]
tabela_mp3 = [[],['1.mp3', 'h.mp3', 'li.mp3', 'na.mp3', 'k.mp3', 'rb.mp3', 'cs.mp3', 'fr.mp3'],
['2.mp3','be.mp3', 'mg.mp3', 'ca.mp3', 'sr.mp3', 'ba.mp3', 'ra.mp3'],['3.mp3','sc.mp3', 'y.mp3',
['3,1mp3','la.mp3', 'ce.mp3', 'pr.mp3', 'nd.mp3', 'pm.mp3', 'sm.mp3', 'eu.mp3', 'gd.mp3', 'tb.mp3', 'dy.mp3', 'ho.mp3', 'er.mp3', 'tm.mp3', 'yb.mp3', 'lu.mp3'],
['3,2.mp3','ac.mp3', 'th.mp3', 'pa.mp3', 'u.mp3', 'np.mp3', 'pu.mp3', 'am.mp3', 'cm.mp3', 'bk.mp3', 'cf.mp3', 'es.mp3', 'fm.mp3', 'md.mp3', 'no.mp3', 'lr.mp3']],
['4.mp3','ti.mp3', 'zr.mp3', 'hf.mp3', 'rf.mp3'],['5.mp3','v.mp3', 'nb.mp3', 'ta.mp3', 'db.mp3'],['6.mp3','cr.mp3', 'mo.mp3', 'w.mp3', 'sg.mp3'],
['7.mp3','mn.mp3', 'tc.mp3', 're.mp3', 'bh.mp3'],['8.mp3','fe.mp3', 'ru.mp3', 'os.mp3', 'hs.mp3'],['9.mp3','co.mp3', 'rh.mp3', 'ir.mp3', 'mt.mp3'],
['10.mp3','ni.mp3', 'pd.mp3', 'pt.mp3', 'ds.mp3'],['11.mp3','cu.mp3', 'ag.mp3', 'au.mp3', 'rg.mp3'],['12.mp3', 'zn.mp3', 'cd.mp3', 'hg.mp3', 'cn.mp3'],
['13.mp3','b.mp3', 'al.mp3', 'ga.mp3', 'in.mp3', 'tl.mp3', 'nh.mp3'],['14.mp3','c.mp3', 'si.mp3', 'ge.mp3', 'sn.mp3', 'sn.mp3', 'pb.mp3', 'fl.mp3'],
['15.mp3', 'n.mp3', 'p.mp3', 'as.mp3', 'sb.mp3', 'bi.mp3', 'mc.mp3'],['16.mp3','o.mp3', 's.mp3', 'se.mp3', 'te.mp3', 'po.mp3', 'lv.mp3'],
['17.mp3','f.mp3', 'cl.mp3', 'br.mp3', 'i.mp3', 'at.mp3', 'ts.mp3'],['18.mp3','he.mp3', 'ne.mp3', 'ar.mp3', 'kr.mp3', 'xe.mp3', 'rn.mp3', 'og.mp3']]
def audio(x, y):
    try:
        pygame.mixer.music.load(tabela_ogg[x][y])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy(): 
            pygame.time.Clock().tick(10)
    except Exception:
        try:
            pygame.mixer.music.load(tabela_mp3[x][y])
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy(): 
                pygame.time.Clock().tick(10)
        except Exception:
            try:
                pygame.mixer.music.load('error.ogg')
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy(): 
                    pygame.time.Clock().tick(10)
            except Exception:
                pygame.mixer.music.load('error.mp3')
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy(): 
                    pygame.time.Clock().tick(10)
def audio_s(x, y):
    try:
        pygame.mixer.music.load(tabela_ogg[x][y][0])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy(): 
            pygame.time.Clock().tick(10)
    except Exception:
        try:
            pygame.mixer.music.load(tabela_mp3[x][y][0])
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy(): 
                pygame.time.Clock().tick(10)
        except Exception:
            try:
                pygame.mixer.music.load('error.ogg')
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy(): 
                    pygame.time.Clock().tick(10)
            except Exception:
                pygame.mixer.music.load('error.mp3')
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy(): 
                    pygame.time.Clock().tick(10)
    tres = int(input())
    try:
        pygame.mixer.music.load(tabela_ogg[x][y][tres])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy(): 
            pygame.time.Clock().tick(10)
    except Exception:
        try:
            pygame.mixer.music.load(tabela_mp3[x][y][tres])
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy(): 
                pygame.time.Clock().tick(10)
        except Exception:
            try:
                pygame.mixer.music.load('error.ogg')
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy(): 
                    pygame.time.Clock().tick(10)
            except Exception:
                pygame.mixer.music.load('error.mp3')
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy(): 
                    pygame.time.Clock().tick(10)
while(1):
    fpsTime.tick(60)
    var = 0
    w = 'w'
    y = 'y'
    n = 'n'
    inicio = str(input())
    try:
        inicio = int(inicio)
        var = 1
    except Exception:
        var = 0
    if var==0:
        fator = 7
        try:
            inicio_ = inicio+'.ogg'
            pygame.mixer.music.load(inicio_)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy(): 
                pygame.time.Clock().tick(10)
        except Exception:
            try:
                inicio_ = inicio + '.mp3'
                pygame.mixer.music.load(inicio_)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy(): 
                    pygame.time.Clock().tick(10)
            except Exception:
                try:
                    pygame.mixer.music.load('error.ogg')
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy(): 
                        pygame.time.Clock().tick(10)
                except Exception:
                    pygame.mixer.music.load('error.mp3')
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy(): 
                        pygame.time.Clock().tick(10)
    if var==1:
        fator = 0
        audio(inicio, 0)
        vertical = input()
        vertical = int(vertical)
        if inicio==3 and (vertical==4 or vertical==5):
            audio_s(inicio, vertical)
        else:
            audio(inicio, vertical)
        if fator != 7:
            try:
                pygame.mixer.music.load('next_iteration.ogg')
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy(): 
                    pygame.time.Clock().tick(10)
            except Exception:
                pygame.mixer.music.load('next_iteration.mp3')
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy(): 
                    pygame.time.Clock().tick(10)
            nit = str(input())
            if nit=='y':
                pass
            elif nit=='n':
                pygame.quit()
                sys.exit()
            else:
                try:
                    pygame.mixer.music.load('error.ogg')
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy(): 
                        pygame.time.Clock().tick(10)
                except Exception:
                    pygame.mixer.music.load('error.mp3')
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy(): 
                        pygame.time.Clock().tick(10)




