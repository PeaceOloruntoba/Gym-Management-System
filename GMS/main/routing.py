# GYM MANAGEMENT SYSTEM BY PEACE OLORUNTOBA C.E.O. PEASCAINC
# You can contact me on gmail @ profprincepeace@gmail.com or peascainc@gmail.com
# You can also call me or whatsapp me on +2348166846226

from django.urls import path
from .consumers import NotificationConsumer

# Route
ws_patterns=[
	path('ws/notifications/',NotificationConsumer.as_asgi()),
]