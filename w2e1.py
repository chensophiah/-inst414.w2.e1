sum = 0.0
count = 0.0
rating = 0.0

with open("imdb_movies_1985to2022.json", "r") as f:
    for line in f:
        this_movie = json.loads(line)
        actors = this_movie["actors"]
        for a in actors:
            if a[1] == "Hugh Jackman":
                r = this_movie["rating"]
                sum += r["avg"]
                count += 1
                
rating = sum/count
print(rating)