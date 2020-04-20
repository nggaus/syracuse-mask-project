from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from mask_project.forms import DonationRequestForm


class RequestDonationsView(TemplateView):
    template_name = "request-donations-form.html"
    form_class = DonationRequestForm
    success_url = 'request-donations-thanks'

    def get_context_data(self, **kwargs):
        context = super(RequestDonationsView, self).get_context_data(**kwargs)
        context['page_title'] = "Request Donations"
        context['extra_css'] = []
        context['extra_javascript'] = []

        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['form'] = self.form_class()

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['form'] = self.form_class(request.POST)

        if context['form'].is_valid():
            context['form'].save()

            return redirect(self.success_url)

        return render(request, self.template_name, context)


class RequestDonationsThanksView(TemplateView):
    template_name = "request-donations-thanks.html"

    def get_context_data(self, **kwargs):
        context = super(RequestDonationsThanksView, self).get_context_data(**kwargs)
        context['page_title'] = "Request Received, Thank You"
        context['extra_css'] = []
        context['extra_javascript'] = []

        return context
