import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import WebDriverException, TimeoutException
import time

BASE_URL = "https://jsonplaceholder.typicode.com"
def test_get_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    print("✅ GET Users OK")
def test_post_user():
    payload = {"name": "QA Engineer", "job": "Tester"}
    headers = {"Content-Type": "application/json"}
    response = requests.post(f"{BASE_URL}/posts", json=payload, headers=headers)
    print("\n--- POST USER DEBUG ---")
    print("Status code:", response.status_code)
    print("Response body:", json.dumps(response.json(), indent=2))
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    print("✅ POST User OK")
def test_put_user():
    payload = {"name": "QA Updated", "job": "Engineer"}
    response = requests.put(f"{BASE_URL}/posts/1", json=payload)
    assert response.status_code in [200, 201]
    print("✅ PUT User OK")
def test_delete_user():
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code in [200, 204]
    print("✅ DELETE User OK")
def open_api_docs():
    print("🔍 Membuka dokumentasi API...")
    try:
        service = Service("msedgedriver.exe")
        options = Options()
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        driver = webdriver.Edge(service=service, options=options)
        driver.set_page_load_timeout(60) 
        driver.get("https://reqres.in/")
        time.sleep(3)  
        driver.maximize_window()
        assert "ReqRes" in driver.title
        print("✅ API Docs loaded successfully")
        driver.quit()
    except TimeoutException:
        print("Timeout saat membuka dokumentasi API")
        driver.quit()
    except WebDriverException as e:
        print(f"WebDriverException: {e}")
    except Exception as e:
        print(f" Gagal membuka dokumentasi: {e}")
if __name__ == "__main__":
    print("\n=== START API TEST SESSION ===")
    try:
        test_get_users()
        test_post_user()
        test_put_user()
        test_delete_user()
        try:
            open_api_docs()
        except Exception as e:
            print(f"Gagal membuka dokumentasi: {e}")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

    print("\n=== END TEST SESSION ===")


