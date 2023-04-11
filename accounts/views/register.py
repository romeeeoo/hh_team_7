from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from accounts.forms import SignUpForm


class RegisterView(CreateView):
    template_name = "register.html"
    form_class = SignUpForm
    success_url = "/admin"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        print(form.is_bound)
        if form.is_valid():
            user = form.save()
            # user.refresh_from_db()
            user.profile.phone_number = form.cleaned_data.get("phone_number")
            user.profile.is_corporate = form.cleaned_data.get("is_corporate")
            user.profile.avatar = form.cleaned_data.get("avatar")
            user.profile.save()
            login(request, user)
            return redirect("index")
        context = dict()
        print(context)
        context["form"] = form
        print(form.fields)
        print(form)
        print(context)
        return self.render_to_response(context)