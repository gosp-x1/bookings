from app.models import Apartment
import json


def get_aparts(apartment_id):
    try:
        apartment = Apartment.objects.prefetch_related('bookings').get(id=apartment_id)
        data = {
            "id": apartment.id,
            "login": apartment.login,
            "city": apartment.city,
            "street": apartment.street,
            "house_number": apartment.house_number,
            "building_number": apartment.building_number,
            "apart_number": apartment.apart_number,
            "select_stuff": apartment.select_stuff,
            "select_admin": apartment.select_admin,
            "insructions": apartment.insructions,
            "bookings": []
        }
        for booking in apartment.bookings.all():
            data["bookings"].append({
                "id": booking.id,
                "start_date": booking.start_date,
                "end_date": booking.end_date,
                "booking_platform": booking.booking_platform,
                "guest_name": booking.guest_name,
                "phone": booking.phone,
                "prepayment": booking.prepayment
            })
    except Exception as e:
        data = dict()
    return data

def save_apart(request):
    try:
        data = json.loads(request.body)
        apartment_id = data.pop("apartment_id")
        Apartment.objects.update_or_create(id=apartment_id, defaults=data)
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error"}

def del_apart(request):
    try:
        data = json.loads(request.body)
        apart = Apartment.objects.get(data)
        apart.delete()
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error"}
