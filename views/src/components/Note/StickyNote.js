import React, { useState, useEffect, useRef } from 'react';
import { deleteNote } from './api/noteApi';
import { updateNote } from './api/noteApi';


const StickyNote = ({ noteData }) => {
  const [expanded, setExpanded] = useState(false);
  const [title, setTitle] = useState(noteData.title);
  const [content, setContent] = useState(noteData.description);
  const color = noteData.color;
  

  const handleClickOutside = (event) => {
    if (expanded) {
      updateNote(noteData, title, content);
      setExpanded(false);
    }
  };

  useEffect(() => {
    document.addEventListener('click', handleClickOutside);
    return () => {
      document.removeEventListener('click', handleClickOutside);
    };
  }, [expanded, title, content]);

  return (
    <div
      id={`note-${noteData.id}`}
      className={`sticky-note ${expanded ? 'expanded' : ''}`}
      style={{ backgroundColor: color }}
      onClick={(e) => {
        if(!expanded){
          document.querySelectorAll('.sticky-note').forEach(n => n.classList.remove('expanded'));
        }
        setExpanded(true);
        e.stopPropagation();
      }}
    >
      <input
        type="text"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        placeholder="Tiêu đề..."
        className="title"
      />
      <textarea
        value={content}
        onChange={(e) => setContent(e.target.value)}
        placeholder="Nội dung..."
        className="content"
      />
      <button className="delete-btn" onClick={(e) => {
                                                e.stopPropagation();
                                                deleteNote(noteData);
                                              }}>
        <img src="../../static/images/cross.png" alt="Delete" style={{ width: '20px', height: '20px' }} />
      </button>
    </div>
  );
};

export default StickyNote;
