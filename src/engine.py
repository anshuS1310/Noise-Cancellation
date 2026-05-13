import torch
from denoiser import pretrained
from denoiser.dsp import LowPassFilters
import numpy as np

class AudioEngine:
    def __init__(self):
        # Load Facebook's DNS-48 model 
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = pretrained.dns48().to(self.device)
        self.model.eval()
        
    def process_chunk(self, audio_chunk):
        """
        Takes a numpy array chunk, cleans it, and returns it.
        """
        # 1. Convert Numpy to PyTorch Tensor
        out_tensor = torch.from_numpy(audio_chunk).to(self.device).float()
        
        # Ensure correct shape [Batch, Channels, Time]
        if out_tensor.ndim == 1:
            out_tensor = out_tensor.unsqueeze(0).unsqueeze(0)
        
        # 2. Volume Normalization (Capture input energy)
        input_rms = torch.sqrt(torch.mean(out_tensor**2))
        
        # 3. AI Inference
        with torch.no_grad():
            cleaned_tensor = self.model(out_tensor)
            
        # 4. Volume Matching (Restore energy to the cleaned speech)
        output_rms = torch.sqrt(torch.mean(cleaned_tensor**2))
        
        if output_rms > 0:
            gain = input_rms / (output_rms + 1e-5) # Avoid division by zero
            cleaned_tensor *= gain

        # 5. Convert back to Numpy
        return cleaned_tensor.squeeze().cpu().numpy()