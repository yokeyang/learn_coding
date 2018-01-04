# -*- coding:utf-8 -*-
import json
import math


class commend:
    def __init__(self):
        f = open('../public/movies.json',encoding='utf-8')
        self.data = json.load(f)
    def setup(self):
        titles = self.data['titles']
        star = {}
        for title in titles:
            print(title)
            star[title] = input("please input the %s's rating"%title)
            if star[title] == '':
                star[title] = None
        self.findNearestNeighbors(star)

    def findNearestNeighbors(self, user):
        similarityScores = {}
        for other in self.data['users']:
            similarity = self.euclideanDistance(user, other)
            similarityScores[other['name']] = similarity

        self.data['users'] = sorted(
            self.data['users'], key=lambda i: i['name'], reverse=True)
        for title in self.data['titles']:
            if (user[title] == None):
                k = 5
                weightedSum = 0
                similaritySum = 0
                for j in range(k):
                    name = self.data['users'][j]['name']
                    sim = similarityScores[name]
                    ratings = self.data['users'][j]
                    rating = ratings[title]
                    if(rating != None):
                        weightedSum += rating * sim
                        similaritySum += sim
                print(weightedSum,similaritySum,weightedSum/similaritySum)


    def euclideanDistance(self,ratings1,ratings2):
        titles = self.data['titles']
        sumSquares = 0
        for title in titles:
            rating1 = ratings1[title]
            rating2 = ratings2[title]
            if (rating1 != None and rating2 != None):
                diff = int(rating1) - int(rating2)
                sumSquares += diff * diff

        similarity = 1 / (1 + math.sqrt(sumSquares))
        return similarity


c = commend()
c.setup()