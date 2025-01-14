import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [aliens, setAliens] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/aliens/')
      .then(response => {
        setAliens(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  return (
    <div>
      {}
    </div>
  );
}

export default App;