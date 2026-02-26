from django import forms



class InputLengthForm(forms.Form):
    
    value = forms.FloatField(
    required=True,
    label="Value to convert",
    initial=0.0,
    help_text="type value you want to convert (ie. 10.5)"
)
    unit_choice = [
        ('km', 'Kilometre'),
        ('m', 'Metre'),
        ('mm', 'Millimetre'),
        ('cm', 'Centimetre'),
        ('inch', 'Inch'),
        ('mile','Mile'),
        ('yard','Yard')
    ]
    unit_from = forms.ChoiceField(
        choices=unit_choice,
        label="unit to convert from",
        widget=forms.RadioSelect
    )
    unit_to = forms.ChoiceField(
        choices=unit_choice,
        label="unit to convert to",
        widget=forms.RadioSelect
    )

class InputWeightForm(forms.Form):
    
    value = forms.FloatField(
    required=True,
    label="Value to convert",
    initial=0.0,
    help_text="type value you want to convert (ie. 10.5)"
)
    unit_choice = [
        ('kg', 'Kilogram'),
        ('ton', 'Ton'),
        ('g', 'Gram'),
        ('mg', 'Milligram'),
        ('pound', 'Pound'),
        ('ounce','Ounce')
    ]
    unit_from = forms.ChoiceField(
        choices=unit_choice,
        label="unit to convert from",
        widget=forms.RadioSelect
    )
    unit_to = forms.ChoiceField(
        choices=unit_choice,
        label="unit to convert to",
        widget=forms.RadioSelect
    )

class InputTempForm(forms.Form):
    
    value = forms.FloatField(
    required=True,
    label="Value to convert",
    initial=0.0,
    help_text="type value you want to convert (ie. 10.5)"
)
    unit_choice = [
        ('c', 'Celcius'),
        ('f', 'Fahrenheit'),
        ('k', 'kelvin'),
    ]
    unit_from = forms.ChoiceField(
        choices=unit_choice,
        label="unit to convert from",
        widget=forms.RadioSelect
    )
    unit_to = forms.ChoiceField(
        choices=unit_choice,
        label="unit to convert to",
        widget=forms.RadioSelect
    )
    