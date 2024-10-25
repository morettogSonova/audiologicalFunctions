#! this files contains various classes for evaluation of audiological quantities
import numpy as np
from scipy.interpolate import interp1d

#%%
class AudiogramEval:
    """
    class for evaluation of various qunatities related to the audiogram
    """
    #! standard frequency arrays for audiograms
    frequencies = {
        4: [500, 1000, 2000, 4000],
        8: [250, 500, 1000, 2000, 3000, 4000, 6000, 8000],
        11: [125, 250, 500, 750, 1000, 1500, 2000, 3000, 4000, 6000, 8000]
    }
    #! specify whicha frequency array is the standard
    standardArray = 8
   
    @staticmethod    
    def frequencyArray(sizeArray=None):
        #! return standatdized audiogram frequency arrays
        """
        specify the standardized audiogram frequency arrays. if no input is given the standard frequency range is returned
        """
        if sizeArray is None:
            return AudiogramEval.frequencies[AudiogramEval.standardArray]
        elif sizeArray in AudiogramEval.frequencies:
            return AudiogramEval.frequencies[sizeArray]
        else:
            raise ValueError("No stored frequency array for the given value")    

    @staticmethod    
    def averageHL(audiogram):
        """
        return the average hearing loss of an audiogram
        """
        return sum(audiogram)/len(audiogram)

    @staticmethod    
    def average4PTA(audiogram):
        """
        return the 4 pure ton average hearing loss of an audiogram
        """
        freqArray = AudiogramEval.frequencyArray(len(audiogram))
        freq4PTA = AudiogramEval.frequencies[4]
        fInterp = interp1d(freqArray,audiogram)

        return fInterp(freq4PTA).mean()
 
