from src.engine import AudioEngine
from src.audio_manager import AudioManager
from src.ui import NoiseCancellationUI
import sounddevice as sd

if __name__ == "__main__":
    # 1. Start the AI Brain
    engine = AudioEngine()
    
    # 2. Start the Plumbing
    manager = AudioManager(engine)
    
    # 3. Launch the Interface
    app = NoiseCancellationUI(manager)
    
    # Note: In a real run, you'd pick the IDs from the UI.
    # For now, we start the stream with placeholder IDs (0, 1)
    # You can update start_stream to be called via a "Start" button in UI
    manager.start_stream(input_device_id=1, virtual_cable_id=8)
    
    app.mainloop()