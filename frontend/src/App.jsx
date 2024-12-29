import './App.css';
import User_reg from './User_reg/User_reg';


function App() {

  const showUsers=()=>{
    console.log("users here...")
  }
  return (
    <div className="App">
      <User_reg />
      <div className='display-users-button' onClick={showUsers}>Registered Users</div>
    </div>
  );
}

export default App;
