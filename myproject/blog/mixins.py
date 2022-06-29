from django.shortcuts import redirect
from .models import Article, Author

class FieldsMixin():
	def dispatch(self, request, *args, **kwargs):
		self.fields = [
				"title","slug","category","description",
				"image","published","is_special","status",
			]
		if request.user.is_superuser:
			self.fields.append("author")
		return super().dispatch(request, *args, **kwargs)


class AuthorsAccessMixin():
	authors = Author.objects.all()
	authors_list = [item.user for item in authors]
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			if request.user in self.authors_list:
				return super().dispatch(request, *args, **kwargs)
			else:
				return redirect("dashboard:dashboard-page")
		else:
			return redirect("dashboard:login")