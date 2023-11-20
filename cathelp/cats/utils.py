import cats.models


# dynamic content
class ListCatMixin:
    def get_user_data(self, **kwargs):
        context = self.kwargs
        if "color_slug" not in context:
            context["color_selected"] = ""
        context["colors"] = cats.models.Color.objects.all()
        return context
