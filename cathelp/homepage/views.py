from django.views.generic import ListView


class Homepage(ListView):
    template_name = "homepage/homepage.html"

    # dynamic context
    def get_context_data(self, *, object_list=None, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context["name"] = name
        # return context
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        pass
