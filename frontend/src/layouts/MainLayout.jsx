import React from 'react';
import { Outlet, useNavigate, useLocation } from 'react-router-dom';
import {
  AppBar,
  Box,
  Button,
  Container,
  Toolbar,
  Typography,
  IconButton,
} from '@mui/material';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';

const MainLayout = () => {
  const navigate = useNavigate();
  const location = useLocation();

  const handleLogout = () => {
    // TODO: Add actual logout logic
    console.log('Logout');
    navigate('/', { state: { farewell: true } }); // Redirect with state
  };
  
  const handlePreferences = () => {
    navigate('/preferences');
  }

  // Determine button visibility based on the current path
  const publicRoutes = ['/', '/login', '/signup'];
  const topLevelPages = ['/', '/login', '/signup', '/home'];
  const isAuthenticated = !publicRoutes.includes(location.pathname);
  const isTopLevelPage = topLevelPages.includes(location.pathname);


  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <Toolbar>
          {!isTopLevelPage && (
            <IconButton
              edge="start"
              color="inherit"
              aria-label="back"
              onClick={() => navigate(-1)}
              sx={{ mr: 1 }}
            >
              <ArrowBackIcon />
            </IconButton>
          )}
          <Typography
            variant="h6"
            component="div"
            onClick={() => isAuthenticated ? navigate('/home') : navigate('/')}
            sx={{ flexGrow: 1, cursor: 'pointer' }}
          >
            Greetings
          </Typography>
          {isAuthenticated && (
            <Box>
              <Button color="inherit" onClick={handlePreferences}>
                Preferences
              </Button>
              <Button color="inherit" onClick={handleLogout}>
                Logout
              </Button>
            </Box>
          )}
        </Toolbar>
      </AppBar>
      <Container component="main" sx={{ mt: 4, mb: 4 }}>
        <Outlet />
      </Container>
    </Box>
  );
};

export default MainLayout;

