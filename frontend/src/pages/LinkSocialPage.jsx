import React from 'react';
import { Box, Button, Typography, Divider } from '@mui/material';
import GoogleIcon from '@mui/icons-material/Google';
import FacebookIcon from '@mui/icons-material/Facebook';

const LinkSocialPage = () => {
  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Link Social Media Accounts
      </Typography>
      <Typography variant="body1" sx={{ mb: 3 }}>
        Connect your social media accounts for easier login.
      </Typography>
      <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2, maxWidth: '300px' }}>
        <Button variant="outlined" startIcon={<GoogleIcon />}>
          Link Google Account
        </Button>
        <Button variant="outlined" startIcon={<FacebookIcon />}>
          Link Facebook Account
        </Button>
      </Box>
    </Box>
  );
};

export default LinkSocialPage;
