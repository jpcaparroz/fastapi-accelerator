from fastapi import Body

from schemas import user_schema as schemas


UpdateUserBody = Body(
    title='User',
    description='The user json representation.',
    examples=[
        schemas.UpdateUserSchema(
            user_name='user_example',
            user_password='******',
            user_email='example@gmail.com',
            is_admin=True
        )
    ]
)