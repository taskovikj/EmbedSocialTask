import json
from django.shortcuts import render
from .script import read_json_data

def index(request):
    # Read the JSON data

    reviews = read_json_data('ESTask/static/reviews.json')

    prioritize_text = request.GET.get('prioritize_text', 'no')
    order_by_rating = request.GET.get('order_by_rating', 'highest')
    order_by_date = request.GET.get('order_by_date', 'oldest')
    minimum_rating = int(request.GET.get('minimum_rating', 1))

    # Filter the reviews based on the minimum rating
    filtered_reviews = [review for review in reviews if review['rating'] >= minimum_rating]

    # Sort the reviews based on the selected options
    if prioritize_text == 'yes':
        text_reviews = [review for review in filtered_reviews if review['reviewText']]
        non_text_reviews = [review for review in filtered_reviews if not review['reviewText']]

        text_reviews = sorted(text_reviews, key=lambda r: r['rating'], reverse=order_by_rating == 'highest')
        non_text_reviews = sorted(non_text_reviews, key=lambda r: r['rating'], reverse=order_by_rating == 'highest')

        if order_by_date == 'oldest':
            text_reviews = sorted(text_reviews, key=lambda r: r['reviewCreatedOnTime'])
            non_text_reviews = sorted(non_text_reviews, key=lambda r: r['reviewCreatedOnTime'])
        else:
            text_reviews = sorted(text_reviews, key=lambda r: r['reviewCreatedOnTime'], reverse=True)
            non_text_reviews = sorted(non_text_reviews, key=lambda r: r['reviewCreatedOnTime'], reverse=True)

        sorted_reviews = text_reviews + non_text_reviews
    else:
        sorted_reviews = sorted(filtered_reviews, key=lambda r: r['rating'], reverse=order_by_rating == 'highest')

        if order_by_date == 'oldest':
            sorted_reviews = sorted(sorted_reviews, key=lambda r: r['reviewCreatedOnTime'])
        else:
            sorted_reviews = sorted(sorted_reviews, key=lambda r: r['reviewCreatedOnTime'], reverse=True)

    context = {
        'reviews': sorted_reviews
    }

    return render(request, 'ESTask/index.html', context)
