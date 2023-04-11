from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import UpdateView

from accounts.forms import UserChangeForm, ProfileChangeForm


class UserChangeView(UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'partial/partial_user_change.html'
    context_object_name = 'user_obj'
    data = dict()

    def get_context_data(self, **kwargs):
        if 'profile_form' not in kwargs:
            kwargs['profile_form'] = self.get_profile_form()
        return super().get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        data = self.data
        data['html_forms'] = render_to_string(self.template_name, self.get_context_data(), request=request)
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        profile_form = self.get_profile_form()
        if form.is_valid() and profile_form.is_valid():
            return self.form_valid(form, profile_form, request)
        else:
            return self.form_invalid(form, profile_form, request)

    def form_valid(self, form, profile_form, request):
        self.object = form.save()
        profile_form.save()
        data = self.data
        data['forms_are_valid'] = True
        user_obj = self.object
        data['html_general_profile_info'] = render_to_string("partial/partial_general_profile_info.html", {"user_obj": user_obj})
        return JsonResponse(data)

    def form_invalid(self, form, profile_form, request):
        data = self.data
        data['forms_are_valid'] = False
        context = self.get_context_data(form=form, profile_form=profile_form)
        data['html_forms'] = render_to_string(self.template_name, context, request=request)
        return JsonResponse(data)

    def get_profile_form(self):
        form_kwargs = {'instance': self.object.profile}
        if self.request.method == 'POST':
            form_kwargs['data'] = self.request.POST
            form_kwargs['files'] = self.request.FILES
            print(form_kwargs)
        print(form_kwargs)
        print(self.object.profile.avatar)
        return ProfileChangeForm(**form_kwargs)
