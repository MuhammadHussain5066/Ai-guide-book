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

      const response = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
          query: input,
          context: selectedText || ""
        })
      });

      const data = await response.json();
      setMessages(prev => [...prev, { role: 'assistant', content: data.answer }]);
    } catch (error) {
      console.error('Error:', error);
      setMessages(prev => [...prev, { 
        role: 'assistant', 
        content: 'Sorry, I could not connect to the chatbot service. Please make sure the backend is running.' 
      }]);
    }
    setLoading(false);
  };

  return (
    <>
      <button 
        className={styles.chatButton}
        onClick={() => setIsOpen(!isOpen)}
        title="Ask AI about the book"
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
            {messages.length === 0 && (
              <div className={styles.welcomeMessage}>
                👋 Hi! I can answer questions about this AI Guide Book.
                <br /><br />
                💡 Tip: Select any text on the page and ask me about it!
              </div>
            )}
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
              placeholder="Ask a question (or select text first)..."
            />
            <button onClick={sendMessage} disabled={loading}>
              {loading ? '...' : 'Send'}
            </button>
          </div>
        </div>
      )}
    </>
  );
}