import React from 'react';
import Head from 'next/head';
import { Header } from '../components/Header';
import { Footer } from '../components/Footer';

const Home: React.FC = () => {
  return (
    <div>
      <Head>
        <title>Home</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <Header />

      <main>
        <h1>Welcome to our Web App</h1>
        <p>This is a modern, performant web application using the Next.js framework for the frontend and Django for the backend.</p>
      </main>

      <Footer />
    </div>
  )
}

export default Home;