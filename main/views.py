from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Equipment, Reservation, AvailableReservationsTrack, Work
from .forms import ContactForm, PasswordChange, ChangeEmailForm
from datetime import date, datetime
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, authenticate, login

def home(request):
    return render(request, 'main/home.html', {})

def reservations_eq_date(request):
    if request.method == 'POST':
        print(request.POST) 
        date = request.POST.get('myDate')
        hour = request.POST.get('myTime')
        request.session['date_p'] = date
        request.session['hour_p'] = hour
        return HttpResponseRedirect("/reservations_eq", {})
    return render(request, 'main/reservations_eq_date.html', {})

def reservations_eq(request):
    eq = Equipment.objects.all()
    date = request.session['date_p']
    hour = request.session['hour_p']
    reservation = Reservation.objects.filter(date=date, hour = hour)
    amounts = {}
    print(str(date) + " " + str(hour))

    for item in eq:
        amounts[str(item.eq_name)] = str(item.amount)
        count = 0
        for res in reservation:
            if res.equipment == item:
               count = count + 1
            amounts[str(item.eq_name)] = str(item.amount-count) 

    if request.method == 'POST':
        print(request.POST)
        radio = request.POST.get('radio')
        if radio==None:
            return render(request, 'main/reservations_eq.html', {'eq':eq,'amounts':amounts})
        else:
            reservations_amount = Reservation.objects.count() + 1 
            if int(amounts[str(radio)]) > 0:
                request.session['reservations_amount'] = reservations_amount
                request.session['radio'] = radio
                return HttpResponseRedirect("/reservations_eq_finalize", {})
            else:
                return render(request, 'main/reservations_eq.html', {'eq':eq,'amounts':amounts})
    return render(request, 'main/reservations_eq.html', {'eq':eq,'amounts':amounts})


def reservations_eq_finalize(request):
    reservations_amount = request.session['reservations_amount']
    date = request.session['date_p']
    hour_got = request.session['hour_p']
    hour_cut = hour_got[:-3]
    hour = int(hour_cut)
    hour_end = hour + 1

    hour_str = str(hour) + ":00:00"

    reservation_date = datetime.strptime(date, '%Y-%m-%d').date().strftime('%d/%m/%Y')

    radio = request.session['radio']
    equip = Equipment.objects.get(eq_name = radio)
    
    equip_name = Equipment.objects.get(eq_name = radio).eq_name

    print(equip)

    if request.method == 'POST':
        print(request.POST)
        res = Reservation(reservation_id = reservations_amount, date = date, hour = hour_str, equipment = equip)
        res.save()
        request.user.reservation.add(res)
        return render(request, 'main/reservations_eq_success.html', {})
    
    context = {
        'reservation_date':reservation_date,
        'hour':hour,
        'hour_end':hour_end,
        'equip_name':equip_name,
    }

    return render(request, 'main/reservations_eq_finalize.html', context)


def reservations_tracks_date(request):
    if request.method == 'POST':
        print(request.POST) 
        date = request.POST.get('myDate')
        request.session['date_p'] = date
        return HttpResponseRedirect("/reservations_tracks", {})
    return render(request, 'main/reservations_tracks_date.html', {})


def reservations_tracks(request):
    date = request.session['date_p']
    reservation_date = datetime.strptime(date, '%Y-%m-%d').date().strftime('%d/%m/%Y')
    av_reservations = AvailableReservationsTrack.objects.filter(date=date).values_list("time_from","time_to", "track1", "track2", "track3", "track4", "track5", "track6", flat=False)
    for item in av_reservations:
        print(item)

    print(date)

    av_reservations = AvailableReservationsTrack.objects.filter(date=date)

    reservations = Reservation.objects.filter(date=date)

    t1_8 = 'Z'
    t2_8 = 'Z'
    t3_8 = 'Z'
    t4_8 = 'Z'
    t5_8 = 'Z'
    t6_8 = 'Z'

    t1_9 = 'Z'
    t2_9 = 'Z'
    t3_9 = 'Z'
    t4_9 = 'Z'
    t5_9 = 'Z'
    t6_9 = 'Z'

    t1_10 = 'Z'
    t2_10 = 'Z'
    t3_10 = 'Z'
    t4_10 = 'Z'
    t5_10 = 'Z'
    t6_10 = 'Z'

    t1_11 = 'Z'
    t2_11 = 'Z'
    t3_11 = 'Z'
    t4_11 = 'Z'
    t5_11 = 'Z'
    t6_11 = 'Z'

    t1_12 = 'Z'
    t2_12 = 'Z'
    t3_12 = 'Z'
    t4_12 = 'Z'
    t5_12 = 'Z'
    t6_12 = 'Z'

    t1_13 = 'Z'
    t2_13 = 'Z'
    t3_13 = 'Z'
    t4_13 = 'Z'
    t5_13 = 'Z'
    t6_13 = 'Z'

    t1_14 = 'Z'
    t2_14 = 'Z'
    t3_14 = 'Z'
    t4_14 = 'Z'
    t5_14 = 'Z'
    t6_14 = 'Z'

    t1_15 = 'Z'
    t2_15 = 'Z'
    t3_15 = 'Z'
    t4_15 = 'Z'
    t5_15 = 'Z'
    t6_15 = 'Z'

    t1_16 = 'Z'
    t2_16 = 'Z'
    t3_16 = 'Z'
    t4_16 = 'Z'
    t5_16 = 'Z'
    t6_16 = 'Z'

    t1_17 = 'Z'
    t2_17 = 'Z'
    t3_17 = 'Z'
    t4_17 = 'Z'
    t5_17 = 'Z'
    t6_17 = 'Z'

    t1_18 = 'Z'
    t2_18 = 'Z'
    t3_18 = 'Z'
    t4_18 = 'Z'
    t5_18 = 'Z'
    t6_18 = 'Z'
    
    t1_19 = 'Z'
    t2_19 = 'Z'
    t3_19 = 'Z'
    t4_19 = 'Z'
    t5_19 = 'Z'
    t6_19 = 'Z'


    for item in av_reservations:
        for hour in range(int(item.time_from.hour),int(item.time_to.hour),1):
            #print(item.time_from.hour)

            #hour = int(item.time_from.hour)

            if hour >= 8 and hour < 9:
                if item.track1 == True:
                    t1_8 = 'W'
                if item.track2 == True:
                    t2_8 = 'W'
                if item.track3 == True:
                    t3_8 = 'W'
                if item.track4 == True:
                    t4_8 = 'W'
                if item.track5 == True:
                    t5_8 = 'W'
                if item.track6 == True:
                    t6_8 = 'W'

            if hour >= 9 and hour < 10:
                if item.track1 == True:
                    t1_9 = 'W'
                if item.track2 == True:
                    t2_9 = 'W'
                if item.track3 == True:
                    t3_9 = 'W'
                if item.track4 == True:
                    t4_9 = 'W'
                if item.track5 == True:
                    t5_9 = 'W'
                if item.track6 == True:
                    t6_9 = 'W'

            if hour >= 10 and hour < 11:
                if item.track1 == True:
                    t1_10 = 'W'
                if item.track2 == True:
                    t2_10 = 'W'
                if item.track3 == True:
                    t3_10 = 'W'
                if item.track4 == True:
                    t4_10 = 'W'
                if item.track5 == True:
                    t5_10 = 'W'
                if item.track6 == True:
                    t6_10 = 'W'

            if hour >= 11 and hour < 12:
                if item.track1 == True:
                    t1_11 = 'W'
                if item.track2 == True:
                    t2_11 = 'W'
                if item.track3 == True:
                    t3_11 = 'W'
                if item.track4 == True:
                    t4_11 = 'W'
                if item.track5 == True:
                    t5_11 = 'W'
                if item.track6 == True:
                    t6_11 = 'W'

            if hour >= 12 and hour < 13:
                if item.track1 == True:
                    t1_12 = 'W'
                if item.track2 == True:
                    t2_12 = 'W'
                if item.track3 == True:
                    t3_12 = 'W'
                if item.track4 == True:
                    t4_12 = 'W'
                if item.track5 == True:
                    t5_12 = 'W'
                if item.track6 == True:
                    t6_12 = 'W'

            if hour >= 13 and hour < 14:
                if item.track1 == True:
                    t1_13 = 'W'
                if item.track2 == True:
                    t2_13 = 'W'
                if item.track3 == True:
                    t3_13 = 'W'
                if item.track4 == True:
                    t4_13 = 'W'
                if item.track5 == True:
                    t5_13 = 'W'
                if item.track6 == True:
                    t6_13 = 'W'
            
            if hour >= 14 and hour < 15:
                if item.track1 == True:
                    t1_14 = 'W'
                if item.track2 == True:
                    t2_14 = 'W'
                if item.track3 == True:
                    t3_14 = 'W'
                if item.track4 == True:
                    t4_14 = 'W'
                if item.track5 == True:
                    t5_14 = 'W'
                if item.track6 == True:
                    t6_14 = 'W'

            if hour >= 15 and hour < 16:
                if item.track1 == True:
                    t1_15 = 'W'
                if item.track2 == True:
                    t2_15 = 'W'
                if item.track3 == True:
                    t3_15 = 'W'
                if item.track4 == True:
                    t4_15 = 'W'
                if item.track5 == True:
                    t5_15 = 'W'
                if item.track6 == True:
                    t6_15 = 'W'

            if hour >= 16 and hour < 17:
                if item.track1 == True:
                    t1_16 = 'W'
                if item.track2 == True:
                    t2_16 = 'W'
                if item.track3 == True:
                    t3_16 = 'W'
                if item.track4 == True:
                    t4_16 = 'W'
                if item.track5 == True:
                    t5_16 = 'W'
                if item.track6 == True:
                    t6_16= 'W'

            if hour >= 17 and hour < 18:
                if item.track1 == True:
                    t1_17 = 'W'
                if item.track2 == True:
                    t2_17 = 'W'
                if item.track3 == True:
                    t3_17 = 'W'
                if item.track4 == True:
                    t4_17 = 'W'
                if item.track5 == True:
                    t5_17 = 'W'
                if item.track6 == True:
                    t6_17 = 'W'

            if hour >= 18 and hour < 19:
                if item.track1 == True:
                    t1_18 = 'W'
                if item.track2 == True:
                    t2_18 = 'W'
                if item.track3 == True:
                    t3_18 = 'W'
                if item.track4 == True:
                    t4_18 = 'W'
                if item.track5 == True:
                    t5_18 = 'W'
                if item.track6 == True:
                    t6_18 = 'W'

            if hour >= 19 and hour < 20:
                if item.track1 == True:
                    t1_19 = 'W'
                if item.track2 == True:
                    t2_19 = 'W'
                if item.track3 == True:
                    t3_19 = 'W'
                if item.track4 == True:
                    t4_19 = 'W'
                if item.track5 == True:
                    t5_19 = 'W'
                if item.track6 == True:
                    t6_19 = 'W'


    for item in reservations:
        if item.track != None:

            if item.hour.hour == 8:
                if item.track == 1:
                    t1_8 = "Z"
                if item.track == 2:
                    t2_8 = "Z"
                if item.track == 3:
                    t3_8 = "Z"
                if item.track == 4:
                    t4_8 = "Z"
                if item.track == 5:
                    t5_8 = "Z"
                if item.track == 6:
                    t6_8 = "Z"

            if item.hour.hour == 9:
                if item.track == 1:
                    t1_9 = "Z"
                if item.track == 2:
                    t2_9 = "Z"
                if item.track == 3:
                    t3_9 = "Z"
                if item.track == 4:
                    t4_9 = "Z"
                if item.track == 5:
                    t5_9 = "Z"
                if item.track == 6:
                    t6_9 = "Z"    
            
            if item.hour.hour == 10:
                if item.track == 1:
                    t1_10 = "Z"
                if item.track == 2:
                    t2_10 = "Z"
                if item.track == 3:
                    t3_10 = "Z"
                if item.track == 4:
                    t4_10 = "Z"
                if item.track == 5:
                    t5_10 = "Z"
                if item.track == 6:
                    t6_10 = "Z"    

            if item.hour.hour == 11:
                if item.track == 1:
                    t1_11 = "Z"
                if item.track == 2:
                    t2_11 = "Z"
                if item.track == 3:
                    t3_11 = "Z"
                if item.track == 4:
                    t4_11 = "Z"
                if item.track == 5:
                    t5_11 = "Z"
                if item.track == 6:
                    t6_11 = "Z"    

            if item.hour.hour == 12:
                if item.track == 1:
                    t1_12 = "Z"
                if item.track == 2:
                    t2_12 = "Z"
                if item.track == 3:
                    t3_12 = "Z"
                if item.track == 4:
                    t4_12 = "Z"
                if item.track == 5:
                    t5_12 = "Z"
                if item.track == 6:
                    t6_12 = "Z"    

            if item.hour.hour == 13:
                if item.track == 1:
                    t1_13 = "Z"
                if item.track == 2:
                    t2_13 = "Z"
                if item.track == 3:
                    t3_13 = "Z"
                if item.track == 4:
                    t4_13 = "Z"
                if item.track == 5:
                    t5_13 = "Z"
                if item.track == 6:
                    t6_13 = "Z"    

            if item.hour.hour == 14:
                if item.track == 1:
                    t1_14 = "Z"
                if item.track == 2:
                    t2_14 = "Z"
                if item.track == 3:
                    t3_14 = "Z"
                if item.track == 4:
                    t4_14 = "Z"
                if item.track == 5:
                    t5_14 = "Z"
                if item.track == 6:
                    t6_14 = "Z"    
            
            if item.hour.hour == 15:
                if item.track == 1:
                    t1_15 = "Z"
                if item.track == 2:
                    t2_15 = "Z"
                if item.track == 3:
                    t3_15 = "Z"
                if item.track == 4:
                    t4_15 = "Z"
                if item.track == 5:
                    t5_15 = "Z"
                if item.track == 6:
                    t6_15 = "Z"    

            if item.hour.hour == 16:
                if item.track == 1:
                    t1_16 = "Z"
                if item.track == 2:
                    t2_16 = "Z"
                if item.track == 3:
                    t3_16 = "Z"
                if item.track == 4:
                    t4_16 = "Z"
                if item.track == 5:
                    t5_16 = "Z"
                if item.track == 6:
                    t6_16 = "Z"    

            if item.hour.hour == 17:
                if item.track == 1:
                    t1_17 = "Z"
                if item.track == 2:
                    t2_17 = "Z"
                if item.track == 3:
                    t3_17 = "Z"
                if item.track == 4:
                    t4_17 = "Z"
                if item.track == 5:
                    t5_17 = "Z"
                if item.track == 6:
                    t6_17 = "Z"    

            if item.hour.hour == 18:
                if item.track == 1:
                    t1_18 = "Z"
                if item.track == 2:
                    t2_18 = "Z"
                if item.track == 3:
                    t3_18 = "Z"
                if item.track == 4:
                    t4_18 = "Z"
                if item.track == 5:
                    t5_18 = "Z"
                if item.track == 6:
                    t6_18 = "Z"    

            if item.hour.hour == 19:
                if item.track == 1:
                    t1_19 = "Z"
                if item.track == 2:
                    t2_19 = "Z"
                if item.track == 3:
                    t3_19 = "Z"
                if item.track == 4:
                    t4_19 = "Z"
                if item.track == 5:
                    t5_19 = "Z"
                if item.track == 6:
                    t6_19 = "Z"    

        
    context = {
        't1_8': t1_8,
        't2_8': t2_8,
        't3_8': t3_8,
        't4_8': t4_8,
        't5_8': t5_8,
        't6_8': t6_8,
        't1_9': t1_9,
        't2_9': t2_9,
        't3_9': t3_9,
        't4_9': t4_9,
        't5_9': t5_9,
        't6_9': t6_9,
        't1_10': t1_10,
        't2_10': t2_10,
        't3_10': t3_10,
        't4_10': t4_10,
        't5_10': t5_10,
        't6_10': t6_10,
        't1_11': t1_11,
        't2_11': t2_11,
        't3_11': t3_11,
        't4_11': t4_11,
        't5_11': t5_11,
        't6_11': t6_11,
        't1_12': t1_12,
        't2_12': t2_12,
        't3_12': t3_12,
        't4_12': t4_12,
        't5_12': t5_12,
        't6_12': t6_12,
        't1_13': t1_13,
        't2_13': t2_13,
        't3_13': t3_13,
        't4_13': t4_13,
        't5_13': t5_13,
        't6_13': t6_13,
        't1_14': t1_14,
        't2_14': t2_14,
        't3_14': t3_14,
        't4_14': t4_14,
        't5_14': t5_14,
        't6_14': t6_14,
        't1_15': t1_15,
        't2_15': t2_15,
        't3_15': t3_15,
        't4_15': t4_15,
        't5_15': t5_15,
        't6_15': t6_15,
        't1_16': t1_16,
        't2_16': t2_16,
        't3_16': t3_16,
        't4_16': t4_16,
        't5_16': t5_16,
        't6_16': t6_16,
        't1_17': t1_17,
        't2_17': t2_17,
        't3_17': t3_17,
        't4_17': t4_17,
        't5_17': t5_17,
        't6_17': t6_17,
        't1_18': t1_18,
        't2_18': t2_18,
        't3_18': t3_18,
        't4_18': t4_18,
        't5_18': t5_18,
        't6_18': t6_18,
        't1_19': t1_19,
        't2_19': t2_19,
        't3_19': t3_19,
        't4_19': t4_19,
        't5_19': t5_19,
        't6_19': t6_19,
        'reservation_date': reservation_date,
    }

    if request.method == 'POST':
        print(request.POST)
        radio = request.POST.get('radio')
        print(radio)

        if radio == None:
            render(request, 'main/reservations_tracks.html', context)
        else:
            track = radio[1]
            hour = str(radio [3:len(radio)])
            request.session['track_selected'] = track
            request.session['hour_selected'] = hour
            return HttpResponseRedirect("/reservations_tracks_finalize", {})

    return render(request, 'main/reservations_tracks.html', context)



def reservations_tracks_finalize(request):
    
    reservations_amount = Reservation.objects.count() + 1
    date = request.session['date_p']
    reservation_date = datetime.strptime(date, '%Y-%m-%d').date().strftime('%d/%m/%Y')

    hour = int(request.session['hour_selected'])
    hour_end = hour + 1
    track = int(request.session['track_selected'])

    hour_str = str(hour) + ":00:00"

    if request.method == 'POST':
        print(request.POST)
        print(reservations_amount, date, hour, track)
        ress = Reservation(reservation_id = reservations_amount, date = date, hour = hour_str, track = track)
        ress.save()
        request.user.reservation.add(ress)
        return render(request, 'main/reservations_tracks_success.html', {})
    

    context = {
        'reservation_date': reservation_date,
        'hour': hour,
        'hour_end': hour_end,
        'track': track,
    }

    return render(request, 'main/reservations_tracks_finalize.html', context)


def reservations_show_all(request, sort_field='date', sort_order='desc'):
    reservations = Reservation.objects.all()

    if request.GET.get('filter_field'):
        reservations = reservations.filter(field_to_filter=request.GET['filter_field'])

    if sort_order == 'desc':
        sort_prefix = '-'
    else:
        sort_prefix = ''

    reservations = reservations.order_by(sort_prefix + sort_field)

    context = {
        'reservations':reservations,
        'sort_field': sort_field,
        'sort_order': sort_order,
    }

    return render(request, 'main/reservations_show_all.html', context)

def reservations_show_user(request, sort_field='date', sort_order='desc'):
    user = request.user
    reservations = Reservation.objects.filter(user=user)

    if sort_order == 'desc':
        sort_prefix = '-'
    else:
        sort_prefix = ''

    reservations = reservations.order_by(sort_prefix + sort_field)
    
    context = {
        'reservations':reservations,
    }

    return render(request, 'main/reservations_show_user.html', context)


def reservations_tracks_add(request):
    
    if request.method == 'POST':
        print(request.POST)

        track1 = False
        track2 = False
        track3 = False
        track4 = False
        track5 = False
        track6 = False

        if 'track1' in request.POST:
            check1 = request.POST['track1']
            if check1 == 'on':
                track1 = True
        
        if 'track2' in request.POST:
            check2 = request.POST['track2']
            if check2 == 'on':
                track2 = True

        if 'track3' in request.POST:
            check3 = request.POST['track3']
            if check3 == 'on':
                track3 = True

        if 'track4' in request.POST:
            check4 = request.POST['track4']
            if check4 == 'on':
                track4 = True

        if 'track5' in request.POST:
            check5 = request.POST['track5']
            if check5 == 'on':
                track5 = True

        if 'track6' in request.POST:
            check6 = request.POST['track6']
            if check6 == 'on':
                track6 = True
        
        date_res = request.POST['date_res']
        time_from = request.POST['time_from']
        time_to = request.POST['time_to']

        print(date_res)
        print(time_from)
        print(time_to)
        print(track1)
        print(track2)
        print(track3)
        print(track4)
        print(track5)
        print(track6)
        
        av_res = AvailableReservationsTrack(date=date_res, time_from=time_from, time_to=time_to, track1=track1, track2=track2, track3=track3, track4=track4, track5=track5, track6=track6)
        av_res.save()
        print("Dodano dostepnosci torów")

        return render(request, 'main/reservations_tracks_add.html', {})

    return render(request, 'main/reservations_tracks_add.html', {})


def work(request):
    newest_work = Work.objects.filter(user=request.user).order_by('-time').first()

    if newest_work is None:
        work_text = "Nie pracujesz"
    elif newest_work.is_working == False:
        work_text = "Nie pracujesz"
    else:
        work_text = "Pracujesz"

    if request.method == 'POST':
        if request.POST.get('start'):
            work_obj = Work(user=request.user, time=datetime.now(), is_working=True)
            work_obj.save()
            request.user.work.add(work_obj)
            work_text = "Pracujesz"
        elif request.POST.get('stop'):
            work_obj = Work(user=request.user, time=datetime.now(), is_working=False)
            work_obj.save()
            request.user.work.add(work_obj)
            work_text = "Nie pracujesz"

    context = {
        'work_text': work_text,
    }

    return render(request, 'main/work.html', context)


def storage(request):
    eq = Equipment.objects.all()
    amounts = {}

    for item in eq:
        amounts[str(item.eq_name).replace(' ', '_')] = str(item.amount)

    print(amounts)

    if request.method == 'POST':
        item1_value = request.POST.get('item1')
        item2_value = request.POST.get('item2')
        item3_value = request.POST.get('item3')
        item4_value = request.POST.get('item4')
        item5_value = request.POST.get('item5')
        item6_value = request.POST.get('item6')

        obj1 = Equipment.objects.get(eq_id=1)
        obj1.amount = int(item1_value)
        obj1.save()

        obj2 = Equipment.objects.get(eq_id=2)
        obj2.amount = int(item2_value)
        obj2.save()
        
        obj3 = Equipment.objects.get(eq_id=3)
        obj3.amount = int(item3_value)
        obj3.save()

        obj4 = Equipment.objects.get(eq_id=4)
        obj4.amount = int(item4_value)
        obj4.save()

        obj5 = Equipment.objects.get(eq_id=5)
        obj5.amount = int(item5_value)
        obj5.save()

        obj6 = Equipment.objects.get(eq_id=6)
        obj6.amount = int(item6_value)
        obj6.save()

        print(amounts.keys())
        
        return HttpResponseRedirect("/storage", {})


    context = {
        'eq':eq,
        'amounts':amounts,
    }
    return render(request, 'main/storage.html', context)


def work_show(request, sort_field='time', sort_order='desc'):
    works = Work.objects.all()

    if sort_order == 'desc':
        sort_prefix = '-'
    else:
        sort_prefix = ''

    works = works.order_by(sort_prefix + sort_field)

    context = {
        'works':works,
        'sort_field': sort_field,
        'sort_order': sort_order,
    }

    return render(request, 'main/work_show.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            subject = f'New message from {name} ({email})'
            message = f'{message}\n\n{name}'
            sender = settings.EMAIL_HOST_USER
            rec = 'myswimmingpoolsend@gmail.com'
            recipient = [rec,]
            
            send_mail(subject, message, sender, recipient, fail_silently=False)
            
            return render(request, 'main/contact_thanks.html')
    else:
        form = ContactForm()
    
    return render(request, 'main/contact.html', {'form': form})

def account(request):
    
    return render(request, 'main/account.html', {})


def account_change_password(request):
    if request.method == 'POST':
        form = PasswordChange(request.POST)
        if form.is_valid():
            user = request.user
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']
            new_password_again = form.cleaned_data['new_password_again']

            if not user.check_password(old_password):
                messages.error(request, 'Wprowadziłeś złe hasło. Spróbuj ponownie.')
            elif new_password != new_password_again:
                messages.error(request, 'Hasła się nie zgadzają. Spróbuj ponownie.')
            else:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
                user = authenticate(username=user.username, password=new_password)
                login(request, user)
                return render(request, 'main/account_change_password_success.html')
        else:
            for field in form.errors:
                for error in form.errors[field]:
                    messages.error(request, f'{field.capitalize()}: {error}')
    else:
        form = PasswordChange()

    context = {
        'form':form,
    }
    return render(request, 'main/account_change_password.html', context)





def account_change_email(request):
    if request.method == 'POST':
        form = ChangeEmailForm(request.POST)
        if form.is_valid():
            new_email = form.cleaned_data.get('email')
            request.user.email = new_email
            request.user.save()
            return render(request, 'main/account_change_email_success.html')
        else:
            for field in form.errors:
                for error in form.errors[field]:
                    messages.error(request, f'{field.capitalize()}: {error}')
    else:
        form = ChangeEmailForm()

    return render(request, 'main/account_change_email.html', {'form': form})