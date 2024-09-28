from flask import render_template,url_for,flash, redirect

from app import app, db
from app.forms import TodoForm
from app.models import Todo



@app.route('/')
@app.route('/index')
def home():
    statement = db.select(Todo)
    tasks = db.session.scalars(statement).all()
    form = TodoForm()
    return render_template('index.html', title="Home", todos=tasks, form=form)



@app.route('/create', methods=['GET', 'POST'])
def create():
    form = TodoForm()
    if form.validate_on_submit():
        todo = Todo(task=form.task.data, priority=form.priority.data, status=form.status.data)
        db.session.add(todo)
        db.session.commit()
        flash('Todo={}'.format(form.task.data))
        return redirect(url_for('home'))
    return render_template('create.html', title="Create", form=form)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    todo = Todo.query.get_or_404(id)
    form = TodoForm()
    if form.validate_on_submit():
        todo.task = form.data['task']
        todo.priority = form.data['priority']
        todo.status = form.data['status']
        db.session.commit()
        return redirect(url_for('home'))


# pass all data back
    form.task.data = todo.task
    form.priority.data = todo.priority
    form.status.data = todo.status
    return render_template('edit.html', title="Edit", form=form)






@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('home'))



