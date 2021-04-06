from flask import request
from flask_restful import Resource
from http import HTTPStatus

from db.db import get_mydql_connection

# 우리가 이 파일에서 작성하는 클래스는 
# 플라스크 프레임워크에서 경로랑 연결시킬 클래스입니다.
# 따라서 클래스명 뒤에 resource클래스를 상속받아야합니다.
# 플라스크 프레임워크의 레퍼런스 사용법에 나와있습니다.
class RecipeListResource(Resource) :
    # get 메소드로 연결시킬 함수 작성
    def get(self):
        # recipe 테이블에 저장되어있는 모든 레시피 정보를 가져오는 함수

        # 1. DB 커넥션을 가져온다.
        connection = get_mydql_connection()

        # 2. 커서를 가져온다.
        cursor = connection.cursor(dictionary = True)

        # 3. 쿼리문을 작성한다.
        query = """select * from recipe;"""

        # 4. sql 실행
        cursor.excute(query)

        # 5. 데이터를 페치한다.
        records = cursor.fetchall()
        print(records)

        ret = {}
        for row in records:
            row['created_at'] = row['created_at'].isoformat()
            row['updated_at'] = row['updated_at'].isoformat()
            ret.append(row)

        # 6. 커서와 커넥션을 닫아준다.
        cursor.close()
        connection.close()

        # 7. 클라이언트에 리스폰스 한다.
        return { 'count':len(records), 'ret':records }, HTTPStatus.OK

    def post(self):
        # recipe 테이블에 저장되어있는 모든 레시피 정보를 가져오는 함수

        # 1. DB 커넥션을 가져온다.
        connection = get_mydql_connection()

        # 2. 커서를 가져온다.
        cursor = connection.cursor(dictionary = True)

        # 3. 쿼리문을 작성한다.
        query = """select * from recipe;"""

        # 4. sql 실행
        cursor.excute(query)

        # 5. 데이터를 페치한다.
        records = cursor.fetchall()
        print(records)

        ret = {}
        for row in records:
            row['created_at'] = row['created_at'].isoformat()
            row['updated_at'] = row['updated_at'].isoformat()
            ret.append(row)

        # 6. 커서와 커넥션을 닫아준다.
        cursor.close()
        connection.close()

        # 7. 클라이언트에 리스폰스 한다.
        return { 'count':len(records), 'ret':records }, HTTPStatus.OK