#this program offers a film sugestion based on a previously watched movie.
#it imports spacy to achieve this

import spacy
nlp = spacy.load('en_core_web_md')

similarities =[]

#it defines a function to complete this purpotse taking the previous movie description as a parametre.
def next_movie(previous_movie_description):

    #it first opens the movies.txt doc
    with open('movies.txt', 'r') as f:
        movies_list = f.readlines()

    test_sentence = nlp(previous_movie_description)

    #it then uses a for loop to loop through the movies and compares the description of each with the description of the previous movie
    #it then appends those similarities to the similarities list defined above
    for movie in movies_list:
        split_movie = movie.split(':')
        similarity = nlp(split_movie[1]).similarity(test_sentence)
        similarities.append(similarity)
    
    #it finds the movie number by finding the index of the highest similarity using the max() and the index() methods
    movie_num = similarities.index(max(similarities))

    #it then prints the movie that matches that index using a for loop with the enumerate function
    for pos, movie in enumerate (movies_list):
        if pos == movie_num:
            split_movie = movie.split(':')
            print (f'Based on your previous movie you should watch {split_movie[0]}. \nDescription: {split_movie[1]}')

#it runs the function with the description of the previous movie
next_movie('Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator')