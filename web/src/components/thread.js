'use strict';

const e = React.createElement;




class MovieThread extends React.Component {
  constructor(props) {
    super(props);
    this.state = {titles: [{ "year": "1972", "name": "The Godfather", "id": "tt0068646" }]};
  }

  addTitle(title){
    var curr = this.state.titles;
    curr = curr.concat(title)
    console.log("titles: ")
    console.log(curr)
    this.setState({
        titles: curr
    });
  }

  render() {
    const listItems = this.state.titles.map((title) =>
        <li key={title.id}>{title.name}, ({title.year})</li>
    );
    return(
      <ul>{listItems}</ul>
    );
  }
}

