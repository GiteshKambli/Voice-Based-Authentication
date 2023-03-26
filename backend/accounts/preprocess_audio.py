import os

import librosa
import numpy as np
import pandas as pd
from tqdm import tqdm

import torch
import torch.utils.data
import torch.nn.functional as F

from librosa.filters import mel as librosa_mel_fn
from librosa.util import normalize
from scipy.io.wavfile import read

import matplotlib.pyplot as plt


mel_basis = {}
hann_window = {}

params = {"N_FFT": 1024,
        "Mel_Dim": 80,
        "Frame_Length": 1024,
        "Frame_Shift": 256,
        "Sample_Rate": 22050,
        "Mel_F_Min": 0,
        "Mel_F_Max": 8000,}

def load_wav(full_path):
    """
        This method reads a wav file and returns the sampling rate and data
    """
    
    sampling_rate, data = read(full_path)
    return data, sampling_rate


def dynamic_range_compression_torch(x, C=1, clip_val=1e-5):
    """
        This method performs dynamic range compression on the spectrogram
    """
    
    return torch.log(torch.clamp(x, min=clip_val) * C)

def spectral_normalize_torch(magnitudes):
    """
        This method normalizes the spectrogram
    """
    
    output = dynamic_range_compression_torch(magnitudes)
    return output

def mel_spectrogram(y, n_fft, n_mels, sr, hop_size, win_size, fmin, fmax, center=False):
    """
        This method converts the audio into a mel-spectrogram
    """

    if torch.min(y) < -1.:
        print('min value is ', torch.min(y))
    if torch.max(y) > 1.:
        print('max value is ', torch.max(y))

    global mel_basis, hann_window
    if fmax not in mel_basis:
        mel = librosa_mel_fn(sr = sr, n_fft = n_fft, n_mels =  n_mels, fmin = fmin, fmax = fmax)
        mel_basis[str(fmax) + '_' + str(y.device)] = torch.from_numpy(mel).float().to(y.device)
        hann_window[str(y.device)] = torch.hann_window(win_size).to(y.device)

    y = F.pad(y.unsqueeze(1), (int((n_fft - hop_size) / 2), int((n_fft - hop_size) / 2)), mode='reflect')
    y = y.squeeze(1)

    spec = torch.stft(y, n_fft, hop_length=hop_size, win_length=win_size, window=hann_window[str(y.device)],
                      center=center, pad_mode='reflect', normalized=False, onesided=True)

    spec = torch.sqrt(spec.pow(2).sum(-1) + (1e-9))

    spec = torch.matmul(mel_basis[str(fmax) + '_' + str(y.device)], spec)
    spec = spectral_normalize_torch(spec)

    return spec

def pattern_generate(path, n_fft: int, n_mels: int, sample_rate: int, hop_size: int, win_size: int,
                     fmin: int,
                     fmax: int,
                     center: bool = False,
                     top_db=60
                     ):
    
    """
        This method reads a file from the path and converts it into a mel-spectrogram and returns the audio and mel
    """
    
    try:
        audio, _ = librosa.load(path, sr=sample_rate)
    except Exception as e:
        return None, None

    audio = librosa.effects.trim(audio, top_db=top_db, frame_length=512, hop_length=256)[0]
    audio = librosa.util.normalize(audio) * 0.95
    mel = mel_spectrogram(
        y=torch.from_numpy(audio).float().unsqueeze(0),
        n_fft=n_fft,
        n_mels=n_mels,
        sr=sample_rate,
        hop_size=hop_size,
        win_size=win_size,
        fmin=fmin,
        fmax=fmax,
        center=center
    ).squeeze(0).T.numpy()

    return audio, mel.T

def pad_spec(arr, desired_shape, mode):
    """
        This method pads the spectrogram to the desired shape
    """
    
    pad_width = [(0, desired_shape[0] - arr.shape[0]), (0, desired_shape[1] - arr.shape[1])]
    padded_arr = np.pad(arr, pad_width, mode=mode)
    return padded_arr

def pad_crop(spec,mode):
    """
        This method pads or crops the spectrogram to the desired shape
    """
    
    y = spec.shape[1]
    if y < 450:
        return pad_spec(spec, desired_shape = (80,450), mode = mode)
    elif y >= 450:
        return spec[:,:450]
    
def get_mel(path):
    audio, mel = pattern_generate(path, params['N_FFT'], params['Mel_Dim'], params['Sample_Rate'], params['Frame_Shift'],
                                  params['Frame_Length'], params['Mel_F_Min'], params['Mel_F_Max'])
     
    mel = pad_crop(mel, mode = 'mean')
    mel = mel.reshape(-1, 80, 450)
    return mel
            
# print(get_mel('media/mel1.wav'))