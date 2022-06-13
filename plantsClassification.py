from attr import dataclass
from numpy import place
from torchvision import models, transforms
import torch
import torch.nn as nn
from PIL import Image
from torch.utils.data import Dataset, DataLoader
import pymysql


device = torch.device("cpu")
dir = '/home/ubuntu/img/and/'
#dir = 'C:/Pegue/Final_Project/plant_project-main/plant_project-main/media/'

model=models.regnet_x_32gf(pretrained=False)
model.fc=nn.Linear(in_features=2520, out_features=6) 
model.load_state_dict(torch.load("/home/ubuntu/ai/plants_classification.pt", map_location=torch.device('cpu')))
#model.load_state_dict(torch.load("C:/Pegue/Final_Project/test2/plants_classification.pt", map_location=torch.device('cpu')))
model = model.to(device)


class customDataset(Dataset):
    def __init__(self, filename, transform = None):        
        
        self.filename = dir + filename
        self.transform = transform
        self.targets= ['멕시코소철', '백량금', '아글라오네마', '옥살리스(사랑초)', '골드크레스트 "윌마"'] 

    def __len__(self):
        return len(self.filename)

    def __getitem__(self, idx):
    
      img=Image.open(self.filename)
      
      if self.transform:
            image = self.transform(img)    
      return image, self.targets



def Predict(userid, filename, num_images=2):   

  was_training = model.training
  model.eval() # 모델을 검증모드로



  print('Predict....(filename : {})'.format(filename))

  tf = transforms.Compose([
    transforms.Resize((224, 224)), # 이미지 사이즈를 resize로 변경한다.
    #transforms.CenterCrop(200), # 이미지 중앙을 resize × resize로 자른다      
    transforms.ToTensor(), # 이미지 데이터를 tensor로 바꿔준다.
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]) # 이미지 정규화        
  ])

  dataset = customDataset(filename, transform=tf)

  imgloader = DataLoader(dataset, batch_size=32, shuffle=False, num_workers=0)

  class_names = ['멕시코소철', '백량금', '아글라오네마', '옥살리스(사랑초)', '골드크레스트 "윌마"']
  #class_names = [16245, 18694, 19469, 19474, 12955]
  print('Predict....(tensor complete)')
  
  with torch.no_grad():

    iterator=iter(imgloader)

    inputs, labels = next(iterator)   
    
    print('Predict....(input complete)')

    outputs = model(inputs)

    _, preds = torch.max(outputs, 1)
        
    plant = class_names[preds[0]]
    model.train(mode=was_training)      
    
    print('Predict....(output complete)')
  return plant





