import './App.css';
import User_reg from './User_reg/User_reg';
import { NavLink, Route, Routes ,useLocation} from 'react-router-dom'
import Reg_users from './Reg_users/Reg_users.jsx'


function App() {
  const path=useLocation()
  const loc=path.pathname

  return (
    <div className="App">
      <nav>
      {loc==='/' && <NavLink to="/reg_users" className='display-users-button'>Registered Users</NavLink>}
      </nav>


      <Routes>
        <Route path="/" element={<User_reg />} />
        <Route path="/reg_users" element={<Reg_users />} />
      </Routes>
    </div>
  );
}

export default App;
