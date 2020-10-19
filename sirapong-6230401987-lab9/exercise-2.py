from abc import ABC, abstractmethod

class Abstract_class_image:
    @abstractmethod
    def load_image(self):
        pass
    @abstractmethod
    def save_image(self):
        pass

class Bitmap(Abstract_class_image):
    def load_image(self, name):
        print(f"loading bitmap file {name}")
    def save_image(self, name):
        print(f"saving bitmap file {name}")

class Jpeg(Abstract_class_image):
    def load_image(self, name):
        print(f"loading bitmap file {name}")
    def save_image(self, name):
        print(f"saving bitmap file {name}")

if __name__ == "__main__":
    bitmap1 = Bitmap()
    bitmap1.save_image("kku.bmp")
    bitmap1.load_image("kku.bmp")
    jpeg1 = Jpeg()
    jpeg1.save_image("en.jpg")
    jpeg1.load_image("en.jpg")