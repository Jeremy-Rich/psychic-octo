import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './pages/HomePage';
import StoriesPage from './pages/StoriesPage';
import SubmitStoryPage from './pages/SubmitStoryPage';
import AboutUsPage from './pages/AboutUsPage';
import ResourcesPage from './pages/ResourcesPage';
import ContactUsPage from './pages/ContactUsPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={HomePage} />
        <Route path="/stories" element={StoriesPage} />
        <Route path="/submit-story" element={SubmitStoryPage} />
        <Route path="/about-us" element={AboutUsPage} />
        <Route path="/resources" element={ResourcesPage} />
        <Route path="/contact-us" element={ContactUsPage} />
      </Routes>
    </Router>
  );
}

export default App;
