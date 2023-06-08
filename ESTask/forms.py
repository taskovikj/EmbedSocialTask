from django import forms

class ReviewSortForm(forms.Form):
    RATING_CHOICES = [
        ('highest', 'Highest First'),
        ('lowest', 'Lowest First'),
    ]
    DATE_CHOICES = [
        ('oldest', 'Oldest First'),
        ('newest', 'Newest First'),
    ]

    prioritize_text = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')])
    order_by_rating = forms.ChoiceField(choices=RATING_CHOICES)
    order_by_date = forms.ChoiceField(choices=DATE_CHOICES)
    minimum_rating = forms.ChoiceField(choices=[(str(i), str(i)) for i in range(1, 6)])
