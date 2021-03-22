from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings


def send_verify_mail(user):
    verify_link = settings.DOMAIN_NAME + reverse('auth:verify', args=[user.id, user.activation_key])

    title = f'Подтверждение регистрации {user.email}'

    message = f'Здравствуйте, {user.first_name}, вы получили это письмо, потому что зарегистрировались на нашем сайте. Для завершения регистрации пройдите по ссылке {verify_link}'

    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
