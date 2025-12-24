import React from 'react';
import { useNavigate } from 'react-router-dom';
import {
  Box,
  Typography,
  List,
  ListItem,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Divider,
} from '@mui/material';
import LinkIcon from '@mui/icons-material/Link';
import RecordVoiceOverIcon from '@mui/icons-material/RecordVoiceOver';
import PasswordIcon from '@mui/icons-material/Password';
import MarkEmailReadIcon from '@mui/icons-material/MarkEmailRead';

const PreferencesPage = () => {
  const navigate = useNavigate();

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Preferences
      </Typography>
      <List component="nav" aria-label="preferences options">
        <ListItem disablePadding>
          <ListItemButton onClick={() => navigate('/link-social')}>
            <ListItemIcon>
              <LinkIcon />
            </ListItemIcon>
            <ListItemText primary="Link Social Media Accounts" />
          </ListItemButton>
        </ListItem>
        <Divider />
        <ListItem disablePadding>
          <ListItemButton onClick={() => navigate('/change-greeting')}>
            <ListItemIcon>
              <RecordVoiceOverIcon />
            </ListItemIcon>
            <ListItemText primary="Change Preferred Greeting" />
          </ListItemButton>
        </ListItem>
        <Divider />
        <ListItem disablePadding>
          <ListItemButton onClick={() => navigate('/change-password')}>
            <ListItemIcon>
              <PasswordIcon />
            </ListItemIcon>
            <ListItemText primary="Change Password" />
          </ListItemButton>
        </ListItem>
        <Divider />
        <ListItem disablePadding>
          <ListItemButton onClick={() => navigate('/verify-email')}>
            <ListItemIcon>
              <MarkEmailReadIcon />
            </ListItemIcon>
            <ListItemText primary="Verify Email" />
          </ListItemButton>
        </ListItem>
      </List>
    </Box>
  );
};

export default PreferencesPage;

