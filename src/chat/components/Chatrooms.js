
import React, { Component } from 'react';

import axios from 'axios';

class Chatrooms extends Component {
  
  constructor(props) {
    
    super(props);
    
    this.state = {
      publicRooms: [],
      availableRooms: [],
      privateRooms: [],
      directMessages: []
    };
  }
  
  async componentDidMount() {
    
    var res = await axios.get('./api/rooms/list');
    this.setState({
      availableRooms: res.data.available,
      directMessages: res.data.direct,
      privateRooms: res.data.private,
      publicRooms: res.data.public
    });
  }
  
  render() {
    return (
      <div>
        {!!(this.state.availableRooms.length > 0) &&
          <ul>
            {this.state.availableRooms.map((r, i) => (
              <li key={i}>{r.name}</li>
            ))}
          </ul>
        }
      </div>
    )
  }
}

export default Chatrooms;