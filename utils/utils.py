import torch
from PIL import Image
from torchvision import transforms
from model import Model

model = Model("model_files/50.pth")

image_transforms = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

decode_answer = {
    0: "Shih-Tzu",
    1: "Rhodesian ridgeback",
    2: "Beagle",
    3: "English foxhound",
    4: "Border terrier",
    5: "Australian terrier",
    6: "Golden retriever",
    7: "Old English sheepdog",
    8: "Samoyed",
    9: "Dingo",
}

def get_predict(image):
    int_predict = torch.max(model(image), 1)[1].numpy()[0]
    str_predict = decode_answer[int_predict]
    return str_predict

def prepare_image(image):
    image = Image.open(image)
    image = image_transforms(image).unsqueeze(0)
    return image
