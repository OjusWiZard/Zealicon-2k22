import os
import hmac
import string
import random
import hashlib
import razorpay
from .models import Order


def random_string_generator(
    size=15, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase
):
    return "".join(random.choice(chars) for _ in range(size))


def unique_order_id_generator(Klass):
    new_order_id = random_string_generator()

    qs_exists = Klass.objects.filter(order_id=new_order_id).exists()
    if qs_exists:
        return unique_order_id_generator(Klass)
    return new_order_id


client = razorpay.Client(auth=(os.environ.get("KEY_ID"), os.environ.get("KEY_SECRET")))
client.set_app_details({"title": "Zealicon 2022", "version": "22.0.0"})


def hmac_sha256(data: str, key: str):
    return hmac.new(key.encode(), data.encode(), hashlib.sha256).hexdigest()


def payment_order(user):
    receipt_id = unique_order_id_generator(Order)
    fee_amount = int(os.environ.get("FEE_AMOUNT"))
    data = {"amount": fee_amount * 100, "currency": "INR", "receipt": receipt_id}
    payment = client.order.create(data=data)
    print(payment)
    Order.objects.create(
        user=user,
        order_id=receipt_id,
        entity=payment["entity"],
        amount=str(payment["amount"]),
        amount_paid=str(payment["amount_paid"]),
        amount_due=str(payment["amount_due"]),
        currency=payment["currency"],
        receipt=payment["receipt"],
        offer_id=payment["offer_id"],
        status=payment["status"],
        attempts=str(payment["attempts"]),
    )
    return payment, receipt_id


def verify_payment(callback):
    razorpay_order_id = callback.get("razorpay_order_id")
    razorpay_payment_id = callback.get("razorpay_payment_id")
    callback_signature = callback.get("razorpay_signature")
    print("callback signature: ", callback_signature)

    generated_signature = hmac_sha256(
        razorpay_order_id + "|" + razorpay_payment_id, os.environ.get("KEY_SECRET")
    )
    print("generated signature: ", generated_signature)

    if generated_signature == callback_signature:
        payment_params = {
            "razorpay_order_id": razorpay_order_id,
            "razorpay_payment_id": razorpay_payment_id,
            "razorpay_signature": callback_signature,
        }
        client.utility.verify_payment_signature(payment_params)
        return True
    else:
        return False
