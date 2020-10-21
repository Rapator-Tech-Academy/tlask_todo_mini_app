class TaskFactory:
    def __init__(self, builder):
        self.builder = builder
    
    def create(self, **kwargs):
        return self.builder(
            header=kwargs.get('header'),
            body=kwargs.get('body'),
            done=kwargs.get('done', False)
        )