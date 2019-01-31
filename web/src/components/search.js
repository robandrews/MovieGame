'use strict';


const e = React.createElement;

class MovieSearch extends React.Component {
  constructor(props) {
    super(props);
    this.state = {name: ""}
  }

  // changeInput(event){
  //   console.log("changeinput")
  //   this.setState({name: event.target.value})
  // }

  // clearInput(){
  //   this.setState({name: ""})
  // }

  render() {
    return(
      <form role="form">
          <div className="form-group">
            <input className="form-control" id="titles_search" type="text" placeholder="Enter a movie" />
          </div>
      </form>
    );
  }
}

ReactDOM.render(e(MovieSearch), document.querySelector('#search-container'));