from django import forms


class FilterForm(forms.Form):

    def __init__(self, *args, **kwargs):
        choices_company = kwargs.pop('choices_company')
        choices_product = kwargs.pop('choices_product')
        choices_parameter = kwargs.pop('choices_parameter')
        super(FilterForm, self).__init__(*args, **kwargs)
        self.fields["Company"] = forms.MultipleChoiceField(choices=choices_company,
                                                           widget=forms.CheckboxSelectMultiple(), required=True)
        self.fields["Product"] = forms.MultipleChoiceField(choices=choices_product,
                                                           widget=forms.CheckboxSelectMultiple(), required=True)
        self.fields["Parameter"] = forms.MultipleChoiceField(choices=choices_parameter,
                                                           widget=forms.CheckboxSelectMultiple(), required=True)
