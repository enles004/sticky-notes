import React from 'react';

const Header = () => {
    return (
        <header>
            <div className="logo">NotesApp</div>
            <div className="icons">
                <a href="https://github.com/enles004"><i className="fab fa-github" style={{ fontSize: '30px' }}></i></a>
                <a href="https://www.facebook.com/loo3enles/"><i className="fab fa-facebook" style={{ fontSize: '30px' }}></i></a>
                <a href="https://www.linkedin.com/in/phuocc-le-0a8814281/"><i className="fab fa-linkedin" style={{ fontSize: '30px' }}></i></a>
            </div>
        </header>
    );
};

export default Header;
