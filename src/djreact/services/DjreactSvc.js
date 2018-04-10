
import axios from 'axios';

class DjreactService {
  
  async isAdmin() {
    var res = await axios.get('/api/is-admin');
    return res.data.is_admin;
  }
}

const DjreactSvc = new DjreactService();
export default DjreactSvc;