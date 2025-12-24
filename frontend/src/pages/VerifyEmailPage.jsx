import React from 'react';
import {
  Box,
  Typography,
  FormControlLabel,
  Checkbox,
} from '@mui/material';

const VerifyEmailPage = () => {
  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Email Verification
      </Typography>
      <Typography variant="body1" sx={{ mb: 2 }}>
        This is a placeholder page to represent verifying a user's email address.
      </Typography>
      <FormControlLabel
        control={<Checkbox value="remember" color="primary" />}
        label="Mark email as verified"
      />
    </Box>
  );
};

export default VerifyEmailPage;
