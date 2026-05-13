import sounddevice as sd
import numpy as np

print(sd.query_devices())
class AudioManager:
    def __init__(self, engine):
        self.engine = engine
        self.enabled = False
        self.sample_rate = 16000 # DNS-48 expects 16kHz
        self.chunk_size = 1024   # ~64ms of audio at 16kHz
        self.current_rms = 0.0

    def stream_callback(self, indata, outdata, frames, time, status):
        if status:
            print(status)
            
        if self.enabled:
            # 1. Convert Stereo Input to Mono (Average the channels)
            # indata shape is (1024, 2), we want (1024,)
            if indata.shape[1] > 1:
                mono_input = np.mean(indata, axis=1)
            else:
                mono_input = indata.flatten()

            # 2. Process through AI
            clean_audio = self.engine.process_chunk(mono_input)
        
            # 3. Match Output Shape
            # If outdata expects 2 channels, we copy the clean mono audio to both
            if outdata.shape[1] > 1:
            # Reshape clean_audio to (1024, 1) then tile it to (1024, 2)
                clean_stereo = np.column_stack((clean_audio, clean_audio))
                outdata[:] = clean_stereo
            else:
                outdata[:] = clean_audio.reshape(-1, 1)
        else:
            # Bypass mode: Direct pass-through
            outdata[:] = indata

    def start_stream(self, input_device_id, virtual_cable_id):
        input_info = sd.query_devices(input_device_id)
        output_info = sd.query_devices(virtual_cable_id)
    
    # Determine the required channels. 
    # Most Windows devices default to 2 channels (Stereo)
        input_ch = input_info['max_input_channels']
        output_ch = output_info['max_output_channels']
    
    # Use 2 if both support it, otherwise try to find a common ground
        channels = min(input_ch, output_ch)

        self.stream = sd.Stream(
            device=(input_device_id, virtual_cable_id),
            samplerate=self.sample_rate,
            blocksize=self.chunk_size,
            channels=channels, 
            callback=self.stream_callback
            )
        self.stream.start()