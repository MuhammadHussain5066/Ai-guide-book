import React, { useState } from 'react';
import styles from './RagChatbot.module.css';

export default function RagChatbot() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [isOpen, setIsOpen] = useState(false);
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { role: 'user', content: input };
    setMessages([...messages, userMessage]);
    setInput('');
    setLoading(true);

    try {
      // Get selected text if any
      const selectedText = window.getSelection().toString();
      const query = selectedText 
        ? `Context: "${selectedText}"\n\nQuestion: ${input}`
        : input;

      const response = await fetch('YOUR_API_ENDPOINT/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query })
      });

      const data = await response.json();
      setMessages(prev => [...prev, { role: 'assistant', content: data.answer }]);
    } catch (error) {
      setMessages(prev => [...prev, { 
        role: 'assistant', 
        content: 'Error: Could not get response' 
      }]);
    }
    setLoading(false);
  };

  return (
    <>
      <button 
        className={styles.chatButton}
        onClick={() => setIsOpen(!isOpen)}
      >
        💬
      </button>

      {isOpen && (
        <div className={styles.chatWidget}>
          <div className={styles.chatHeader}>
            <h3>Ask about the book</h3>
            <button onClick={() => setIsOpen(false)}>✕</button>
          </div>

          <div className={styles.chatMessages}>
            {messages.map((msg, idx) => (
              <div key={idx} className={styles[msg.role]}>
                {msg.content}
              </div>
            ))}
            {loading && <div className={styles.loading}>Thinking...</div>}
          </div>

          <div className={styles.chatInput}>
            <input
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
              placeholder="Ask a question (select text first for context)..."
            />
            <button onClick={sendMessage}>Send</button>
          </div>
        </div>
      )}
    </>
  );
}