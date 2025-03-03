# Backend - FastAPI

## **Overview**
This is the backend service built with **FastAPI**, handling audio file uploads and storing metadata in a **MySQL** database. It provides APIs for file upload, retrieval, and visualization support.

---

## **1️⃣ Prerequisites**
- Python 3.9+
- MySQL (running via Docker or installed locally)
- `pip` for package management
- `uvicorn` for running the FastAPI server

---

## **2️⃣ Setup & Installation**

### **Step 1: Clone the Repository**
```bash
git clone <repo-url>
cd backend
```

### **Step 2: Create a Virtual Environment** (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 4: Start MySQL (via Docker)**
If MySQL is not running locally, start a MySQL container:
```bash
docker run --name mysql-db -e MYSQL_ROOT_PASSWORD=rootpassword \
    -e MYSQL_DATABASE=mydatabase -e MYSQL_USER=user -e MYSQL_PASSWORD=password \
    -p 3306:3306 -d mysql:8
```

---

## **3️⃣ Running the Server**

### **Option 1: Run FastAPI Locally**
Ensure `main.py` has the correct database connection (`localhost` instead of `mysql-db` if running outside Docker):
```python
DATABASE_URL = "mysql+pymysql://user:password@localhost:3306/mydatabase"
```
Then, start the FastAPI server:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### **Option 2: Run FastAPI Inside Docker**
Use `mysql-db` as the database host if running inside Docker:
```python
DATABASE_URL = "mysql+pymysql://user:password@mysql-db:3306/mydatabase"
```
Then, build and run the FastAPI container:
```bash
docker build -t backend .
docker network create mynetwork
docker run --name backend --network mynetwork -p 8000:8000 backend
```

---

## **4️⃣ API Endpoints**
### **Check API Docs**
Once the server is running, open **Swagger UI**:
```
http://localhost:8000/docs
```

### **Available Endpoints**
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Check if API is running |
| `POST` | `/upload-audio/` | Upload an audio file |
| `GET` | `/uploaded-files/` | Fetch list of uploaded files |

---

## **5️⃣ Next Steps**
- ✅ Add **audio file processing** (e.g., duration, format analysis)
- ✅ Implement **real-time visualization support**
- ✅ Enhance security with authentication


