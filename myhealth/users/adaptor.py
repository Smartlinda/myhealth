from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import resolve_url, redirect

class MyAccountAdapter(DefaultAccountAdapter):
    # def save_user(self, request, user, form, commit=True):
    #     data = form.cleaned_data
    #     user.email = data.get('email')
    #     user.username = data.get('email')
    #     if 'password1' in data:
    #         user.set_password(data["password1"])
    #     else:
    #         user.set_unusable_password()
    #     self.populate_username(request, user)
    #     if commit:
    #         # Ability not to commit makes it easier to derive from
    #         # this adapter by adding
    #         user.save()
    #     return user

    def get_login_redirect_url(self, request):
        # path = super(MyAccountAdapter, self).get_login_redirect_url(request)
        current_user=request.user
        if current_user.user_type == 1:
            path='doc/dochome/'
        elif current_user.user_type == 2:
            path='lab/labhome/'
        elif current_user.user_type == 3:
            path='recep/recephome/'
        elif current_user.user_type == 4:
            path='patient/patienthome/'
        elif current_user.user_type == 5:
            path='admini/adminhome/'
        else:
            return HttpResponse("Your Rango account is disabled.")
        return path
        # .format(username=request.user.id)
