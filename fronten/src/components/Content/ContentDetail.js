import React from 'react';
import { useParams } from 'react-router-dom';

const ContentDetail = () => {
  const { id } = useParams();
  // Assume you fetch the content by id here

  return (
    <div>
      <h2>Content Detail</h2>
      {/* Display content details here */}
    </div>
  );
};

export default ContentDetail;
