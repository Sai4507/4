import pandas as pd


class suggestCrops:

  def __init__(self,resultList,InputList):

    self.resultList=resultList

    self.N=InputList[0]

    self.P=InputList[1]

    self.K=InputList[2]

    self.suggestions=[]

    self.suggestionsDict={}

  def suggestList(self):

    for dict in self.resultList:

      self.temperaturelist=[]

      if self.N in range(int(dict["Nmin"]),int(dict["Nmax"])):

        if self.P in range(int(dict["Pmin"]),int(dict["Pmax"])):

          if self.K in range(int(dict["Kmin"]),int(dict["Kmax"])):

            self.suggestions.append(dict["Label"])

            self.temperaturelist.append(float(dict["TemperatureMin"]))

            self.temperaturelist.append(float(dict["TemperatureMax"]))

            self.suggestionsDict[dict["Label"]]=self.temperaturelist

  def getsuggestionsDict(self):

    self.suggestList()

    return self.suggestions,self.suggestionsDict

    '''print(self.suggestions)

    print(self.suggestionsDict)'''

def runSuggestCrops(listNPK):

  df = pd.read_csv('Crop_recommendation.csv')

  # Get the unique labels

  unique_labels = df['label'].unique()

  # Initialize an empty list to store the results

  results_list = []

  # Iterate over unique labels

  for label in unique_labels:

    label_data = df[df['label'] == label]

    result_dict = {

      'Label': label,

      'Nmin': label_data['N'].min(),

      'Nmax': label_data['N'].max(),

      'Pmin': label_data['P'].min(),

      'Pmax': label_data['P'].max(),

      'Kmin':label_data['K'].min(),

      'Kmax':label_data['K'].max(),

      'TemperatureMin': label_data['temperature'].min(),

      'TemperatureMax': label_data['temperature'].max(),

    }

    results_list.append(result_dict)

  # Print the list of results

  obj=suggestCrops(results_list,listNPK)

  slist,sugDict=obj.getsuggestionsDict()

  return slist,sugDict