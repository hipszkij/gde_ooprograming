class Album:
    ##_images = []

    def __init__(self, id, name, user):
        self.id = id
        self.name = name
        self.user = user
        self._images = []

    def add_image(self, newImage):
        if newImage.user == self.user:
            self._images.append(newImage)

    def get_images(self):
        for image in self._images:
            print(f"Album: {self.name}")
            print(f"Kép: {image.name}, Tulajdonos: {image.user.name}")