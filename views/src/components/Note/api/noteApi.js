import React from "react";
import axios from "axios";

import Swal from "sweetalert2";


export const deleteNote = async (noteData) => {
  Swal.fire({
    title: 'Bạn có chắc chắn?',
    text: 'Bạn không thể khôi phục lại ghi chú này!',
    icon: 'warning',
    showCancelButton: true,
    confirmButtonText: 'Xóa',
    cancelButtonText: 'Hủy',
    reverseButtons: true,
  }).then(async (result) => {
    if (result.isConfirmed) {
      try {
        const response = await axios.delete(`/api/note/${noteData.id}`);
        if (response.data.message === 'Note deleted successfully!') {
          Swal.fire('Đã xóa', 'Ghi chú đã được xóa', 'success');
          const noteElement = document.getElementById(`note-${noteData.id}`);
          if (noteElement) {
            noteElement.remove();
          }
        } else {
          Swal.fire('Lỗi', 'Có lỗi xảy ra khi xóa ghi chú.', 'error');
        }
        return response.data.message;
      } catch (error) {
        Swal.fire('Lỗi', 'Có lỗi xảy ra khi xóa ghi chú.', 'error');
      }
    }
  });
};

      
export const updateNote = async (noteData, title, content) => {
  try {
    const newPayload = { title: title, description: content };
    const response = await axios.patch(`/api/note/${noteData.id}`, newPayload);
    return response.data.data;
  } catch (error) {
    throw error;
  }
};


export const addNote = async () => {
  try {  
    const newNote = { title: "", description: "", color: getRandomColor() };
    const response = await axios.post('/api/note', newNote);
    return response.data.data;
  } catch (error) {
    throw error;
  }
};

export const getNote = async () => {
  try {
    const response = await axios.get('/api/note', { withCredentials: true, credentials: 'include' });
    return response.data.data;  
  } catch (error) {
    throw error;
  }
};

const getRandomColor = () => {
  const colors = ['#FBBF24', '#FECACA', '#BBF7D0', '#BFDBFE', '#E9D5FF', '#FBCFE8', '#B1C29E',
                  '#EBEAFF', '#E8BCB9', '#D8DBBD', '#E5D9F2', '#C8ACD6'];
  return colors[Math.floor(Math.random() * colors.length)];
};