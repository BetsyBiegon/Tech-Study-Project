import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Layout/Navbar';
import Footer from './components/Layout/Footer';
import Login from './components/Auth/Login';
import Register from './components/Auth/Register';
import ContentList from './components/Content/ContentList';
import ContentDetail from './components/Content/ContentDetail';

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/contents" element={<ContentList />} />
        <Route path="/contents/:id" element={<ContentDetail />} />
      </Routes>
      <Footer />
    </Router>
  );
}

export default App;
