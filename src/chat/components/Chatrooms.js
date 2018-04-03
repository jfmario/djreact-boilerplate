
import React, { Component } from 'react';

import ChatSvc from '../services/ChatSvc';

/**
 * Component Chatrooms
 * function onSelectChat Function will be called with the chat id that the user selects.
 */
class Chatrooms extends Component {
  
  constructor(props) {
    
    super(props);
    
    this.handleAvailableChatClick = this.handleAvailableChatClick.bind(this);
    this.handleChatClick = this.handleChatClick.bind(this);
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
  
  async handleChatClick(e) {
    let chatId = e.target.attributes.chatid.value;
    this.props.onSelectChat(chatId);
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
                <li key={i}>
                  <a
                    href="javascript:void(0);"
                    chatid={r.id}
                    onClick={this.handleChatClick}
                  >
                    {r.name}
                  </a>
                </li>
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