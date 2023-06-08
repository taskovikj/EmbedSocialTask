from django.db import models

# Create your models here.

class Review:
    def __init__(self, id, reviewId, reviewFullText, reviewText, numLikes, numComments, numShares, rating,
                 reviewCreatedOn, reviewCreatedOnDate, reviewCreatedOnTime, reviewerId, reviewerUrl, reviewerName,
                 reviewerEmail, sourceType, isVerified, source, sourceName, sourceId, tags, href, logoHref, photos):
        self.id = id
        self.reviewId = reviewId
        self.reviewFullText = reviewFullText
        self.reviewText = reviewText
        self.numLikes = numLikes
        self.numComments = numComments
        self.numShares = numShares
        self.rating = rating
        self.reviewCreatedOn = reviewCreatedOn
        self.reviewCreatedOnDate = reviewCreatedOnDate
        self.reviewCreatedOnTime = reviewCreatedOnTime
        self.reviewerId = reviewerId
        self.reviewerUrl = reviewerUrl
        self.reviewerName = reviewerName
        self.reviewerEmail = reviewerEmail
        self.sourceType = sourceType
        self.isVerified = isVerified
        self.source = source
        self.sourceName = sourceName
        self.sourceId = sourceId
        self.tags = tags
        self.href = href
        self.logoHref = logoHref
        self.photos = photos

    def __str__(self):
        return self.reviewFullText

