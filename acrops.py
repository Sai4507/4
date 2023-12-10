crop_growth_periods = {

  "apple": 7, "banana": 9, "blackgram": 3, "chickpea": 4, "coconut": 9, "coffee": 9, "cotton": 6,

  "grapes": 9, "jute": 6, "kidneybeans": 3, "lentil": 3, "corn": 3, "mango": 9, "mothbeans": 3,

  "mungbeans": 3, "muskmelon": 3, "orange": 9, "papaya": 8, "pigeonpeas": 6, "pomegranate": 9,

  "rice": 6, "watermelon": 3

}

class SuitableCrops:

  def __init__(self, cropList, cropTempDict, avgTemp):

    self.cropTempDict = cropTempDict

    self.avgTemp = avgTemp

    self.cropList = [crop.lower() for crop in cropList] # Convert crop names to lowercase

  def crops(self):

    suitcrop = []

    for crop in self.cropList:

      if crop in crop_growth_periods and crop_growth_periods[crop] <= len(self.avgTemp):

        cropMin, cropMax = self.cropTempDict[crop]

        if any(cropMin <= temp <= cropMax for temp in self.avgTemp):

          suitcrop.append(crop)

    return suitcrop

def runSuitableCropList(cropList, cropTempDict, avgTemp):

  obj=SuitableCrops(cropList, cropTempDict, avgTemp)

  suitcrops=obj.crops()

  return suitcrops