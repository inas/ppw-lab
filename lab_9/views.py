# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
#catatan: tidak bisa menampilkan messages jika bukan menggunakan method 'render'
from .api_enterkomputer import get_drones, get_soundcard, get_optical

response = {}

# NOTE : untuk membantu dalam memahami tujuan dari suatu fungsi (def)
# Silahkan jelaskan menggunakan bahasa kalian masing-masing, di bagian atas
# sebelum fungsi tersebut.

# ======================================================================== #
# User Func
# Apa yang dilakukan fungsi INI? #silahkan ganti ini dengan penjelasan kalian 
# kalau pada session belum login maka akan diredirect ke halaman login.
# kalau sudah login maka akan diarahkan ke profil
def index(request):
    print ("#==> masuk index")
    if 'user_login' in request.session:
        return HttpResponseRedirect(reverse('lab-9:profile'))
    else:
        html = 'lab_9/session/login.html'
        return render(request, html, response)


def set_data_for_session(res, request):
    response['author'] = request.session['user_login']
    response['access_token'] = request.session['access_token']
    response['kode_identitas'] = request.session['kode_identitas']
    response['role'] = request.session['role']
    response['drones'] = get_drones().json()    
    response['soundcard'] = get_soundcard().json()
    response['optical'] = get_optical().json()
    print(response['drones'])
    print(response['optical'])

    # print ("#drones = ", get_drones().json(), " - response = ", response['drones'])
    ## handling agar tidak error saat pertama kali login (session kosong)
    if 'drones' in request.session.keys():
        response['fav_drones'] = request.session['drones']
    # jika tidak ditambahkan else, cache akan tetap menyimpan data
    # sebelumnya yang ada pada response, sehingga data tidak up-to-date
    else:
        response['fav_drones'] = []

    if 'soundcard' in request.session.keys():
        response['fav_soundcard'] = request.session['soundcard']
    else:
        response['fav_soundcard'] = []

    if 'optical' in request.session.keys():
        response['fav_optical'] = request.session['optical']
    else:
        response['fav_optical'] = []


def profile(request):
    print ("#==> profile")
    ## sol : bagaimana cara mencegah error, jika url profile langsung diakses
    if 'user_login' not in request.session.keys():
        return HttpResponseRedirect(reverse('lab-9:index'))
    ## end of sol

    set_data_for_session(response, request)

    html = 'lab_9/session/profile.html'
    return render(request, html, response)

# ======================================================================== #

### Drones
def add_session_drones(request, id):
    ssn_key = request.session.keys()
    if not 'drones' in ssn_key:
        print ("# init drones ")
        request.session['drones'] = [id]
    else:
        drones = request.session['drones']
        print ("# existing drones => ", drones)
        if id not in drones:
            print ('# add new item, then save to session')
            drones.append(id)
            request.session['drones'] = drones

    messages.success(request, "Berhasil tambah drone favorite")
    return HttpResponseRedirect(reverse('lab-9:profile'))

def del_session_drones(request, id):
    print ("# DEL drones")
    drones = request.session['drones']
    print ("before = ", drones)
    drones.remove(id) #untuk remove id tertentu dari list
    request.session['drones'] = drones
    print ("after = ", drones)

    messages.error(request, "Berhasil hapus dari favorite")
    return HttpResponseRedirect(reverse('lab-9:profile'))

def clear_session_drones(request):
    print ("# CLEAR session drones")
    print ("before 1 = ", request.session['drones'])
    del request.session['drones']

    messages.error(request, "Berhasil reset favorite drones")
    return HttpResponseRedirect(reverse('lab-9:profile'))

### Soundcard
def add_session_soundcard(request, id):
    ssn_key = request.session.keys()
    if not 'soundcard' in ssn_key:
        print ("# init soundcard ")
        request.session['soundcard'] = [id]
    else:
        soundcard = request.session['soundcard']
        print ("# existing soundcard => ", soundcard)
        if id not in soundcard:
            print ('# add new item, then save to session')
            soundcard.append(id)
            request.session['soundcard'] = soundcard

    messages.success(request, "Berhasil tambah soundcard favorite")
    return HttpResponseRedirect(reverse('lab-9:profile'))

def del_session_soundcard(request, id):
    print ("# DEL soundcard")
    soundcard = request.session['soundcard']
    print ("before = ", soundcard)
    soundcard.remove(id) #untuk remove id tertentu dari list
    request.session['soundcard'] = soundcard
    print ("after = ", soundcard)

    messages.error(request, "Berhasil hapus dari favorite")
    return HttpResponseRedirect(reverse('lab-9:profile'))

def clear_session_soundcard(request):
    print ("# CLEAR session soundcard")
    print ("before 1 = ", request.session['soundcard'])
    del request.session['soundcard']

    messages.error(request, "Berhasil reset favorite soundcard")
    return HttpResponseRedirect(reverse('lab-9:profile'))

### Optical
def add_session_optical(request, id):
    ssn_key = request.session.keys()
    if not 'optical' in ssn_key:
        print ("# init optical ")
        request.session['optical'] = [id]
    else:
        optical = request.session['optical']
        print ("# existing optical => ", optical)
        if id not in optical:
            print ('# add new item, then save to session')
            optical.append(id)
            request.session['optical'] = optical

    messages.success(request, "Berhasil tambah optical favorite")
    return HttpResponseRedirect(reverse('lab-9:profile'))

def del_session_optical(request, id):
    print ("# DEL optical")
    optical = request.session['optical']
    print ("before = ", optical)
    optical.remove(id) #untuk remove id tertentu dari list
    request.session['optical'] = optical
    print ("after = ", optical)

    messages.error(request, "Berhasil hapus dari favorite")
    return HttpResponseRedirect(reverse('lab-9:profile'))

def clear_session_optical(request):
    print ("# CLEAR session optical")
    print ("before 1 = ", request.session['optical'])
    del request.session['optical']

    messages.error(request, "Berhasil reset favorite optical")
    return HttpResponseRedirect(reverse('lab-9:profile'))


# ======================================================================== #
# COOKIES

# Apa yang dilakukan fungsi INI? #silahkan ganti ini dengan penjelasan kalian 
def cookie_login(request):
    print ("#==> masuk login")
    if is_login(request):
        return HttpResponseRedirect(reverse('lab-9:cookie_profile'))
    else:
        html = 'lab_9/cookie/login.html'
        return render(request, html, response)

def cookie_auth_login(request):
    print ("# Auth login")
    if request.method == "POST":
        user_login = request.POST['username']
        user_password = request.POST['password']

        if my_cookie_auth(user_login, user_password):
            print ("#SET cookies")
            res = HttpResponseRedirect(reverse('lab-9:cookie_login'))

            res.set_cookie('user_login', user_login)
            res.set_cookie('user_password', user_password)

            return res
        else:
            msg = "Username atau Password Salah"
            messages.error(request, msg)
            return HttpResponseRedirect(reverse('lab-9:cookie_login'))
    else:
        return HttpResponseRedirect(reverse('lab-9:cookie_login'))

def cookie_profile(request):
    print ("# cookie profile ")
    # method ini untuk mencegah error ketika akses URL secara langsung
    if not is_login(request):
        print ("belum login")
        return HttpResponseRedirect(reverse('lab-9:cookie_login'))
    else:
        # print ("cookies => ", request.COOKIES)
        in_uname = request.COOKIES['user_login']
        in_pwd= request.COOKIES['user_password']

        # jika cookie diset secara manual (usaha hacking), distop dengan cara berikut
        # agar bisa masuk kembali, maka hapus secara manual cookies yang sudah diset
        if my_cookie_auth(in_uname, in_pwd):
            html = "lab_9/cookie/profile.html"
            res =  render(request, html, response)
            return res
        else:
            print ("#login dulu")
            msg = "Kamu tidak punya akses :P "
            messages.error(request, msg)
            html = "lab_9/cookie/login.html"
            return render(request, html, response)

def cookie_clear(request):
    res = HttpResponseRedirect('/lab-9/cookie/login')
    res.delete_cookie('user_password')
    res.delete_cookie('user_login')

    msg = "Anda berhasil logout. Cookies direset"
    messages.info(request, msg)
    return res

# Apa yang dilakukan fungsi ini?
def my_cookie_auth(in_uname, in_pwd):
    my_uname = "usher" #SILAHKAN ganti dengan USERNAME yang kalian inginkan
    my_pwd = "jbjb" #SILAHKAN ganti dengan PASSWORD yang kalian inginkan
    return in_uname == my_uname and in_pwd == my_pwd

#Apa yang dilakukan fungsi ini? 
def is_login(request):
    return 'user_login' in request.COOKIES and 'user_password' in request.COOKIES
