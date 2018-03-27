
import React, { Component } from 'react';

import ChatSvc from '../services/ChatSvc';

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
    var rooms = await ChatSvc.listChats();
    console.log(rooms);
    this.setState({
      availableRooms: rooms.available,
      directMessages: rooms.direct,
      privateRooms: rooms.private,
      publicRooms: rooms.public
    });
  }
  
  render() {
    return (
      <div>
        
        {!!(this.state.publicRooms.length > 0)  &&
          
          <h3>Public Rooms</h3>
        }
        {!!(this.state.availableRooms.length > 0) &&
          <div>
            <h3>Available Public Rooms</h3>
            <ul>
              {this.state.availableRooms.map((r, i) => (
                <li key={i}>{r.name}</li>
              ))}
            </ul>
          </div>
        }
      </div>
    )
  }
}

export default Chatrooms;