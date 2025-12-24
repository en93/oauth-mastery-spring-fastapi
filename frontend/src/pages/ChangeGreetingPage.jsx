import React, { useState } from 'react';
import {
  Box,
  Button,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  Typography,
} from '@mui/material';

const ChangeGreetingPage = () => {
  const [greeting, setGreeting] = useState('');

  const handleGreetingChange = (event) => {
    setGreeting(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // TODO: Handle greeting update logic
    console.log('New greeting:', greeting);
  };

  return (
    <Box
      component="form"
      onSubmit={handleSubmit}
      sx={{ maxWidth: '400px' }}
    >
      <Typography variant="h4" gutterBottom>
        Change Preferred Greeting
      </Typography>
      <FormControl fullWidth required sx={{ mt: 3, mb: 2 }}>
        <InputLabel id="greeting-select-label">New Greeting</InputLabel>
        <Select
          labelId="greeting-select-label"
          id="greeting-select"
          value={greeting}
          label="New Greeting"
          onChange={handleGreetingChange}
        >
          <MenuItem value={'Hello'}>Hello</MenuItem>
          <MenuItem value={'Hi'}>Hi</MenuItem>
          <MenuItem value={'Hey'}>Hey</MenuItem>
          <MenuItem value={'Yo'}>Yo</MenuItem>
          <MenuItem value={'Howdy'}>Howdy</MenuItem>
        </Select>
      </FormControl>
      <Button
        type="submit"
        fullWidth
        variant="contained"
      >
        Update Greeting
      </Button>
    </Box>
  );
};

export default ChangeGreetingPage;
