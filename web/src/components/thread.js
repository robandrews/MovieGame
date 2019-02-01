'use strict';

const e = React.createElement;


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

  render() {
    const listItems = this.state.titles.map((title) =>
        <li key={title.id}>{title.movie == true ? "Movie" : "Actor"} -- {title.name}{title.year ? `, ${title.year}` : ""}</li>
    );
    return(
      <ul>{listItems}</ul>
    );
  }
}

