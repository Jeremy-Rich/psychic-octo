import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import HomePage from './pages/HomePage';
import StoriesPage from './pages/StoriesPage';
import SubmitStoryPage from './pages/SubmitStoryPage';
import AboutUsPage from './pages/AboutUsPage';
import ResourcesPage from './pages/ResourcesPage';
import ContactUsPage from './pages/ContactUsPage';

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={HomePage} />
        <Route path="/stories" component={StoriesPage} />
        <Route path="/submit-story" component={SubmitStoryPage} />
        <Route path="/about-us" component={AboutUsPage} />
        <Route path="/resources" component={ResourcesPage} />
        <Route path="/contact-us" component={ContactUsPage} />
      </Switch>
    </Router>
  );
}

export default App;
