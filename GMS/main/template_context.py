# GYM MANAGEMENT SYSTEM BY PEACE OLORUNTOBA C.E.O. PEASCAINC
# You can contact me on gmail @ profprincepeace@gmail.com or peascainc@gmail.com
# You can also call me or whatsapp me on +2348166846226

from . import models

# Logo
def get_logo(request):
	logo=models.AppSetting.objects.first()
	data={
		'logo':logo.image_tag
	}
	return data