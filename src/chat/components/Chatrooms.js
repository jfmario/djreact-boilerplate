
import React, { Component } from 'react';

import ChatSvc from '../services/ChatSvc';

class Chatrooms extends Component {
  
  constructor(props) {
    
    super(props);
    
    this.handleAvailableChatClick = this.handleAvailableChatClick.bind(this);
    this.state = {
      publicRooms: [],
      availableRooms: [],
      privateRooms: [],
      directMessages: []
    };
  }
  
  async componentDidMount() {
    await this.refreshRooms();
  }
  
  async refreshRooms() {
    var rooms = await ChatSvc.listChats();
    this.setState({
      availableRooms: rooms.available,
      directMessages: rooms.direct,
      privateRooms: rooms.private,
      publicRooms: rooms.public
    });
  }
  
  async handleAvailableChatClick(e) {
    
    let chatId = e.target.attributes.chatid.value;
    let success = await ChatSvc.joinPublicChat(chatId);
    
    if (success) {
      this.refreshRooms();
    }
    else {
      console.log("There was an error joining that chat.");
    }
  }
  
  render() {
    return (
      <div>
        
        {!!(this.state.publicRooms.length > 0)  &&
          <div>
          
            <h5>Public Rooms</h5>
          
            <ul>
              {this.state.publicRooms.map((r, i) => (
                <li key={i}>{r.name}</li>
              ))}
            </ul>
          </div>
        }
        {!!(this.state.availableRooms.length > 0) &&
          <div>
          
            <h5>Available Public Rooms</h5>
            
            <ul>
              {this.state.availableRooms.map((r, i) => (
                <li key={i}>
                  <a
                    href="javascript:void(0);"
                    chatid={r.id}
                    onClick={this.handleAvailableChatClick}
                  >
                    {r.name}
                  </a>
                </li>
              ))}
            </ul>
          </div>
        }
      </div>
    )
  }
}

export default Chatrooms;