from django.shortcuts import render
from django.http.response import HttpResponse
from converter.forms import InputLengthForm, InputWeightForm, InputTempForm

# Create your views here.
def temp_unit_conversion(unit_from, unit_to, value):
    if unit_from == unit_to:
        return value
    
    to_celcius = {
        'c' : lambda x: x,
        'f' : lambda x: (x - 32) / 1.8,
        'k' : lambda x: x - 273.15
    }

    from_celcius = {
        'c' : lambda x: x,
        'f' : lambda x: (x * 1.8) + 32,
        'k' : lambda x: x + 273.15
    }
    result = None
    value_in_celcius = to_celcius[unit_from](value)
    result = from_celcius[unit_to](value_in_celcius)

    return result
 
def weight_unit_conversion(unit_from, unit_to, value):
    if unit_from == unit_to:
        return value
    
    factors = {
		'kg' : 1.0, 
		'ton'	: 1000,
		'g'	: 0.001,
		'mg'	: 0.000001,
		'pound' : 0.453592,
		'ounce' : 0.0283495,
	}
    result = None
    value_in_kg = value * factors[unit_from]
    result = value_in_kg / factors[unit_to]

    return result if result is not None else value

def length_unit_conversion(unit_from, unit_to, value):#unit conversion function
    if unit_from == unit_to:
        return value
    
    factors = {
    'km': 1.0,
    'm': 0.001,
    'cm': 0.00001,
    'mm': 0.000001,
    'inch': 0.0000254,
    'mile': 1.60934,
    'yard': 0.0009144
    }
    result = None
    value_in_km = value * factors[unit_from]
    result = value_in_km / factors[unit_to]
    
    return result if result is not None else value


#get full unit name
def full_length_unit_name(unit_to):
    unit_choice = [
        ('km', 'Kilometre'),
        ('m', 'Metre'),
        ('mm', 'Millimetre'),
        ('cm', 'Centimetre'),
        ('inch', 'Inch'),
        ('mile','Mile'),
        ('yard','Yard')
    ]
    for unit in unit_choice:
        if unit_to in unit:
            full_unit_name = unit[1]
            return full_unit_name
    return unit_to
def full_weight_unit_name(unit_to):
    unit_choice = [
        ('kg', 'Kilogram'),
        ('ton', 'Ton'),
        ('g', 'Gram'),
        ('mg', 'Milligram'),
        ('pound', 'Pound'),
        ('ounce','Ounce')
    ]
    for unit in unit_choice:
        if unit_to in unit:
            full_unit_name = unit[1]
            return full_unit_name
    return unit_to

def full_temp_unit_name(unit_to):
    unit_choice = [
        ('c', 'Celcius'),
        ('f', 'Fahrenheit'),
        ('k', 'kelvin'),
    ]
    for unit in unit_choice:
        if unit_to in unit:
            full_unit_name = unit[1]
            return full_unit_name
    return unit_to


def length(request):
    result = None
    form = InputLengthForm()
    full_unit_to = None
    
    if request.method == "POST":
        form = InputLengthForm(request.POST)
        
        if form.is_valid():
            input_value = form.cleaned_data['value']
            unit_from = form.cleaned_data['unit_from']
            unit_to = form.cleaned_data['unit_to']
            
            result = length_unit_conversion(unit_from, unit_to, input_value)
            full_unit_to = full_length_unit_name(unit_to)
                
        
        
    return render(request, 'converter/length.html', {
        'form': form, 
        'result': result, 
        'unit': full_unit_to,
        'active_menu': 'length'
    })

    

def weight(request):
    result = None
    full_unit_to = None
    form = InputWeightForm()
    if request.method == "POST":
        form = InputWeightForm(request.POST)
        
        if form.is_valid():
            input_value = form.cleaned_data['value']
            unit_from = form.cleaned_data['unit_from']
            unit_to = form.cleaned_data['unit_to']
            
            result = weight_unit_conversion(unit_from, unit_to, input_value)
            full_unit_to = full_weight_unit_name(unit_to)

    return render(request, 'converter/weight.html', {
        'form': form, 
        'result': result, 
        'unit': full_unit_to,
        'active_menu': 'weight'
    })

def temp(request):
    result = None
    full_unit_to = None
    form = InputTempForm()
    if request.method == "POST":
        form = InputTempForm(request.POST)
        
        if form.is_valid():
            input_value = form.cleaned_data['value']
            unit_from = form.cleaned_data['unit_from']
            unit_to = form.cleaned_data['unit_to']
            
            result = temp_unit_conversion(unit_from, unit_to, input_value)
            full_unit_to = full_temp_unit_name(unit_to)

    return render(request, 'converter/temperature.html', {
        'form': form, 
        'result': result, 
        'unit': full_unit_to,
        'active_menu': 'temperature'
    })