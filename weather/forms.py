from django import forms 

class WeatherForm(forms.Form):
    CHOICES =[
        ('Arusha','Arusha'),
        ('Dar es Salaam','Dar es Salaam'),
        ('Dodoma','Dodoma'),
        ('Iringa','Iringa'),
        ('Kagera','Kagera'),
        ('Kigoma','Kigoma'),
        ('Kilimanjaro','Kilimanjaro'),
        ('Lindi','Lindi'),
        ('Manyara','Manyara'),
        ('Mara','Mara'),
        ('Mbeya','Mbeya'),
        ('Morogoro','Morogoro'),
        ('Mtwara','Mtwara'),
        ('Mwanza','Mwanza'),
        ('Pemba','Pemba'),
        ('Pwani','Pwani'),
        ('Rukwa','Rukwa'),
        ('Ruvuma','Ruvuma'),
        ('Shinyanga','Shinyanga'),
        ('Singida','Singida'),
        ('Tabora','Tabora'),
        ('Tanga','Tanga'),
        ('Zanzibar','Zanzibar')
    ]

    Location = forms.ChoiceField(choices=CHOICES)