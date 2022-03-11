from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .models import Profile
from .db import session

#Schema class for model Profile.
class ProfileSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Profile
        sqla_session = session