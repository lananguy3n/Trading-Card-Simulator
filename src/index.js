import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import './style.css';

/*const Header = () => {
  const myStyle = {
      color: rgb(255, 255, 255),
      width: 779px,
      height: 168px,
      font-size: 94px,
      font-style: normal,
      font-weight: 900,
      border-color: #ffffff,
      border-width: 12px,
      margin-bottom: var(--dl-space-space-fourunits),
      text-transform: uppercase
  };
} */

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
