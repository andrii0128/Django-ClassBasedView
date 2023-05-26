from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import GeeksModel

class GeeksCreate(CreateView):

	# specify the model for create view
	model = GeeksModel

	# specify the fields to be displayed

	fields = ['title', 'description']

class GeeksList(ListView):
	model = GeeksModel

class GeeksDetailView(DetailView):
	model = GeeksModel

class GeeksUpdateView(UpdateView):
	model = GeeksModel

	fields = [
		"title",
		"description"
	]

	success_url = "/list/"

class GeeksDeleteView(DeleteView):
	model = GeeksModel

	success_url = "/list/"

