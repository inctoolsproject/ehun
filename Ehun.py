
import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess

satpam = LINETCR.LINE() # Login Pake Akun Kicker Kalian
#satpam.login(token="token anda")#ganti dgn token kalian
satpam.login(token="EpWYYMjmEWUba52UlKA1.8nezDhK7HGW9hVtLK4qvGq.4AyYmATuAvCztvMdCZ5xnyhRST1FUx3coUoPztOJtEw=")
satpam.loginResult()

cl = LINETCR.LINE() #Luffy
#cl.login(token="token anda")#ganti dgn token kalian
cl.login(token="EpWYYMjmEWUba52UlKA1.8nezDhK7HGW9hVtLK4qvGq.4AyYmATuAvCztvMdCZ5xnyhRST1FUx3coUoPztOJtEw=")
cl.loginResult()

ki = LINETCR.LINE() #Zorro
#ki.login(token="token anda")#ganti dgn token kalian
ki.login(token="EpWYYMjmEWUba52UlKA1.8nezDhK7HGW9hVtLK4qvGq.4AyYmATuAvCztvMdCZ5xnyhRST1FUx3coUoPztOJtEw=")
ki.loginResult()

kk = LINETCR.LINE() #Sanji
#kk.login(token="token anda")#ganti dgn token kalian
kk.login(token="EpWYYMjmEWUba52UlKA1.8nezDhK7HGW9hVtLK4qvGq.4AyYmATuAvCztvMdCZ5xnyhRST1FUx3coUoPztOJtEw=")
kk.loginResult()

kc = LINETCR.LINE() #Ussop
#kc.login(token="token anda")#ganti dgn token kalian
kc.login(token="

print "login success Boss"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""" ^[One Piece Bot]^
OWNER •Eehun•
http://line.me/ti/p/~sarehun

Command bot for owner :
======================
> Set/Status
> Help
> Admin menu
> Gn (ganti nama grup)
> kick mid (kick + mid target)
> Invite mid (Invite + mid target)
> Admin add @ (tambah admin + tag kontak)
> Admin remove @ (hapus admin + tag kontak)
> Adminlist/adminlist (list admin)
> Allbio: ... (bikin status di bio bot)
> Myname:...
> Cancel (membatalkan undangan)
> Buka qr 
> Tutup qr
> Info Group (info grup tsb)
> Message change: ... 
> /invitemeto: ... (/invitemeto: id group)
> Kuy/One piece/Join OP (Bot masuk group)owner/creator
> Kuya/Koplak OP (bot masuk group)bot
> Koplak join (bot masuk room)
> Bye op/Kabur all/Kaboor all/One piece left (klr dari room)
> Kabur OP(klr Room)
> Bot like (semua bot ngelike status akun utama)
> Like temen (semua bot ngelike status temen)
> Kill ..(kick banned)
> Ready op (ratakan)
> Nk .. (kick tag member)
> LG (list group)
> Bot out/Op bye (klr dari semua group)


> Add on/off
> Comment on/off
> Jam on
> Change clock
> Jam Update

[ command di atas hanya utk owner bot => Ehun


Command bot for admin :
=======================
> Admin menu
> Help
> Keyword
> Spam: ...
> Bot? (cek kontak bot)
> Me
> My mid (cek mid kita sendiri)
> Mid Bot (cek mid bot)
> Cctv (ngeset Reader)
> Ciduk (ngecek yg ngintip) 
> Tag all/Tagall (tag semua member)
> Blacklist @ 
> Banned @
> Mid @
> Unban @
> Up/up/Up Chat/Up chat/up chat/Upchat/upchat (naik chat spam)
> GBc ... (ngeBC ke semua group yg ada bot trsbt)
> Absen/Absen bot/Absen dulu/Respon
> Speed/Sp
> Ban
> Unban
> Creator
> Banlist
> Cek ban
> Kill ban
> Clear

******************"""

keyword =""" ^[One Piece Bot]^
bot chat :
==========
> Wkwkwk/Wkwk/Wk
> Hehehe/Hehe/He
> Galau
> Galau
> You
> Hadeuh
> Please
> Haaa
> Lol
> Hmmm/Hmm/Hm
> Welcome
> #welcome
> Woy/woy/Woi/bot/Bot

keywordiseng :
===============
> Apakah [sebutkan kata yg anda mau]
> Berapa besar cinta [sebutkan kata yg anda mau]
> Adakah [sebutkan kata yg anda mau]
> Cakepkah [sebutkan kata yg anda mau]
> Siapakah cewek [sebutkan kata yg anda mau]
> Siapakah cowok [sebutkan kata yg anda mau]
******************#"""

Setgroup =""" 
    [Admin Menu]
==============
||[Protect QR]
||- Qr on/off
||[Protect Join]
||- Join on/off
||[Mid Via Contact]
||- Contact on/off
||-[Cancel Invited]
||- Cancel all
==============
   ONE PIECE BOT
==============#"""
KAC=[cl,ki,kk,kc,ks,ka,kb,ko,ke,ku]
mid = cl.getProfile().mid #Luffy
Amid = ki.getProfile().mid #Zorro
Bmid = kk.getProfile().mid #Sanji
Cmid = kc.getProfile().mid #Ussop
Dmid = ks.getProfile().mid #Chooper
Emid = ka.getProfile().mid #Franky
Fmid = kb.getProfile().mid #Brook
Gmid = ko.getProfile().mid #Nami
Hmid = ke.getProfile().mid #Robin
Imid = ku.getProfile().mid #Rebecca
Smid = satpam.getProfile().mid #Akun Utama
mid1 = k1.getProfile().mid #Backup

Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Smid,mid1]
admin=["ub3808de9f7df35f57fb366d157f9790a"]
owner=["ub3808de9f7df35f57fb366d157f9790a"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"""тerima Kasih Sudah Menambahkan Aku Jadi Teman
≫ Aku Ga Jawab PM Karna aq Cuma Bot Protect ≪
≫ ONE PIECE BOT PROTECT ≪

Ready:

≫ bot protect ≪
≫ SelfBot ≪


ṡȗƿƿȏяṭєԀ ɞʏ:
  
☆ FS3I FAMILY ☆
☆ ONE PIECE BOT PROTECT ☆
☆ SMULE VOICE FAMILY ☆
☆ FOUNDER COMMUNITY ☆
☆ ASOSIATION FOUNDER INDONESIA ☆
☆ Generasi Kickers Killers ☆


Minat? Silahkan PM!
Idline: http://line.me/ti/p/~alrahmantoganteng""",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"™1™ ",
    "cName2":"™2™ ",
    "cName3":"™3™ ",
    "cName4":"™4™ ",
    "cName5":"™5™ ",
    "cName6":"™Franky™ ",
    "cName7":"™Brook™ ",
    "cName8":"™Nami™ ",
    "cName9":"™Robin™ ",
    "cName10":"™Rebecca™ ",
    "cName11":"",
    "cName12":"™ONE PIECE BOT™ ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Protectgr":True,
    #"Protectjoin":True, # Ga Kepake(Yang Gabung langsung di kick :D) Udah  Udah ada Protect Cancell
    "Protectcancl":True,
    "protectionOn":True,
    "atjointicket":True
    }

         wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        #------Protect Group Kick start------#
        if op.type == 11:
          if wait["Protectgr"] == True:
            if op.param2 not in Bots:
              G = random.choice(KAC).getGroup(op.param1)
              G.preventJoinByTicket = True
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              random.choice(KAC).updateGroup(G)
              random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "Jangan Buka Kode QR Woooyyy")
        #------Protect Group Kick finish-----#

        #------Cancel Invite User start------#
        if op.type == 13:
          if wait["Protectcancl"] == True:
            if op.param2 not in Bots:
              group = cl.getGroup(op.param1)
              gMembMids = [contact.mid for contact in group.invitee]
              random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)
        #------Cancel Invite User Finish------#
            
        if op.type == 13: 
            if op.param3 in mid:
                if op.param2 in Amid:
                    G = Amid.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)

            if op.param3 in Amid:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)

            if op.param3 in Bmid:
                if op.param2 in Amid:
                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)

            if op.param3 in Cmid:
                if op.param2 in Bmid:
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                
            if op.param3 in Dmid:
                if op.param2 in Cmid:
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ks.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)
                
            if op.param3 in Emid:
                if op.param2 in Dmid:
                    X = ks.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ks.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ka.updateGroup(X)
                    Ti = ka.reissueGroupTicket(op.param1)
                
            if op.param3 in Fmid:
                if op.param2 in Emid:       
                    X = ka.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ka.updateGroup(X)
                    Ti = ka.reissueGroupTicket(op.param1)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kb.updateGroup(X)
                    Ti = kb.reissueGroupTicket(op.param1)
                
            if op.param3 in Gmid:
                if op.param2 in Fmid:
                    X = kb.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kb.updateGroup(X)
                    Ti = kb.reissueGroupTicket(op.param1)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ko.updateGroup(X)
                    Ti = ko.reissueGroupTicket(op.param1)
                
            if op.param3 in Hmid:
                if op.param2 in Gmid:
                    X = ko.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ko.updateGroup(X)
                    Ti = ko.reissueGroupTicket(op.param1)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ke.updateGroup(X)
                    Ti = ke.reissueGroupTicket(op.param1)
                    
            if op.param3 in Imid:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)        

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
                    
        if op.type == 19: #Member Ke Kick
          if op.param2 not in Bots:
            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
              
        if op.type == 19:
           if op.param2 in induk: 
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              random.choice(xbots).inviteIntoGroup(op.param1,[op.param3])
              
        if op.type == 19:
           if op.param2 in Bots:
              G = cl.getGroup(msg.to)
              ginfo = cl.getGroup(msg.to)
              G.preventJoinByTicket = False
              cl.updateGroup(G)
              invsend = 0
              Ticket = cl.reissueGroupTicket(msg.to)
              ki.acceptGroupInvitationByTicket(msg.to,Ticket)
              time.sleep(0.01)
              kk.acceptGroupInvitationByTicket(msg.to,Ticket)
              time.sleep(0.01)
              kc.acceptGroupInvitationByTicket(msg.to,Ticket)
              time.sleep(0.01)
              ks.acceptGroupInvitationByTicket(msg.to,Ticket)
              time.sleep(0.01)
              ka.acceptGroupInvitationByTicket(msg.to,Ticket)
              time.sleep(0.01)
              kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                 if op.type == 19: #Member Ke Kick
          if op.param2 not in Bots:
            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
              
        if op.type == 19:
           if op.param2 in induk: 
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              random.choice(xbots).inviteIntoGroup(op.param1,[op.param3])
              
        if op.type == 19:
           if op.param2 in Bots:
              G = cl.getGroup(msg.to)
              ginfo = cl.getGroup(msg.to)
              G.preventJoinByTicket = False
              cl.updateGroup(G)
              invsend = 0
              Ticket = cl.reissueGroupTicket(msg.to)
              ki.acceptGroupInvitationByTicket(msg.to,Ticket)
              time.sleep(0.01)
              kk.acceptGroupInvitationByTicket(msg.to,Ticket)
              time.sleep(0.01)
              kc.acceptGroupInvitationByTicket(msg.to,Ticket)
              time.sleep(0.01)
              ks.acceptGroupInvitationByTicket(msg.to,Ticket)
              time.sleep(0.01)
     time.sleep(0.01)
              ko.acceptGroupInvitationByTicket(msg.to,Ticket)
              time.sleep(0.01)
              ke.acceptGroupInvitationByTicket(msg.to,Ticket)
              time.sleep(0.01)
              ku.acceptGroupInvitationByTicket(msg.to,Ticket)
              time.sleep(0.01)
              k1.acceptGroupInvitationByTicket(msg.to,Ticket)
              time.sleep(0.01)                        
              G = cl.getGroup(msg.to)
              ginfo = cl.getGroup(msg.to)
              G.preventJoinByTicket = True
              cl.updateGroup(G)
              G.preventJoinByTicket(G)
              random.choice(KAC).updateGroup(G)
              
        if op.type == 19: 
          if op.param3 in admin: #Kalo Admin ke Kick
            if op.param2 in Bots:
              pass
            if op.param2 in owner:
              pass
            else:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                cl.inviteIntoGroup(op.param1,[op.param3])
              
        if op.type == 19:
          try:
            if op.param3 in Smid: #Akun Utama Ke Kick
              G = random.choice(KAC).getGroup(op.param1)
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              G.preventJoinByTicket = False
              random.choice(KAC).updateGroup(G)
              Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
              satpam.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              G.preventJoinByTicket = True
              random.choice(KAC).updateGroup(G)
              satpam.updateGroup(G)
              wait["blacklist"][op.param2] = True

            if op.param3 in Smid:
              if op.param2 in mid:
                G = cl.getGroup(op.param1)
                G.preventJoinByTicket = False
                cl.updateGroup(G)
                Ticket = cl.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                cl.updateGroup(G)
              else:
                G = cl.getGroup(op.param1)
                cl.kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                cl.updateGroup(G)
                Ticket = cl.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                satpam.updateGroup(G)
                cl.updateGroup(G)
                wait["blacklist"][op.param2] = True
                                  
            if op.param3 in mid:
              if op.param2 in Amid:
                G = ki.getGroup(op.param1)
                G.preventJoinByTicket = False
                ki.updateGroup(G)
                Ticket = ki.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                ki.updateGroup(G)
              else:
                G = ki.getGroup(op.param1)
                ki.kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                ki.updateGroup(G)
                Ticket = ki.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                cl.updateGroup(G)
                ki.updateGroup(G)
                wait["blacklist"][op.param2] = True
                
            if op.param3 in Amid:
              if op.param2 in Bmid:
                G = kk.getGroup(op.param1)
                G.preventJoinByTicket = False
                kk.updateGroup(G)
                Ticket = kk.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                kk.updateGroup(G)
              else:
                G = kk.getGroup(op.param1)
                kk.kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                kk.updateGroup(G)
                Ticket = kk.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                #cl.updateGroup(G)
                kk.updateGroup(G)
                #wait["blacklist"][op.param2] = True
                
            if op.param3 in Bmid:
              if op.param2 in Cmid:
                G = kc.getGroup(op.param1)
                G.preventJoinByTicket = False
                kc.updateGroup(G)
                Ticket = kc.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                kc.updateGroup(G)
              else:
                G = kc.getGroup(op.param1)
                kc.kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                kc.updateGroup(G)
                Ticket = kc.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                #cl.updateGroup(G)
                kc.updateGroup(G)
                #wait["blacklist"][op.param2] = True
                
            if op.param3 in Cmid:
              if op.param2 in Dmid:
                G = ks.getGroup(op.param1)
                G.preventJoinByTicket = False
                ks.updateGroup(G)
                Ticket = ks.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                ks.updateGroup(G)
              else:
                G = ks.getGroup(op.param1)
                ks.kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                ks.updateGroup(G)
                Ticket = ks.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                #cl.updateGroup(G)
                ks.updateGroup(G)
                #wait["blacklist"][op.param2] = True
                
            if op.param3 in Dmid:
              if op.param2 in Emid:
                G = ka.getGroup(op.param1)
                G.preventJoinByTicket = False
                ka.updateGroup(G)
                Ticket = ka.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                ka.updateGroup(G)
              else:
                G = ka.getGroup(op.param1)
                ka.kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                ka.updateGroup(G)
                Ticket = ka.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                #cl.updateGroup(G)
                ka.updateGroup(G)
                #wait["blacklist"][op.param2] = True
                
            if op.param3 in Emid:
              if op.param2 in Fmid:
                G = kb.getGroup(op.param1)
                G.preventJoinByTicket = False
                kb.updateGroup(G)
                Ticket = kb.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                kb.updateGroup(G)
              else:
                G = kb.getGroup(op.param1)
                kb.kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                kb.updateGroup(G)
                Ticket = kb.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                #cl.updateGroup(G)
                kb.updateGroup(G)
                #wait["blacklist"][op.param2] = True
                
            if op.param3 in Gmid:
              if op.param2 in Hmid:
                G = ku.getGroup(op.param1)
                G.preventJoinByTicket = False
                ku.updateGroup(G)
                Ticket = ku.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                ku.updateGroup(G)
              else:
                G = ku.getGroup(op.param1)
                ku.kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                ku.updateGroup(G)
                Ticket = ku.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                #cl.updateGroup(G)
                ku.updateGroup(G)
                #wait["blacklist"][op.param2] = True
                
            if op.param3 in Hmid:
              if op.param2 in Imid:
                G = ko.getGroup(op.param1)
                G.preventJoinByTicket = False
                ko.updateGroup(G)
                Ticket = ko.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                ko.updateGroup(G)
              else:
                G = ko.getGroup(op.param1)
                ko.kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                ko.updateGroup(G)
                Ticket = ko.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                #cl.updateGroup(G)
                ko.updateGroup(G)
                #wait["blacklist"][op.param2] = True
                
            if op.param3 in Imid:
              if op.param2 in mid:
                G = cl.getGroup(op.param1)
                G.preventJoinByTicket = False
                cl.updateGroup(G)
                Ticket = cl.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                cl.updateGroup(G)
              else:
                G = cl.getGroup(op.param1)
                cl.kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                ka.updateGroup(G)
                Ticket = cl.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                cl.updateGroup(G)
                #ke.updateGroup(G)
                #wait["blacklist"][op.param2] = True
          except:
            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
            cl.inviteIntoGroup(op.param1,[op.param3])
#--------------------------------
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
                              
        if op.type == 22:
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message


            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        kk.sendText(msg.to,"already")
                        kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        ki.sendText(msg.to,"aded")
                        kk.sendText(msg.to,"aded")
                        kc.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Keyword"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,keyword)
                else:
                    cl.sendText(msg.to,helpt)                                        
            elif msg.text in ["Admin menu"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,Setgroup)
                else:
                    cl.sendText(msg.to,Sett)
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("Luffy gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv1 gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("Zorro gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv2 gn ","")
                    kk.updateGroup(X)
                else:
                    kk.sendText(msg.to,"It can't be used besides the group.")
            elif ("Sanji gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv3 gn ","")
                    kc.updateGroup(X)
                else:
                    kc.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Kick ","")
                random.choice(KAC).kickoutFromGroup(msg.to,[midd])
            elif "Luffy kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("_second kick ","")
                ki.kickoutFromGroup(msg.to,[midd])
            elif "Zorro kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("_third kick ","")
                kk.kickoutFromGroup(msg.to,[midd])
            elif "Sanji kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("_fourth kick ","")
                kc.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "Luffy invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("sinvite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "Zorro invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("tinvite ","")
                kk.findAndAddContactsByMid(midd)
                kk.inviteIntoGroup(msg.to,[midd])
            elif "Zorro invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("finvite ","")
                kc.findAndAddContactsByMid(midd)
                kc.inviteIntoGroup(msg.to,[midd])
    #--------------- SC Add Admin ---------
            elif "Admin add @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff add executing"
                _name = msg.text.replace("Admin add @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = ks.getGroup(msg.to)
                gs = ka.getGroup(msg.to)
                gs = kb.getGroup(msg.to)
                gs = ku.getGroup(msg.to)
                gs = ke.getGroup(msg.to)
                gs = ko.getGroup(msg.to)
                gs = satpam.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.append(target)
                            cl.sendText(msg.to,"Admin Ditambahkan")
                        except:
                            pass
                print "[Command]Staff add executed"
              else:
                cl.sendText(msg.to,"Command denied.")
                cl.sendText(msg.to,"Admin permission required.")
                
            elif "Admin remove @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff remove executing"
                _name = msg.text.replace("Admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = ks.getGroup(msg.to)
                gs = ka.getGroup(msg.to)
                gs = kb.getGroup(msg.to)
                gs = ku.getGroup(msg.to)
                gs = ke.getGroup(msg.to)
                gs = ko.getGroup(msg.to)
                gs = satpam.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            cl.sendText(msg.to,"Admin Dihapus")
                        except:
                            pass
                print "[Command]Staff remove executed"
              else:
                cl.sendText(msg.to,"Command denied.")
                cl.sendText(msg.to,"Admin permission required.")
                
            elif msg.text in ["Adminlist","adminlist"]:
              if admin == []:
                  cl.sendText(msg.to,"The stafflist is empty")
              else:
                  cl.sendText(msg.to,"Tunggu...")
                  mc = "||Admin One Piece Bot||\n=====================\n"
                  for mi_d in admin:
                      mc += "••>" +cl.getContact(mi_d).displayName + "\n"
                  cl.sendText(msg.to,mc)
                  print "[Command]Stafflist executed"
    #--------------------------------------
    #--------------- SC Add Owner2 ---------
            elif "Owner add @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff add executing"
                _name = msg.text.replace("Owner add @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = ks.getGroup(msg.to)
                gs = ka.getGroup(msg.to)
                gs = kb.getGroup(msg.to)
                gs = ku.getGroup(msg.to)
                gs = ke.getGroup(msg.to)
                gs = ko.getGroup(msg.to)
                gs = satpam.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            owner.append(target)
                            cl.sendText(msg.to,"Owner Ditambahkan")
                        except:
                            pass
                print "[Command]Staff add executed"
              else:
                cl.sendText(msg.to,"Command denied.")
                cl.sendText(msg.to,"Owner permission required.")
                
            elif "Owner remove @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff remove executing"
                _name = msg.text.replace("Owner remove @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = ks.getGroup(msg.to)
                gs = ka.getGroup(msg.to)
                gs = kb.getGroup(msg.to)
                gs = ku.getGroup(msg.to)
                gs = ke.getGroup(msg.to)
                gs = ko.getGroup(msg.to)
                gs = satpam.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            owner.remove(target)
                            cl.sendText(msg.to,"Owner Dihapus")
                        except:
                            pass
                print "[Command]Staff remove executed"
              else:
                cl.sendText(msg.to,"Command denied.")
                cl.sendText(msg.to,"Owner permission required.")
                
            elif msg.text in ["Ownerlist","ownerlist"]:
              if owner == []:
                  cl.sendText(msg.to,"The stafflist is empty")
              else:
                  cl.sendText(msg.to,"Tunggu...")
                  mc = "||Owner One Piece Bot||\n=====================\n"
                  for mi_d in owner:
                      mc += "••>" +cl.getContact(mi_d).displayName + "\n"
                  cl.sendText(msg.to,mc)
                  print "[Command]Stafflist executed"
    #--------------------------------------    
    #-------------- Add Friends ------------
            elif "Bot Add @" in msg.text:
              if msg.toType == 2:
                if msg.from_ in owner:
                  print "[Command]Add executing"
                  _name = msg.text.replace("Bot Add @","")
                  _nametarget = _name.rstrip('  ')
                  gs = cl.getGroup(msg.to)
                  gs = ki.getGroup(msg.to)
                  gs = kk.getGroup(msg.to)
                  gs = kc.getGroup(msg.to)
                  gs = ks.getGroup(msg.to)
                  gs = ka.getGroup(msg.to)
                  gs = kb.getGroup(msg.to)
                  gs = ke.getGroup(msg.to)
                  gs = ko.getGroup(msg.to)
                  gs = ku.getGroup(msg.to)
                  targets = []
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    random.choice(KAC).sendText(msg.to,"Contact not found")
                  else:
                    for target in targets:
                      try:
                        cl.findAndAddContactsByMid(target)
                        ki.findAndAddContactsByMid(target)
                        kk.findAndAddContactsByMid(target)
                        kc.findAndAddContactsByMid(target)
                        ks.findAndAddContactsByMid(target)
                        ka.findAndAddContactsByMid(target)
                        kb.findAndAddContactsByMid(target)
                        ko.findAndAddContactsByMid(target)
                        ke.findAndAddContactsByMid(target)
                        ku.findAndAddContactsByMid(target)
                      except:
                        cl.sendText(msg.to,"Error")
              else:
                cl.sendText(msg.to,"Perintah Ditolak")
                cl.sendText(msg.to,"Perintah ini Hanya Untuk Owner Kami")
                  
    #-------------=SC AllBio=---------------- Ganti Bio Semua Bot Format => Allbio: SUKA SUKA KALIAN :D
            elif "Allbio:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kk.getProfile()
                    profile.statusMessage = string
                    kk.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kc.getProfile()
                    profile.statusMessage = string
                    kc.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ks.getProfile()
                    profile.statusMessage = string
                    ks.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ka.getProfile()
                    profile.statusMessage = string
                    ka.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kb.getProfile()
                    profile.statusMessage = string
                    kb.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ku.getProfile()
                    profile.statusMessage = string
                    ku.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ke.getProfile()
                    profile.statusMessage = string
                    ke.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ko.getProfile()
                    profile.statusMessage = string
                    ko.updateProfile(profile)
                    cl.sendText(msg.to,"Bio berubah menjadi " + string + "")
    #--------------=Finish=----------------
    #--------------= SC Ganti nama Owner=--------------
            elif "Myname1:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Myname1:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Name Menjadi : " + string + "")
            elif "Myname2:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Myname2:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"Update Name Menjadi : " + string + "")                 
            elif "Myname3:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Myname3:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = kk.getProfile()
                    profile.displayName = string
                    kk.updateProfile(profile)
                    kk.sendText(msg.to,"Update Name Menjadi : " + string + "")                                 
            elif "Myname4:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Myname4:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = kc.getProfile()
                    profile.displayName = string
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Update Name Menjadi : " + string + "")                                 
            elif "Myname5:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Myname5:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ks.getProfile()
                    profile.displayName = string
                    ks.updateProfile(profile)
                    ks.sendText(msg.to,"Update Name Menjadi : " + string + "")                                 
            elif "Myname6:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Myname6:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ka.getProfile()
                    profile.displayName = string
                    ka.updateProfile(profile)
                    ka.sendText(msg.to,"Update Name Menjadi : " + string + "")                                 
            elif "Myname7:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Myname7:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = kb.getProfile()
                    profile.displayName = string
                    kb.updateProfile(profile)
                    kb.sendText(msg.to,"Update Name Menjadi : " + string + "")                                 
            elif "Myname8:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Myname8:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ko.getProfile()
                    profile.displayName = string
                    ko.updateProfile(profile)
                    ko.sendText(msg.to,"Update Name Menjadi : " + string + "")  
            elif "Myname9:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Myname9:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ke.getProfile()
                    profile.displayName = string
                    ke.updateProfile(profile)
                    ke.sendText(msg.to,"Update Name Menjadi : " + string + "")                                 
            elif "Myname10:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Myname10:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ku.getProfile()
                    profile.displayName = string
                    ku.updateProfile(profile)
                    ku.sendText(msg.to,"Update Name Menjadi : " + string + "")                                 
            elif "Myname11:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Myname11:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = k1.getProfile()
                    profile.displayName = string
                    k1.updateProfile(profile)
                    k1.sendText(msg.to,"Update Name Menjadi : " + string + "")                  
    #-------------- copy profile----------
            elif "Spam: " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam: ")+str(txt[1])+" "+str(jmlh + " ","")
                tulisan = jmlh * (teks+"\n")
                 #@reno.a.w
                if txt[1] == "on":
                    if jmlh <= 300:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Kelebihan batas:v")
                elif txt[1] == "off":
                    if jmlh <= 300:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Kelebihan batas :v")
    #-----------------=Selesai=------------------
            elif msg.text in ["Bot?"]: #Ngirim Semua Kontak Bot
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
       
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                ks.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}
                ka.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Fmid}
                kb.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Gmid}
                ko.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Hmid}
                ke.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Imid}
                ku.sendMessage(msg)                
            elif msg.text in ["Me"]:
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["Cv2"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","All gift"]:
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
            elif msg.text in ["Cancel","cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        random.choice(KAC).cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Op cancel","Bot cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    G = k3.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        k3.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            k3.sendText(msg.to,"No one is inviting")
                        else:
                            k3.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        k3.sendText(msg.to,"Can not be used outside the group")
                    else:
                        k3.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Buka qr","Open qr"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = random.choice(KAC).getGroup(msg.to)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"QR Sudah Dibuka")
                    else:
                        random.choice(KAC).sendText(msg.to,"Sudah Terbuka Plak")
                else:
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Can not be used outside the group")
                    else:
                        random.choice(KAC).sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Luffy buka qr","Luffy open qr"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done Plak")
                    else:
                        cl.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Zorro buka qr","Zorro open qr"]:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done Plak")
                    else:
                        ki.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Sanji open qr","Sanji buka qr"]:
                if msg.toType == 2:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Done Plak")
                    else:
                        kc.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Tutup qr","Close qr"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = random.choice(KAC).getGroup(msg.to)
                    X.preventJoinByTicket = True
                    random.choice(KAC).updateGroup(X)
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Kode QR Sudah Di Tutup")
                    else:
                        random.choice(KAC).sendText(msg.to,"Sudah Tertutup Plak")
                else:
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Can not be used outside the group")
                    else:
                        random.choice(KAC).sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Luffy close qr","Luffy tutup qr"]:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done Plak")
                    else:
                        ki.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Zorro tutup qr","Zorro close qr"]:
                if msg.toType == 2:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Done Plak")
                    else:
                        kk.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Sanji tutup qr","Sanji close qr"]:
                if msg.toType == 2:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Done Plak")
                    else:
                        kc.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
                     
            elif "Info Group" == msg.text:
              if msg.toType == 2:
                if msg.from_ in admin:
                  ginfo = cl.getGroup(msg.to)
                  try:
                    gCreator = ginfo.creator.displayName
                  except:
                    gCreator = "Error"
                  if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                      sinvitee = "0"
                    else:
                      sinvitee = str(len(ginfo.invitee))
                    if ginfo.preventJoinByTicket == True:
                      QR = "Close"
                    else:
                      QR = "Open"
                    random.choice(KAC).sendText(msg.to,"[Group Name]\n" + "[•]" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + "[•]" + gCreator + "\n\n[Group Status]\n" + "[•]Status QR =>" + QR + "\n\n[Group Picture]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "\nPending:" + sinvitee)
                  else:
                    random.choice(KAC).sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Group Status]\nGroup Picture:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                  if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Can not be used outside the group")
                  else:
                    cl.sendText(msg.to,"Not for use less than group")
                
            elif "My mid" == msg.text:
              if msg.from_ in admin:
                random.choice(KAC).sendText(msg.to, msg.from_)
            elif "Mid Bot" == msg.text:
              if msg.from_ in admin:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
                kk.sendText(msg.to,Bmid)
                kc.sendText(msg.to,Cmid)
                ks.sendText(msg.to,Dmid)
                ka.sendText(msg.to,Emid)
                kb.sendText(msg.to,Fmid)
                ko.sendText(msg.to,Gmid)
                ke.sendText(msg.to,Hmid)
                ku.sendText(msg.to,Imid)
            elif "Luffy" == msg.text:
              if msg.from_ in admin:
                cl.sendText(msg.to,Smid)
            elif "Zorro" == msg.text:
              if msg.from_ in admin:
                ki.sendText(msg.to,mid)
            elif "Sanji" == msg.text:
              if msg.from_ in admin:
                kk.sendText(msg.to,Amid)
            elif "Ussop" == msg.text:
              if msg.from_ in admin:
                kc.sendText(msg.to,Bmid)
            elif msg.text in ["Wkwkwk","Wkwk","Wk","wkwkwk","wkwk","wk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hehehe","Hehe","He","hehehe","hehe","he"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Galau"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Please"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hmmm","Hmm","Hm","hmmm","hmm","hm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["TL: "]:
              if msg.from_ in admin:
                tl_text = msg.text.replace("TL: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Bot1 rename "]:
              if msg.from_ in admin:
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Bot2 rename "]:
              if msg.from_ in admin:
                string = msg.text.replace("Cv1 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ki.getProfile()
                    profile_B.displayName = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Bot3 rename "]:
              if msg.from_ in admin:
                string = msg.text.replace("Cv2 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kk.getProfile()
                    profile_B.displayName = string
                    kk.updateProfile(profile_B)
                    kk.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Mc "]:
              if msg.from_ in admin:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["Cancel on","cancel on"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel off","cancel off"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr on","qr on"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr off","qr off"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact On","Contact on","contact on"]:
              if msg.from_ in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact Off","Contact off","contact off"]:
              if msg.from_ in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ³","Join on","Auto join on","è‡ªå‹•å�ƒåŠ ï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ•","Join off","Auto join off","è‡ªå‹•å�ƒåŠ ï¼šé—œ"]:
              if msg.from_ in admin:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»�ã€‚è¦�æ—¶å¼€è¯·æŒ‡å®šäººæ•°å�‘é€�")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°�ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»�")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
              if msg.from_ in admin:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
              if msg.from_ in admin:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
              if msg.from_ in admin:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["set"]:
              if msg.from_ in admin:
                md = "⭐Status Proteksi⭐\n*============*\n"
                if wait["Protectgr"] == True: md+="[•]Protect QR [On]\n"
                else: md+="[•]Protect QR [Off]\n"
                if wait["Protectcancl"] == True: md+="[•]Protect Invite [On]\n"
                else: md+="[•]Protect Invite [Off]\n"
                if wait["contact"] == True: md+="[•]Contact [On]\n"
                else: md+="[•]Contact [Off]\n"
                if wait["autoJoin"] == True: md+="[•]Auto Join [On]\n"
                else: md +="[•]Auto Join [Off]\n"
                if wait["autoCancel"]["on"] == True:md+="[•]Group Cancel " + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= "[•]Group Cancel [Off]\n"
                if wait["leaveRoom"] == True: md+="[•]Auto Leave [On]\n"
                else: md+=" Auto Leave [Off]\n"
                if wait["timeline"] == True: md+="[•]Share [On]\n"
                else:md+="[•]Share [Off]\n"
                if wait["autoAdd"] == True: md+="[•]Auto Add [On]\n"
                else:md+="[•]Auto Add [Off]\n"
                if wait["commentOn"] == True: md+="[•]Comment [On]\n"
                else:md+="[•]Comment [Off]\n*============*\n⭐One Piece Bot⭐\n*============*"
                cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "album " in msg.text:
                gid = msg.text.replace("album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
                gid = msg.text.replace("album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Group id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:\n%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»�äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "album removeat’" in msg.text:
                gid = msg.text.replace("album removeat’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"Done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
              if msg.from_ in admin:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
