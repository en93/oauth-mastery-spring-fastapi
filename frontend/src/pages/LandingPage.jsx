import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Box, Button, Container, Typography } from '@mui/material';

const LandingPage = () => {
  const navigate = useNavigate();

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
