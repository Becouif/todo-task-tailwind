from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db


class Todo(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    task: so.Mapped[str] = so.mapped_column(sa.String(100))
    priority: so.Mapped[str] = so.mapped_column(sa.String(20))
    status: so.Mapped[str] = so.mapped_column(sa.String(20))

    def __repr__(self):
        return '<id: {}, task: {}, priority: {}, status: {}>'.format(self.id, self.task, self.priority, self.status)