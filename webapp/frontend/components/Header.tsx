import React from 'react';
import Link from 'next/link';

const Header: React.FC = () => {
    return (
        <header>
            <nav>
                <Link href="/">
                    <a>Home</a>
                </Link>
                <Link href="/login">
                    <a>Login</a>
                </Link>
                <Link href="/register">
                    <a>Register</a>
                </Link>
            </nav>
        </header>
    );
};

export default Header;