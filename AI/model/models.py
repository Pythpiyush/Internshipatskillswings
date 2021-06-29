from gingerit.gingerit import GingerIt
import pickle
import librosa
import numpy as np

def grammercheck(text):
    parser = GingerIt()
    ans = parser.parse(text)
    return ans['result']


def getfluency(file_name):
    loaded_model = pickle.load(open('fluency_model.sav', 'rb'))
    label = ['Low','Intermediate','High']
    X , sample_rate = librosa.load(file_name, sr=None)
    if X.ndim > 1:
        X = X[:,0]
    X = X.T
    
    stft = np.abs(librosa.stft(X))
            
    mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=20).T, axis=0) #Returns N_mel coefs
    rmse = np.mean(librosa.feature.rms(y=X).T, axis=0) #RMS Energy for each Frame (Stanford's). Returns 1 value 
    spectral_flux = np.mean(librosa.onset.onset_strength(y=X, sr=sample_rate).T, axis=0) #Spectral Flux (Stanford's). Returns 1 Value
    zcr = np.mean(librosa.feature.zero_crossing_rate(y=X).T, axis=0) #Returns 1 value
    cc = np.hstack([mfccs, rmse, spectral_flux, zcr])
    cc = cc.reshape(1, -1)
    return label[loaded_model.predict(cc)[0]]
    



