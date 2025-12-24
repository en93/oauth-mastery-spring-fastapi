import React from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { Alert, Box, Button, Container, Typography } from '@mui/material';

const LandingPage = () => {
  const navigate = useNavigate();
  const { state } = useLocation();

  return (
    <Container component="main" maxWidth="xs">
      <Box
        sx={{
          marginTop: 8,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          textAlign: 'center',
        }}
      >
        {state?.farewell && (
          <Alert severity="success" sx={{ mb: 3, width: '100%' }}>
            Farewell! You have been successfully logged out.
          </Alert>
        )}
        <Typography component="h1" variant="h2" gutterBottom>
          Greetings
        </Typography>
        <Typography variant="h5" color="text.secondary" paragraph>
          Welcome to your new favorite app.
        </Typography>
        <Box sx={{ mt: 3 }}>
          <Button
            variant="contained"
            size="large"
            sx={{ mx: 1 }}
            onClick={() => navigate('/login')}
          >
            Login
          </Button>
          <Button
            variant="outlined"
            size="large"
            sx={{ mx: 1 }}
            onClick={() => navigate('/signup')}
          >
            Sign Up
          </Button>
        </Box>
      </Box>
    </Container>
  );
};

export default LandingPage;

