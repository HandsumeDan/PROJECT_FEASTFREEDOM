from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order.id)
    message = 'Dear {} {},\n\nYou have successfully placed a ${} order. Your order id is {}.'.format(order.first_name,order.last_name,order.get_total_cost(),order.id)
    mail_sent = send_mail(subject, message, 'projectfeastfreedom@gmail.com', [order.email],fail_silently=False,auth_user='projectfeastfreedom@gmail.com',auth_password='3Y3un3xb')
    return mail_sent
