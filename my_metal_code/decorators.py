from django.forms import BaseModelForm


def show_errors(view_method):
    """
    decorator function to be used with a view class like CreateView or EditView
    note: the view class must have a post method defind
    """
    def decorator(self, request, *args, **kwargs):
        form = self.get_form()
        if not form.is_valid():
            for field_name, errors in form.errors.items():
                for error_message in errors:
                    print(f"Error for field '{field_name}': {error_message}")
        return view_method(self, request, *args, **kwargs)
    return decorator


def handle_img_from_form(view_method):
    """
    decorator function to handle the storate og the image loaded in a form
    note: remember to name the field "img" to proceed properly
    """
    def decorator(self, form: BaseModelForm, *args, **kwargs):
        instance = form.save(commit=False)
        if "img" in self.request.FILES:
            instance.img = self.request.FILES["img"]
            instance.save()
            return view_method(self, form, *args, **kwargs)
        else:
            raise AttributeError("The 'img' field is missing in the form.")
    return decorator
