# wabigram

Cloning instagram with Python Django and React / React Native

---

## pipenv

    Commands:
    check      Checks for security vulnerabilities and against PEP 508 markers
                provided in Pipfile.
    clean      Uninstalls all packages not specified in Pipfile.lock.
    graph      Displays currently–installed dependency graph information.
    install    Installs provided packages and adds them to Pipfile, or (if no
                packages are given), installs all packages from Pipfile.
    lock       Generates Pipfile.lock.
    open       View a given module in your editor.
    run        Spawns a command installed into the virtualenv.
    shell      Spawns a shell within the virtualenv.
    sync       Installs all packages specified in Pipfile.lock.
    uninstall  Un-installs a provided package and removes it from Pipfile.

### 1.27 : Django

메타는 해당 클래스의 Extra정보
장고는 DataBase에 어떤 정보가 올지 읽는다. 모델링 이후 마이그레이션은 필수.

    python manage.py makemigrations && python manage.py migrate


    class Meta:
            abstract = True # Meta 클래스는 무엇이든 이것은 필드가 아니다 라고 지정. (URL과 무관한 클래스라고 지정) : DataBase와 연결 안함

Many to one || One to many

Django \_set

1.  Automagically groups all the related objects into a property

2.  To call all the objects related to the owner all we have to do is call 'modelName_set'

3.  For the cat model it would be cat_set


        wabis = Owner.objects.get(id=1)
        wabi_cats = wabis.cat_set.all()

Many to many : Many users can follow many users

pk = primary key

---

## Many to one || One to many || Many to many ???

    Image can have many comment.
    Image can have many Like
    User can have many Image
    User can have many comment
    User can have many Like

### Djnago 외래키 사용 주의

    Since Django 2.0 The ForeignKey field requires two positional arguments.(The model to map, on_delete argument)

    for example :
    ...
    models.ForeignKey(users_model.User, on_delete=models.PROTECT)
    ...
