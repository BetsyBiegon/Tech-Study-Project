import { configureStore } from '@reduxjs/toolkit';
import authReducer from '../features/auth/authSlice';
import contentReducer from '../features/content/contentSlice';

export default configureStore({
  reducer: {
    auth: authReducer,
    content: contentReducer,
  },
});
