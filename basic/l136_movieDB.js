//create an array with movie objects with properties of title, rating and has watched

var movies = [
	{title: 'Titanic',
	 rating: 5,
	 hasWatched: true},
	 {title: 'Wonder Women',
	 rating: 4.5,
	 hasWatched: false},
	 {title: 'Interstellar',
	 rating: 5,
	 hasWatched: true}
]

movies.forEach(function(movie){
	if(movie.hasWatched){
		hasWatch = "have";
	} else {
		hasWatch = "have not";
	}
	console.log("You " + hasWatch + " watched \"" + movie.title + "\" - "
				+ movie.rating + " stars" )
})