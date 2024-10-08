import { useState } from 'react';
import logo from './logo.svg';
import './App.css';
import WordViewer from './WordViewer.jsx';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Word Document Viewer</h1>
        {/* Use the WordViewer component */}
        <WordViewer />
      </header>
    </div>
  );
}

export default App
