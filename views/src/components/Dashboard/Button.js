import React, {useState} from 'react';
import { useNavigate } from "react-router-dom";

const Buttons = () => {
    const navigate = useNavigate();  // Khai báo hook useNavigate

    const handleRedirect = async (event) => {
        event.preventDefault();  
        navigate("/note");  
    };

    return (
        <div className="buttons">
            <form action="#" method="get">
                <button className="learn-more"><b>Chi tiết hơn</b></button>
            </form>
            <form onSubmit={handleRedirect}>
                <button className="try-now"><b>Trải nghiệm ngay ►</b></button>
            </form>
        </div>
    );
};

export default Buttons;
