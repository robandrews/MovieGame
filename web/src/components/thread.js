'use strict';

const e = React.createElement;


function formatMovieUrl(movieId){
    return `https://www.imdb.com/title/${movieId}/`
}

function formatActorUrl(actorId){
  return `https://www.imdb.com/name/${actorId}/`
}

class MovieThread extends React.Component {
  constructor(props) {
    super(props);
    this.state = {titles: []};
  }

  addTitle(title, movie){
    var curr = this.state.titles;
    title["movie"] = movie;
    curr = curr.concat(title)
    this.setState({
        titles: curr
    });
  }

  resetThread(){
    this.setState({
        titles: []
    });
  }

  render() {
    const listItems = this.state.titles.map((title) =>
        <li key={title.id}>{title.movie == true ? "Movie" : "Actor"} -- {title.name}{title.year ? `, ${title.year}` : ""} [ <a href={title.movie == true ? self.formatMovieUrl(title.id) : self.formatActorUrl(title.id)} target="_blank" >Cheat</a> ]</li>
    );
    return(
      <ul>{listItems}</ul>
    );
  }
}

