# 🎧 NoiseCancellation AI
### Real-time Deep Learning Speech Enhancement

NoiseCancellation is a minimalist, AI-powered desktop application designed to **purify microphone audio in real-time**. By leveraging Meta’s **DNS-48 deep learning model**, the application removes background noise such as fans, keyboard typing, traffic, and ambient sounds while preserving clear human speech.

The cleaned audio is then routed to a virtual audio device, making it compatible with communication platforms like **Zoom, Discord, Microsoft Teams, Google Meet**, and more.

---

# 🚀 Features

## 🧠 Deep Learning Core
- Uses a pre-trained **PyTorch DNS-48** speech enhancement model.
- Performs high-quality real-time noise suppression.
- Preserves speech clarity while reducing unwanted environmental sounds.

## 🎨 Aesthetic UI
- Minimalist **Dark Mode** interface.
- Built using **CustomTkinter**.
- Neon-blue accents for a modern gaming/studio aesthetic.
- Smooth controls and responsive design.

## 📈 Live Audio Visualizer
- Real-time waveform visualization.
- Reacts dynamically to voice activity.
- Indicates purification intensity visually.

## ⚡ Low-Latency Audio Streaming
- Optimized audio callback pipelines.
- Minimal delay between microphone input and clean output.
- Suitable for live communication and streaming.

---

# 📂 Project Structure

```plaintext
NoiseCancellation/
├── main.py                  # Entry point (initializes AI, Audio, and UI)
├── requirements.txt         # Project dependencies
└── src/
    ├── __init__.py
    ├── audio_manager.py     # Hardware routing and volume tracking
    ├── engine.py            # PyTorch AI model processing
    └── ui.py                # CustomTkinter aesthetic interface
