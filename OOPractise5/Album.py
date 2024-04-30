class Album:
    _images = []

    def __init__(self, id, name, user):
        self.id = id
        self.name = name
        self.user = user

    def add_image(self, image):
        if image.user.id == self.user.id:
            self._images.append(image)
        else:
            print("Hiba, a felhasználó nem adhat hozzá képet!")

    def get_all_image(self):
        for image in self._images:
            print(f"{self.name}: {image.name}")