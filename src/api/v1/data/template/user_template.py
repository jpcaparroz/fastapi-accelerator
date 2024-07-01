from fastapi import Body

from schemas.user_schema import CreateUserSchema
from schemas.user_schema import UpdateUserSchema


UpdateUserBody = Body(
    title='User',
    description='The update user json representation.',
    examples=[
        UpdateUserSchema(
            user_name='user_example',
            user_password='******',
            user_email='example@gmail.com',
            is_admin=True
        )
    ]
)


CreateUserBody = Body(
    title='User',
    description='The create user json representation.',
    examples=[
        CreateUserSchema(
            user_name='user_example',
            user_password='******',
            user_email='example@gmail.com',
            is_admin=True
        )
    ]
)