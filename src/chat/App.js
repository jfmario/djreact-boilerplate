
import React, { Component } from 'react';
import { render } from 'react-dom';
import { HashRouter } from 'react-router-dom';

import Chat from './components/Chat';
import Chatrooms from './components/Chatrooms';

class App extends Component {
  
  constructor(props) {
    
    super(props);
    
    this.handleSelectChat = this.handleSelectChat.bind(this);
    this.state = {
      chatId: null
    };
  }
  
  async handleSelectChat(chatId) {
    this.setState({
      chatId: chatId
    });
  }
  
  render() {
    return (
      <div className="row">
        <div className="col 3 bg-info white p1">
          <Chatrooms onSelectChat={this.handleSelectChat} />
        </div>
        <div className="col 9">
          <Chat chatId={this.state.chatId} />
        </div>
      </div>
    )
  }
}

render(<App />, document.getElementById('root'));