import React, { useState } from 'react';
import Swal from 'sweetalert2';
import axios from 'axios';

const StickyNote = ({ noteData }) => {
  const [expanded, setExpanded] = useState(false);
  const [title, setTitle] = useState(noteData.title);
  const [content, setContent] = useState(noteData.description);

  const updateNote = () => {
    const newPayload = { title, description: content };

    axios.patch(`/note/${noteData.id}`, newPayload)
      .catch(error => {
        console.error('Error updating note:', error);
      });
  };

  const deleteNote = () => {
    Swal.fire({
      title: 'Bạn có chắc chắn?',
      text: 'Bạn không thể khôi phục lại ghi chú này!',
      icon: 'warning',
      showCancelButton: true,
      confirmButtonText: 'Xóa',
      cancelButtonText: 'Hủy',
      reverseButtons: true,
    }).then((result) => {
      if (result.isConfirmed) {
        axios.delete(`/note/${noteData.id}`)
          .then(response => {
            if (response.data.message === 'deleted') {
              Swal.fire('Đã xóa', 'Ghi chú đã được xóa', 'success');
            } else {
              Swal.fire('Lỗi', 'Có lỗi xảy ra khi xóa ghi chú.', 'error');
            }
          })
          .catch(error => {
            console.error('Error deleting note:', error);
            Swal.fire('Lỗi', 'Có lỗi xảy ra khi xóa ghi chú.', 'error');
          });
      }
    });
  };

  return (
    <div
      className={`sticky-note ${expanded ? 'expanded' : ''}`}
      style={{ backgroundColor: noteData.color }}
      onClick={() => setExpanded(!expanded)}
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
      <button className="delete-btn" onClick={deleteNote}>
        <img src="static/images/cross.png" alt="Delete" style={{ width: '20px', height: '20px' }} />
      </button>
      {expanded && (
        <div className="actions">
          <button onClick={updateNote}>Cập nhật</button>
        </div>
      )}
    </div>
  );
};

export default StickyNote;
