from datetime import datetime

from flask import Blueprint, render_template, request, redirect, abort, flash
from flask_login import login_required, current_user

from ..models.user import User
from ..extensions import db
from ..models.post import Post
from ..forms import StudentForm, TeacherForm

post = Blueprint('post', __name__)


@post.route('/', methods=['POST', 'GET'])
def all():
    form = TeacherForm()
    form.teacher.choices = [('', 'All teachers')] + [(t.id, t.name) for t in
                                                          User.query.filter_by(status='teacher')]
    disciplines = db.session.query(Post.discipline).distinct().all()
    form.discipline_filter.choices = [('', 'All courses')] + [(d[0], d[0]) for d in disciplines if d[0]]
    groups = db.session.query(Post.group_number).distinct().all()
    form.group_filter.choices = [('', 'All groups')] + [(g[0], g[0]) for g in groups if g[0]]
    query = Post.query
    if request.method == 'POST':
        teacher_id = form.teacher.data
        discipline = form.discipline_filter.data
        group = form.group_filter.data
        show_checked = form.show_checked.data
    else:
        teacher_id = request.args.get('teacher_id')
        discipline = request.args.get('discipline')
        group = request.args.get('group')
        show_checked = request.args.get('checked') == '1'

        if teacher_id:
            form.teacher.data = teacher_id
        if discipline:
            form.discipline_filter.data = discipline
        if group:
            form.group_filter.data = group
        if show_checked:
            form.show_checked.data = True

    if teacher_id:
        query = query.filter(Post.teacher == teacher_id)

    if discipline:
        query = query.filter(Post.discipline == discipline)

    if group:
        query = query.filter(Post.group_number == group)

    if show_checked:
        query = query.filter(Post.is_checked == True)

    posts = query.order_by(Post.date.desc())

    if not any([teacher_id, discipline, group, show_checked]):
        posts = posts.limit(20)

    posts = posts.all()

    return render_template('post/all.html', posts=posts, user=User, form=form)


@post.route('/post/create', methods=['POST', 'GET'])
@login_required
def create():
    form = StudentForm()
    form.student.choices = [s.name for s in User.query.filter_by(status='user')]
    if request.method == 'POST':
        subject = request.form['subject']
        discipline = request.form.get('discipline', '')
        comment = request.form.get('comment', '')
        group_number = request.form.get('group_number', '')
        is_checked = bool(request.form.get('is_checked', False))
        student = request.form['student']
        student_id = User.query.filter_by(name=student).first().id

        # Handle deadline
        deadline_str = request.form.get('deadline')
        deadline = datetime.strptime(deadline_str, '%Y-%m-%d') if deadline_str else None

        post = Post(
            teacher=current_user.id,
            subject=subject,
            discipline=discipline,
            comment=comment,
            group_number=group_number,
            is_checked=is_checked,
            student=student_id,
            deadline=deadline
        )

        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(e)
            db.session.rollback()
            flash('Error creating post', 'danger')

        return redirect('/')
    else:
        return render_template('post/create.html', form=form)


@post.route('/post/<int:id>/update', methods=['POST', 'GET'])
@login_required
def update(id):
    post = Post.query.get_or_404(id)

    if post.teacher != current_user.id:
        abort(403)

    form = StudentForm()
    students = User.query.filter_by(status='user').all()
    form.student.choices = [(str(s.id), s.name) for s in students]

    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                post.subject = form.subject.data
                post.discipline = form.discipline.data
                post.comment = form.comment.data
                post.group_number = form.group_number.data
                post.is_checked = form.is_checked.data
                post.deadline = form.deadline.data

                student_id = form.student.data
                if student_id:
                    student = User.query.get(student_id)
                    if not student:
                        flash('Selected student not found', 'danger')
                        return redirect('/')
                    post.student = student.id

                db.session.commit()
                flash('Post updated successfully', 'success')
                return redirect('/')

            except Exception as e:
                db.session.rollback()
                flash(f'Error updating post: {str(e)}', 'danger')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f"Error in field {getattr(form, field).label.text}: {error}", 'danger')

    else:
        current_student = User.query.get(post.student)
        if current_student:
            form.student.data = str(post.student)
        form.subject.data = post.subject
        form.discipline.data = post.discipline
        form.comment.data = post.comment
        form.group_number.data = post.group_number
        form.is_checked.data = post.is_checked
        form.deadline.data = post.deadline

    return render_template('post/update.html', form=form, post=post)

@post.route('/post/<int:id>/delete', methods=['POST', 'GET'])
@login_required
def delete(id):
    post = Post.query.get(id)
    if post.author.id == current_user.id:

        try:
            db.session.delete(post)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(str(e))
    else:
        abort(403)
