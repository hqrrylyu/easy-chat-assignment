from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import UsernameForm


class IndexView(FormView):
    template_name = "index.html"
    form_class = UsernameForm
    success_url = reverse_lazy("chat:index")

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        self.request.session["username"] = username
        self.request.session.save()
        return super().form_valid(form)
