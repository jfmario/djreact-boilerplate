
import React, { Component } from 'react';
import { render } from 'react-dom';
import { HashRouter } from 'react-router-dom';

import Chatrooms from './components/Chatrooms';

class App extends Component {
  render() {
    return (
      <div class="row mh0">
        <div class="col 3 bg-info white">
          <Chatrooms />
        </div>
        <div class="col 9">
          Chat stuff here.
        </div>
      </div>
    )
  }
}

render(<App />, document.getElementById('root'));