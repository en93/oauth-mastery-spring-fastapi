import React from 'react';
import { Routes, Route } from 'react-router-dom';

// Page Imports
import LandingPage from '../pages/LandingPage';
import LoginPage from '../pages/LoginPage';
import SignupPage from '../pages/SignupPage';
import HomePage from '../pages/HomePage';
import PreferencesPage from '../pages/PreferencesPage';
import ChangePasswordPage from '../pages/ChangePasswordPage';
import VerifyEmailPage from '../pages/VerifyEmailPage';
import LinkSocialPage from '../pages/LinkSocialPage';
import ChangeGreetingPage from '../pages/ChangeGreetingPage';


// Layout Import
import MainLayout from '../layouts/MainLayout';


const AppRouter = () => {
  return (
    <Routes>
      {/* Public Routes */}
      <Route path="/" element={<LandingPage />} />
      <Route path="/login" element={<LoginPage />} />
      <Route path="/signup" element={<SignupPage />} />

      {/* Protected Routes - These will be wrapped by the MainLayout */}
      <Route element={<MainLayout />}>
        <Route path="/home" element={<HomePage />} />
        <Route path="/preferences" element={<PreferencesPage />} />
        <Route path="/change-password" element={<ChangePasswordPage />} />
        <Route path="/verify-email" element={<VerifyEmailPage />} />
        <Route path="/link-social" element={<LinkSocialPage />} />
        <Route path="/change-greeting" element={<ChangeGreetingPage />} />
      </Route>
    </Routes>
  );
};

export default AppRouter;


