import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <iframe src="http://localhost:3000/d-solo/e4808398-51ac-4e6a-965b-cc7a99ad42f1/iot-smarthome?orgId=1&panelId=3" width="450" height="200" frameBorder="0"></iframe>
      </header>
    </div>
  );
}

export default App;
