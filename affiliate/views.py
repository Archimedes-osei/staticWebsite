from django.shortcuts import render
from django.core.mail import send_mail
# from rest_framework import viewsets
# from .models import Service
# from .serializers import ServiceSerializer

# class ServiceView(viewsets.ModelViewSet):
# 	queryset = Service.objects.all().order_by('name')
# 	serializer_class = ServiceSerializer

def home(request):
	return render(request, 'home.html', {})
	
def home(request):
	return render(request, 'home.html', {})

def contact(request):
	return render(request, 'contact.html', {})


# def contact(request):
# 	if request.method == "POST":
# 		message_name = request.POST['message-name']
# 		message_email = request.POST['message-email']
# 		message = request.POST['message']


# 		# send an email
# 		send_mail(
# 			message_name, # subject
# 			message, # message
# 			message_email, # from Email
# 			['lordosei070@gmail.com'], # to email

# 			)


# 		return render(request, 'contact.html', {'message_name'})

# 	else:
# 		return render(request, 'contact.html', {})

# def form_invalid(self, form, **kwargs):
#     ctx = self.get_context_data(**kwargs)
#     random_int = random.randint(0,20)
#     form.data = form.data.copy()       #<--- make a copy
#     form.data['quantity'] = random_int #<--- assign value-->
#     ctx['form'] = form
#     return self.render_to_response(ctx)