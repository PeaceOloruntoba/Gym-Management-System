# GYM MANAGEMENT SYSTEM BY PEACE OLORUNTOBA C.E.O. PEASCAINC
# You can contact me on gmail @ profprincepeace@gmail.com or peascainc@gmail.com
# You can also call me or whatsapp me on +2348166846226

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class NotificationConsumer(WebsocketConsumer):
	# Connect
	def connect(self):
		self.group_name='noti_group_name'
		async_to_sync(self.channel_layer.group_add)(
			self.group_name, self.channel_name
		)
		self.accept()

	# Recieve Notification
	def receive(self,text_data):
		self.send(text_data="This is from server")

	# Disconnect
	def disconnect(self,close_code):
		self.close(close_code)

	# Send Notification
	def send_notification(self,event):
		self.send(event.get('value'))