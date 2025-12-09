import React from 'react';
import RagChatbot from '../components/RagChatbot';

export default function Root({children}) {
  return (
    <>
      {children}
      <RagChatbot />
    </>
  );
}