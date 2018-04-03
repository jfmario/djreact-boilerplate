
import React, { Component } from 'react';

class Chat extends Component {
  
  constructor(props) {
    
    super(props);
    
    this.state = {
      chatId: props.chatId
    };
  }
  
  async componentWillReceiveProps(props) {
    if (props.chatId != this.state.chatId) {
      this.setState({ chatId: props.chatId });
    }
  }
  
  render() {
    return (
      <p>Chat stuff here for {this.state.chatId}.</p>
    )
  }
}

export default Chat;