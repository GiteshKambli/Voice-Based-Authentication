import './App.css';
import {Routes, Route} from 'react-router-dom'

import SignInUp from './pages/SignInUp';
import AudioVerify from './pages/AudioVerify';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path='/' element={<SignInUp />} />
        <Route path='/audioverify' element={<AudioVerify />} />
      </Routes>
    </div>
  );
}

export default App;
