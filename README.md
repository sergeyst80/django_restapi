# Poll API (django REST framework)

# Installation:

1. Clone github repository from https://github.com/sergeyst80/django_restapi.git with command:

git clone https://github.com/sergeyst80/django_restapi.git <destination_folder>

2. Create and activate virtual enviroment.

3. Install django and djangorestframework (use requirements.txt). In project folder run command:

pip install -r requirements.txt

4. Apply migrations.

python ./src/manage.py migrate

5. Create superuser.

python ./src/manage.py createsuperuser

# API reference

1. Create new poll (for admin account).
Input parameters:
{
    "name": <"Poll name">,
    "end date": <"yyyy-mm-dd">,
    "description": <"Poll description">
}

URL: api/v1/poll/admin/create/

2. View all polls (for admin account).
[
    {
        "id": 1,
        "name": "test1",
        "start_date": "2021-04-28",
        "end_date": "2021-09-30",
        "description": "test1"
    },

    ...
]
URL: admin/list/

3. View details about poll - GET command, update pholl - PUT command, delete poll - DELETE command (for admin account). pk - primarykey.

URL: admin/detail/<int:pk>/

4. View questions by poll primarykey. If pk is 0 all questions will return. Answer variants are strings separated with symbol "|".

question_type is enumeration
QUESTION_TYPE = (
        (1, 'Text answer'),
        (2, 'One answer select'),
        (3, 'More than one answer select')
    ) 

output format:
[
    {
        "id": 1,
        "text": "Apple is ...",
        "question_type": 2,
        "answer_variants": "vegetable|fruit|car",
        "correct_answer": "fruit",
        "poll": 1
    },
    ...
]
URL: admin/question/list/<int:pk>/

5. Create new question (for admin account).
Input parameters:
{
    "poll": 1, 
    "text": "Question text",
    "question_type": 2
    "answer_variants": "vegetable|fruit|car"
    "correct_answer": "fruit",
    "poll": 1
}

URL: admin/question/create/

6. View question detail by primarykey (for admin account).
Otput format:
{
    "id": 1,
    "text": "Apple is ...",
    "question_type": 2,
    "answer_variants": "vegetable|fruit|car",
    "correct_answer": "fruit",
    "poll": 1
}


URL: admin/question/detail/<int:pk>/

7. View active polls when end_date greater and equal current date.
output format:
[
    {
        "id": 1,
        "name": "test1",
        "start_date": "2021-04-28",
        "end_date": "2021-09-30",
        "description": "test1"
    },
    ...
]

URL: user/list/

8. View all questions for poll by primarykey.
output format:
[
    {
        "pk": 1,
        "text": "Apple is ...",
        "question_type": 2,
        "answer_variants": "vegetable|fruit|car"
    },
    {
        "pk": 2,
        "text": "3 + 5 = ?",
        "question_type": 1,
        "answer_variants": ""
    }
]
URL: user/question/list/<int:pk>/

9. Start new poll.

Input data:
{
    "user_id": 123,
    "poll": 2
}

Output data:
{
    "id": 3,
    "user_id": 123,
    "poll": 2
}

URL: user/start/

10. Send answer.
Input data:
{
    "answer": "laptop",
    "user_poll": 2,
    "question": 3
}

Output data:
{
    "id": 5,
    "answer": "laptop",
    "user_poll": 2,
    "question": 3
}

URL: user/answer/

11. Users polls history view.
Output data:

[
    {
        "pk": 1,
        "poll": "test1",
        "answers": [
            {
                "question": "Apple is ...",
                "answer": "fruit"
            },
            {
                "question": "3 + 5 = ?",
                "answer": "9"
            }
        ]
    },
    {
        "pk": 2,
        "poll": "test2",
        "answers": [
            {
                "question": "What is \"PC\"?",
                "answer": "computer"
            },
            {
                "question": "1+1=?",
                "answer": "2"
            },
            {
                "question": "What is \"PC\"?",
                "answer": "laptop"
            }
        ]
    },
    {
        "pk": 3,
        "poll": "test2",
        "answers": []
    }
]

URL: user/history/<int:user>/