'use strict';

const e = React.createElement;

class Title extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <h1>The Movie Game</h1>
    );
  }
}


const domContainer = document.querySelector('#title-container');
ReactDOM.render(e(Title), domContainer);
