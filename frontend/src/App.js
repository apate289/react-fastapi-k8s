import React, { useEffect, useState } from 'react';

export default function App() {
  const [items, setItems] = useState([]);
  const [name, setName] = useState('');

  useEffect(() => {
    fetch('/api/items').then(r => r.json()).then(setItems);
  }, []);

  async function add() {
    if (!name) return;
    const res = await fetch('/api/items', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({name, description: 'Created via UI'})
    });
    const j = await res.json();
    setItems(prev => [...prev, j]);
    setName('');
  }

  return (
    <div style={{padding:20}}>
      <h1>React + FastAPI Demo</h1>
      <div>
        <input value={name} onChange={e=>setName(e.target.value)} placeholder="Item name"/>
        <button onClick={add}>Add</button>
      </div>
      <ul>
        {items.map(it => <li key={it.id}>{it.id}: {it.name}</li>)}
      </ul>
    </div>
  );
}
