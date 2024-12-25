import React, { useState, useEffect } from 'react';
import axios from 'axios';
import StickyNote from './StickyNote';
import Header from '../Header';
import '../../static/note.css';
import { getNote, addNote } from './api/noteApi';

const Note = () => {
  const [notes, setNotes] = useState([]);


  useEffect(() => {
    getNote().then(response => {
      setNotes(response);
    })
    .catch(error => {
      throw error;
    })
  }, []);

  const addOneNote = () => {
    addNote().then(response => {
      setNotes([...notes, response[0]]);
    })
    .catch(error => {
      throw error;
    })
  };

  return (
      <main>
        <Header />
        <div className="intro">
          <div id="add-note" className="add-note" onClick={addOneNote}>+</div>
              {notes.map(note => (
              <StickyNote key={note.id}
                          noteData={note}
              />
              ))}
        </div>
      </main>
    
    
  );
};

export default Note;
