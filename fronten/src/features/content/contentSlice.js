import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import axios from 'axios';

export const fetchContents = createAsyncThunk('content/fetchContents', async () => {
  const response = await axios.get('/api/content');
  return response.data;
});

const contentSlice = createSlice({
  name: 'content',
  initialState: {
    items: [],
    status: 'idle',
    error: null,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchContents.fulfilled, (state, action) => {
        state.items = action.payload;
      });
  },
});

export default contentSlice.reducer;
