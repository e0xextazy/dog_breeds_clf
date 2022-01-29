from torchvision import models
import torch


class Model():
    def __init__(self, path):
        self.model = models.resnet50(pretrained=False)
        self.num_ftrs = self.model.fc.in_features
        self.model.fc = torch.nn.Linear(self.num_ftrs, 10)
        self.model.load_state_dict(torch.load(path, map_location=torch.device("cpu")))
        self.model.eval()

    def __call__(self, image):
        return self.model(image)
