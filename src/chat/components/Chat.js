
import React, { Component } from 'react';

import ChatSvc from '../services/ChatSvc';

class Chat extends Component {
  
  constructor(props) {
    
    super(props);
    
    // console.log("Chat Constructor called.");
    
    this.handleUserMessage = this.handleUserMessage.bind(this);
    this.sendChat = this.sendChat.bind(this);
    this.updateChats = this.updateChats.bind(this);
    this.state = {
      chatDescription: '',
      chatId: props.chatId,
      chatName: '',
      messages: [],
      userMessage: ''
    };
  }
  
  async componentDidMount() {
    await this.updateChats(this.props.chatId);
    setInterval(this.updateChats, 5000);
  }
  
  async componentWillReceiveProps(props) {
    if (props.chatId != this.state.chatId) {
      this.setState({ messages: [], chatId: props.chatId });
      await this.updateChats(props.chatId);
    }
  }
  
  async updateChats(chatId) {
    if (!this.state.chatId && !chatId) return;
    // console.log(this.state.chatName);
    if (!chatId) chatId = this.state.chatId;
    let data = await ChatSvc.getRecentMessages(chatId);
    let messages = this.state.messages;
    this.setState({
      chatDescription: data.description,
      chatName: data.chatroom,
      messages: [].concat(data.messages)
    });
  }
  
  async sendChat(e) {
    
    e.preventDefault();

    await ChatSvc.sendMessage(this.state.chatId, this.state.userMessage);
    this.setState({ userMessage: '' });
    this.updateChats();
  }
  
  async handleUserMessage(e) {
    this.setState({
      userMessage: e.target.value
    });
  }
  
  render() {
    return (
      <div>
      
        <p>
          <b># {this.state.chatName}</b>
        </p>
        
        {!!(this.state.messages.length > 0) &&
          <p>
            <a href="javascript:void(0);">Members</a>
            &nbsp;|
            &nbsp;{this.state.chatDescription}
          </p>
        }
        
        <hr />
        
        <div>
          {!!(this.state.messages.length > 0) &&
            <div style={{ height: "400px", overflow: 'scroll' }}>
              {this.state.messages.map((m, i) => (
                <div key={i}>
                  <p>
                    
                    {!!(m.user_image) &&
                      <img className="m1" style={{ height: '20px', width: '20px', float: 'left' }} src={m.user_image} />
                    }
                    
                    <b>{m.user}</b>
                    
                    <br />
                    
                    {m.text}
                  </p>
                </div>
              ))}
            </div>
          }
          {!!(this.state.messages.length == 0 && !!this.state.chatName) &&
            <p><i>There are no messages yet.</i></p>
          }
        </div>
        
        {!!(this.state.chatName) &&
          <form onSubmit={this.sendChat} className="row">
            <input className="card w-100" placeholder="Enter chat message" value={this.state.userMessage} onChange={this.handleUserMessage} />
            <button className="btn bg-success b-success white w-100">Send</button>
          </form>
        }
      </div>
    );
  }
}

export default Chat;