from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from app import funcs_aparts, funcs_bookings
from django.views.decorators.csrf import csrf_exempt


@login_required
def apartment(request):
    if request.method == 'POST':
        result = funcs_aparts.save_apart(request)
        return JsonResponse(result)
    elif request.method == 'DELETE':
        result = funcs_aparts.del_apart(request)
        return JsonResponse(result)

    result = funcs_aparts.get_aparts(request.GET("id", None))
    context = {
        'result': result
    }
    return render(request, 'apartments.html', context=context)

@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        result = funcs_bookings.save_booking(request)
        return JsonResponse(result)
    elif request.method == 'DELETE':
        result = funcs_bookings.del_booking(request)
        return JsonResponse(result)

    result = funcs_bookings.get_bookings(request.GET("id", None))
    context = {
        'result': result
    }
    return render(request, 'bookings.html', context=context)
