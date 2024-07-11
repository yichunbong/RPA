from notion_client import Client
from datetime import datetime 
import pytz



# 노션 API 키 설정
notion_api_key = "secret_5J9IH9GAuyeV7KYzE4CCOY2FtXMA4xGDKJlSUeHHD6B"
notion = Client(auth=notion_api_key)

# 생성할 페이지의 부모 데이터베이스 ID
database_id = "78c1d6bda4474eaeb5b0c5fb643b978e"

"""

def get_page_url(page_id):
    # Notion 페이지 URL 형식
    return f"https://www.notion.so/{page_id.replace('-', '')}"

# 데이터베이스 쿼리
response = notion.databases.query(database_id=database_id)

# 데이터베이스 항목 출력
for page in response['results']:
    properties = page['properties']
    title = properties['이름']['title'][0]['text']['content']

    print(f"Title: {title}")    
    print("-" * 20)
    
"""

# 한국 표준시(KST) 타임존 가져오기
kst = pytz.timezone('Asia/Seoul')
now = datetime.now(kst)

# 년, 월, 일, 시, 분, 초 추출
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second

newpage_title = f"{year}년 {month}월 {day}일 {hour}시 {minute}분 {second}초"

# 새로운 페이지 생성
new_page = notion.pages.create(
    parent={"database_id": database_id},
    properties={
        "이름": {
            "title": [
                {
                    "text": {
                        "content": newpage_title
                    }
                }
            ]
        }
    }
) 

#page_id = new_page["id"]
page_url = new_page["url"] #get_page_url(page_id)

# 생성된 페이지의 정보 출력
print("Created page url:")
print(page_url)