from direct.showbase.ShowBase import ShowBase

class HelloWorld(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        self.scene = self.loader.loadModel("models/environment")
        self.scene.reparentTo(self.render)
        self.scene.setScale(1, 1, 1)
        self.scene.setPos(0, 0, 0)

        self.cube1 = self.loader.loadModel("models/misc/rgbCube")
        self.cube1.reparentTo(self.render)
        self.cube1.setScale(1, 1, 1)
        self.cube1.setPos(0, 20, 0)

        self.cube2 = self.loader.loadModel("models/misc/rgbCube")
        self.cube2.reparentTo(self.render)
        self.cube2.setScale(1, 1, 1)
        self.cube2.setPos(5, 20, 0)
        self.cube2.setScale(2.4)

app = HelloWorld()
app.run()
