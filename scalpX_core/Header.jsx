# 36/45: /frontend/src/components/Header.jsx
import React from 'react';
import logo from '../assets/logo.svg';

const Header = () => {
  return (
    <header style={{ display: 'flex', alignItems: 'center', padding: '10px 20px', backgroundColor: '#1a1a1a', color: '#fff' }}>
      <img src={logo} alt="ScalpX Logo" style={{ height: '40px', marginRight: '20px' }} />
      <h1 style={{ margin: 0, fontSize: '24px' }}>🧠 ScalpX Dashboard</h1>
    </header>
  );
};

export default Header;

# 37/45: /frontend/src/components/Footer.jsx
import React from 'react';

const Footer = () => {
  return (
    <footer style={{ padding: '10px 20px', marginTop: '20px', borderTop: '1px solid #ccc', textAlign: 'center', backgroundColor: '#1a1a1a', color: '#fff' }}>
      <p>© {new Date().getFullYear()} ScalpX. Built with 🚀 for smart traders.</p>
    </footer>
  );
};

export default Footer;

# 38/45: /frontend/src/App.jsx
import React, { useState } from 'react';
import ChartView from './components/ChartView';
import SettingsPanel from './components/SettingsPanel';
import TradeReplay from './components/TradeReplay';
import Header from './components/Header';
import Footer from './components/Footer';

const mockTrades = [
  { symbol: 'AAPL', entry: 190, exit: 192.5, result: '+2.5%', notes: 'VWAP bounce + RSI <30' },
  { symbol: 'AMD', entry: 110, exit: 111.5, result: '+1.4%', notes: 'Breakout scalp' }
];

const App = () => {
  const [settings, setSettings] = useState({ rsi: 30, vwap: 2 });

  const updateSetting = (key, value) => {
    setSettings(prev => ({ ...prev, [key]: Number(value) }));
  };

  return (
    <div style={{ fontFamily: 'Arial, sans-serif', backgroundColor: '#f9f9f9', minHeight: '100vh' }}>
      <Header />
      <main style={{ padding: '20px' }}>
        <ChartView />
        <SettingsPanel settings={settings} updateSetting={updateSetting} />
        <TradeReplay trades={mockTrades} />
      </main>
      <Footer />
    </div>
  );
};

export default App;

# 39/45: /frontend/index.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>ScalpX Dashboard</title>
  <meta name="theme-color" content="#1a1a1a" />
  <link rel="icon" href="/src/assets/logo.svg" type="image/svg+xml" />
</head>
<body style="margin: 0; background-color: #f9f9f9;">
  <div id="root"></div>
  <script type="module" src="/src/index.jsx"></script>
</body>
</html>

# 40/45: /frontend/vite.config.js
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://localhost:5000',
        changeOrigin: true,
        rewrite: path => path.replace(/^\/api/, '')
      }
    }
  },
  build: {
    outDir: 'dist',
    sourcemap: true
  },
  resolve: {
    alias: {
      '@': '/src'
    }
  }
});