import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchContents } from '../../features/content/contentSlice';

const ContentList = () => {
  const dispatch = useDispatch();
  const contents = useSelector((state) => state.content.items);

  useEffect(() => {
    dispatch(fetchContents());
  }, [dispatch]);

  return (
    <div>
      <h2>Content List</h2>
      {contents.map((content) => (
        <div key={content.id}>
          <h3>{content.title}</h3>
          <p>{content.body}</p>
        </div>
      ))}
    </div>
  );
};

export default ContentList;
