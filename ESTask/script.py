import json

def read_json(file_path):
    data_list = []

    with open(file_path) as json_file:
        data = json.load(json_file)

        for item in data:
            # Extract the desired values and create a dictionary or object
            # with the required properties
            extracted_data = {
                'id': item['id'],
        'reviewId': item['reviewId'],
        'reviewFullText': item['reviewFullText'],
        'reviewText': item['reviewText'],
        'numLikes': item['numLikes'],
        'numComments': item['numComments'],
        'numShares': item['numShares'],
        'rating': item['rating'],
        'reviewCreatedOn': item['reviewCreatedOn'],
        'reviewCreatedOnDate': item['reviewCreatedOnDate'],
        'reviewCreatedOnTime': item['reviewCreatedOnTime'],
        'reviewerId': item['reviewerId'],
        'reviewerUrl': item['reviewerUrl'],
        'reviewerName': item['reviewerName'],
        'reviewerEmail': item['reviewerEmail'],
        'sourceType': item['sourceType'],
        'isVerified': item['isVerified'],
        'source': item['source'],
        'sourceName': item['sourceName'],
        'sourceId': item['sourceId'],
        'tags': item['tags'],
        'href': item['href'],
        'logoHref': item['logoHref'],
        'photos': item['photos']
            }

            data_list.append(extracted_data)

    return data_list

# json_file_path = 'static/reviews.json'
# data_list = read_json_data(json_file_path)
#
# for data in data_list:
#     print(data)
