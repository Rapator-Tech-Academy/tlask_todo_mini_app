from flask import render_template, flash, redirect
from app import app

from app.forms import AddTaskForm
from app.usecases import AddTaskCase
from app.repository import Repository

repo = Repository()

@app.route("/", methods=['GET', 'POST'])
def index():
    add_task=AddTaskCase()
    add_task.repo = repo
    form = AddTaskForm()

    all_tasks = repo.get_all_tasks()

    if form.validate_on_submit():
        result = add_task.create(
            header=form.header.data,
            body=form.body.data,
            done=form.done.data,
        )
        flash(f"Task created : {result}")
        return redirect("/")
    return render_template("home.html", form=form, tasks=all_tasks)