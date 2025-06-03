from flask import Blueprint, render_template, redirect, flash, url_for, request
from flask_login import login_required, current_user
from ..models.post import Post
from ..extensions import db
from ..functions import save_file

student_bp = Blueprint('student', __name__)

@student_bp.route('/student/dashboard')
@login_required
def dashboard():
    posts = Post.query.filter_by(student=current_user.id).all()
    return render_template('student/dashboard.html', posts=posts)


@student_bp.route('/student/upload/<int:post_id>', methods=['GET', 'POST'])
@login_required
def upload(post_id):
    post = Post.query.get_or_404(post_id)

    if post.student != current_user.id:
        flash("Access denied", "danger")
        return redirect(url_for('student.dashboard'))

    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            filename = save_file(file)
            post.student_file = filename
            db.session.commit()

            flash('File uploaded successfully!', 'success')
            return redirect(url_for('student.dashboard'))
        else:
            flash('No file selected', 'warning')

    return render_template('student/upload.html', post=post)

@student_bp.route('/student/comment/<int:post_id>', methods=['GET', 'POST'])
@login_required
def comment(post_id):
    post = Post.query.get_or_404(post_id)
    if post.student != current_user.id:
        flash("Access denied", "danger")
        return redirect(url_for('student.dashboard'))

    if request.method == 'POST':
        comment_text = request.form.get('comment')
        if comment_text:
            post.student_comment = comment_text
            db.session.commit()
            flash('Comment submitted!', 'success')
            return redirect(url_for('student.dashboard'))
        else:
            flash('Comment cannot be empty', 'warning')

    return render_template('student/comment.html', post=post)