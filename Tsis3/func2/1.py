movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
#1
def mov(name):
    for x in movies:
        if x['name'] == name:
            if float(x['imdb']) > 5.5:
                return True
            else:
                return False
print(mov('Detective'))
#2
def movv(lst):
    l = []
    for i in lst:
        if mov(i['name']):
            l.append(i['name'])
    return l


print(movv(movies))
#3
def categorry(category):
    l = []
    for i in movies:
        if i['category'] ==  category:
            l.append(i['name'])
    return l
print(categorry('Comedy'))
#4
def average(movie):
    s = 0
    for i in movie:
        s += i['imdb']

    return s/movie.__len__()

print(average(movies))

#5
def average_category(category):
    l = []
    for i in movies:
        if i['name'] in categorry(category):
            l.append(i)

    return average(l)

print(average_category('Romance'))