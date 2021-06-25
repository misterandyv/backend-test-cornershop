# User model
from orders.models import Order

# Django
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# celery logger and task
from backend_test.celery import app
from celery.utils.log import get_task_logger

# Logger celery
logger = get_task_logger(__name__)


@app.task(name="confirm_order_email")
def confirm_order_email(order_pk):
    """ Task for send email confirm order """
    order = Order.objects.get(pk=order_pk)
    subject = 'Hi @{}! Your order has been confirmed'.format(
        order.user.username)
    from_email = 'Internal CornerShop <test-cornershop@cornershop.com>'
    content = render_to_string(
        'email/confirm_order.html',
        {'order': order}
    )
    msg = EmailMultiAlternatives(
        subject, content, from_email, [order.user.email])
    print(msg)
    msg.attach_alternative(content, "text/html")
    msg.send()
