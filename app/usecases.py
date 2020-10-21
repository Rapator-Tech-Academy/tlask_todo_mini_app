from stories import story, arguments, Success, Failure, Result

from app.entities import Task
from app.factories import TaskFactory

class AddTaskCase:
    @story
    @arguments('header', 'body', 'done')
    def create(I):
        I.validate_inputs
        I.build_entity
        I.persist_task
        I.show_task
    
    def validate_inputs(self, ctx):
        header_validated = isinstance(ctx.header, str)
        body_validated = isinstance(ctx.body, str)
        if header_validated and body_validated:
            return Success()
        else:
            return Failure()

    def build_entity(self, ctx):
        ctx.entity_factory = TaskFactory(builder=Task)
        ctx.entity = ctx.entity_factory.create(
            header = ctx.header,
            body = ctx.body,
            done = ctx.done,
        )
        return Success()
    
    def persist_task(self, ctx):
        ctx.result = self.repo.create_task(entity=ctx.entity)
        return Success()

    def show_task(self, ctx):
        return Result(ctx.result)