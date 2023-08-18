# Django
from django.conf import settings
from django.core.mail import EmailMessage


def send_email(
    subject: str,
    body: str,
    to_emails: list[str]
) -> None:
    email = EmailMessage(
        subject,
        body,
        settings.EMAIL_FROM,
        to_emails
    )
    email.send()


def normalize_time(duration: int) -> str:
    SECONDS_PER_MINUTE: int = 60
    minutes, seconds = divmod(
        duration,
        SECONDS_PER_MINUTE
    )
    return f'{int(minutes)} мин {int(seconds)} сек'
