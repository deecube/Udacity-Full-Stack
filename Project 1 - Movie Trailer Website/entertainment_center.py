# coding=utf-8
import fresh_tomatoes
import media

#following are the various movie classes

five_hundred_days_of_summer = media.Movie("500 Days of Summer", 
	"The story is based upon its male protagonist and his memories of a failed \
	relationship and has an wonderfully non linear structure", 
	"https://upload.wikimedia.org/wikipedia/en/d/d1/Five_hundred_days_of_summer.jpg",
	"https://www.youtube.com/watch?v=PsD0NpFSADM")

annie_hall = media.Movie("Annie Hall", "a 1977 American romantic comedy film \
	directed by Woody Allen from a screenplay he co-wrote with \
	Marshall Brickman. Produced by Allen's manager, Charles H. Joffe, the film \
	stars the director as Alvy \"Max\" Singer, who tries to figure \
	out the reasons for the failure of his relationship with the film's \
	eponymous female lead, played by Diane Keaton in a role written specifically for her.",
	"https://upload.wikimedia.org/wikipedia/en/e/e6/Anniehallposter.jpg", 
	"https://www.youtube.com/watch?v=TBzHphcc2Jw")

toy_story = media.Movie("Toy Story", " A story about a boy and his toys \
	that come to life", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A marine on an alien planet called Pandora",
	"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
	"https://www.youtube.com/watch?v=cRdxXPV9GNQ")

before_sunrise = media.Movie("Before Sunrise", "The film follows Jesse, a young \
	American man, and Céline, a young French woman, who meet on a train and \
	disembark in Vienna, where they spend the night walking around \
	the city and getting to know each other.", 
	"https://upload.wikimedia.org/wikipedia/en/d/da/Before_Sunrise_poster.jpg",
	"https://www.youtube.com/watch?v=9v6X-Dytlko")

dark_knight = media.Movie("The Dark Knight", "The Joker, a psychopath, \
	terrorises Gotham so he can prove that even the most incorruptible people \
	can become evil. However, Batman, Gordon and Dent stand against him.", 
	"https://images-na.ssl-images-amazon.\
	com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UY1200_\
	CR90,0,630,1200_AL_.jpg", "https://www.youtube.com/watch?v=yQ5U8suTUw0")

in_the_mood_for_love = media.Movie("In the mood for love", "Neighbours Chow and \
 Su are shocked when they learn their spouses are dating each other. Problem \
 arises when they are attracted to each other but their morals stop them from \
 expressing their love.", 
 "http://imagecache5d.allposters.com/watermarker/56-5665-773UG00Z.jpg?ch=943&cw=637", 
 "https://www.youtube.com/watch?v=BnFjSHQFVkA")

kill_bill = media.Movie("Kill Bill", "Kill Bill is an American two-part martial \
 arts film series, and the fourth film overall that was written and directed \
 by Quentin Tarantino.", "https://upload.wikimedia.org/wikipedia/en/c/cf/Kill_bill_vol_one_ver.jpg",
 "https://www.youtube.com/watch?v=ot6C1ZKyiME")

old_boy = media.Movie("Old Boy", "Dae-Su is an obnoxious drunk bailed from the \
 police station yet again by a friend. However, he's abducted from \
 the street and wakes up in a cell, where he remains for the next 15 years, \
 drugged unconscious when human contact is unavoidable, otherwise with only \
 the television as company. And then, suddenly released, he is invited to \
 track down his jailor with a denouement that is simply stunning.", 
 "http://img.moviepostershop.com/oldboy-movie-poster-2003-1020263711.jpg", 
 "https://www.youtube.com/watch?v=mNgyOueZIEo")

#add all movies to an array
movies=[five_hundred_days_of_summer, annie_hall, toy_story, avatar, 
before_sunrise, dark_knight, in_the_mood_for_love, kill_bill, old_boy]

#pass the array as an arg to the open_movies_page() function in fresh_tomato.py
fresh_tomatoes.open_movies_page(movies)
