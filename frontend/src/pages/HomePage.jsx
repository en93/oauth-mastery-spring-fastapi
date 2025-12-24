import React from 'react';
import { Box, Typography } from '@mui/material';

const HomePage = () => {
  // In a real app, you'd get the user's name and preferred greeting from a context or state management
  const userName = 'Jane Doe';
  const preferredGreeting = 'Howdy';

  return (
    <Box
      sx={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        textAlign: 'center',
      }}
    >
      <Typography component="h1" variant="h3" gutterBottom>
        {preferredGreeting}, {userName}!
      </Typography>
      <Typography variant="body1" color="text.secondary">
        Welcome to the application.
      </Typography>
    </Box>
  );
};

export default HomePage;
