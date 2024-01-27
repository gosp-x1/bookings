from app.models import Booking, Apartment
import json


def get_bookings(booking_id):
    try:
        booking = Booking.objects.get(id=booking_id)
        data = {
            "id": booking.id,
            "start_date": booking.start_date,
            "end_date": booking.end_date,
            "apartment": booking.apartment.id,
            "booking_platform": booking.booking_platform,
            "guest_name": booking.guest_name,
            "phone": booking.phone,
            "prepayment": booking.prepayment,
        }
    except Exception as e:
        data = dict()
    return data

def save_booking(request):
    try:
        data = json.loads(request.body)
        apartment_id = data.pop('apartment_id', None)
        apartment = Apartment.objects.get(id=apartment_id)
        Booking.objects.update_or_create(apartment=apartment, defaults=data)
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error"}

def del_booking(request):
    try:
        data = json.loads(request.body)
        booking = Booking.objects.get(data)
        booking.delete()
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error"}
