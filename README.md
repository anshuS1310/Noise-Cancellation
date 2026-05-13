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
# 📥 Installation

## Clone the Repository

```bash
git clone https://github.com/yourusername/NoiseCancellation.git
cd NoiseCancellation
```

## Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

# 🖥 How to Use

## 1. Install Virtual Audio Driver (Critical First Step)

To pipe the "clean" audio from this app into your meetings, you must install a virtual driver that acts as a bridge.

- **Windows Users:** Download and install **[VB-Audio Virtual Cable](https://vb-audio.com/Cable/)**.
- **macOS Users:** Download and install **[BlackHole (2ch)](https://existential.audio/blackhole/)**.
  - *Note:* On macOS, you may need to restart your system after installation for the driver to appear in your Audio MIDI Setup.

---

## 2. Run the Application

Launch the software via your terminal:

```bash
python main.py
```

> Note for Mac users: Grant "Microphone Access" when prompted by macOS Security & Privacy.

---

## 3. Configure the AI Interface

### Input Source
Select your physical microphone (e.g., "Realtek Audio" or "Built-in Mic") from the dropdown menu.

### Activate Filter
Flip the toggle switch to ON. The UI will glow neon blue to indicate the AI "Brain" is active.

### Visualizer
Speak into the mic; the waveform will react to your cleaned voice activity.

---

## 4. Connect to Your Apps (Zoom / Discord / Teams)

Open the Audio Settings of your communication app.

Set the Microphone Input to:

### Windows
```plaintext
CABLE Output (VB-Audio Virtual Cable)
```

### macOS
```plaintext
BlackHole 2ch
```

Your listeners will now hear the purified, noise-canceled audio stream.

---

# 🧠 Technical Overview

## Frameworks
- PyTorch
- CustomTkinter
- SoundDevice

## Model
- Meta’s Denoiser (DNS-48)

## Optimization

### Windows
Supports NVIDIA CUDA for GPU acceleration.

### macOS
Optimized for Apple Silicon (M1/M2/M3) using Metal Performance Shaders (MPS).

---

# 📄 License

This project was developed for educational purposes, focusing on UI/UX minimalist design and AI integration.
