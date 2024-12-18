import React from 'react';
import Buttons from './Button';
import ImageGallery from './ImageGallery';

const Intro = () => {
    return (
        <main>
            <div className="intro">
                <div className="content">
                    <h1>Welcome to my app!!!</h1>
                    <p>
                        <b>Ứng dụng ghi chú</b>. Miễn phí, đơn giản và trực quan. <b>Không cần đăng nhập.</b>
                    </p>
                    <Buttons />
                    <ImageGallery />
                </div>
            </div>
        </main>
    );
};

export default Intro;
