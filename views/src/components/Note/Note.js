import React, { useState, useEffect } from 'react';
import axios from 'axios';
import StickyNote from './StickyNote';

const Note = () => {
  const [notes, setNotes] = useState([false]);

  useEffect(() => {
    // Lấy dữ liệu ghi chú từ server khi component mount
    axios.get('http://127.0.0.1:5000/api/note', { withCredentials: true })
      .then(response => {
        setNotes(response.data);
        console.log(response);
      })
      .catch(error => {
        console.error('Error fetching notes:', error);
      });
  }, []);

  const addNote = () => {
    const newNote = { title: "", description: "", color: getRandomColor() };

    axios.post('http://127.0.0.1:5000/api/note', newNote)
      .then(response => {
        setNotes([...notes, response.data]);
      })
      .catch(error => {
        console.error('Error adding note:', error);
      });
  };

  const getRandomColor = () => {
    const colors = ['#FBBF24', '#FECACA', '#BBF7D0', '#BFDBFE', '#E9D5FF'];
    return colors[Math.floor(Math.random() * colors.length)];
  };

  return (
    <div className="intro">
      <div id="add-note" className="add-note" onClick={addNote}>+</div>
      <div className="notes-list">
        {/* {notes.map(note => (
          <StickyNote key={note.id} noteData={note} />
        ))} */}
      </div>
    </div>
  );
};

export default Note;
