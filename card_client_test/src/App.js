import logo from './logo.svg';
import './App.css';

function sayHello() {
  fetch("http://localhost:3001/open", {
    method: "POST",
    body: JSON.stringify({
      pack: 0
    }),
    headers: {
      "Content-type": "appliscation/json; charset=UTF-8"
    }
  });
}

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
          href="http://localhost:3001/open"
          target="_blank"
          rel="noopener noreferrer"
        >
          Open cards
        </a>
        <button onClick={sayHello}>Default</button>
      </header>
    </div>
  );
}

export default App;
