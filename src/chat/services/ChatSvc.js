
import axios from 'axios';
import moment from 'moment';

class ChatService {
  
  // adds a user to a chat and return true if successful, false otherwise
  async addUserToChat(userId, chatId) {
    var res = axios.post(`/chat/api/room/${chatId}/add-user/${userId}`);
    if (res.data.success) return true;
    else return false;
  }
  
  // creates a new chat room and returns the chat id or null
  async createChatroom(name, isPublic) {
    
    var data = { name: name };
    if (isPublic) data.publicity = 'public';
    else data.publicity = 'private';
    var res = await axios.post(`/chat/api/create/room`, data);
    
    if (res.status == 200) {
      return res.data.id;
    }
    else {
      return null;
    }
  }
  
  // creates a direct message with the other user and returns the chat id
  async createDirectMessage(userId) {
    var res = await axios.post(`/chat/api/create/direct-message/${userId}`);
    return res.data.id;
  }
  
  // gets recent messages from a chat
  async getRecentMessages(chatId) {
    var res = await axios.post(`/chat/api/room/${chatId}/messages`);
    return res.data;
  }
  
  // joins a public chatroom and returns true if successful
  async joinPublicChat(chatId) {
    var res = await axios.post(`/chat/api/room/${chatId}/join`);
    if (res.status == 200) return true;
    else return false;
  }
  
  // lists chatrooms
  async listChats() {
    var res = await axios.post(`/chat/api/rooms/list`);
    // console.log(res);
    return res.data;
  }
  
  // disconnects from a chat
  async leaveChat(chatId) {
    var res = await axios.post(`/chat/api/room/${chatId}/leave`);
  }
  
  // sends a message to a chat and returns true if successful
  async sendMessage(chatId, message) {
    
    var data = { message: message };
    var res = await axios.post(`/chat/api/room/${chatId}/send-message`, data);
    
    if (res.data.success) return true;
    else return false;
  }
}

const ChatSvc = new ChatService();
export default ChatSvc;