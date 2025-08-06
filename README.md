# 🧩 STEP File Analysis API (FastAPI + Docker)

This project provides an API to extract metadata (file_name, width, depth and height) from `.stp` (STEP) files. It is containerized with Docker and can be deployed on **any platform that supports Docker**.

We've tested and verified deployment using **Render**, which is easy to set up even for users with limited technical experience. You can get it running with just a few basic steps.

If you're comfortable with Docker, feel free to deploy it on your own infrastructure or any preferred cloud platform.

---

## 🚀 How to Deploy on Render

### 📝 Prerequisites

- A **GitHub account**
- A **Render account** (you can create one at [https://render.com](https://render.com))

---

### 🔧 Steps to Deploy

1. **Log into GitHub**

2. Click the green **“Use this template”** button at the top of this page.

3. Create your own GitHub repository using this template.

4. Go to [Render](https://render.com) and **log in**.

5. Click **"New +" → "Web Service"**.

6. **Connect your GitHub account** to Render if not already connected.

7. Select the repository you created from this template.

8. In the service configuration:
   - **Runtime**: Docker  
   - **Start Command**: _Leave this blank (the `Dockerfile` handles it)_  
   - **Region**: Choose the region closest to your location

9. Click **“Create Web Service”** and wait for the deployment to complete.
    
10. Render will give you a **public HTTPS URL** like:
   <br><br> `<url>` = `https://your-app-name.onrender.com`
   <br><br> Navigate to `<url>/docs` to ensure the FastAPI service is running. 

---

## 🔗 After Deployment

You can then use the `<url>/analyse` in a **POST** method and upload the `.stp` file.

👉 For example, in an **HTTP Request node** in an **n8n workflow**, configure:

- **Method**: `POST`  
- **URL**: `<url>/analyse`  
- Enable **Send Body**  
- **Body Content Type**: `Form-Data`  
- **Body Parameters**:
  - **Parameter Type**: `n8n binary file`
  - **Name**: `file`
  - **Input Data Field Name**: `<The name of the incoming field containing the binary file data to be processed>`

⚠️ Make sure the binary file input (from a previous node) matches the field name you set here.
<br><br>
⚠️ Replace `<url>` with the actual Render URL you get after deployment.

- Example Response:
```json
{
  "file_name": "example.stp",
  "width": 56.78,
  "depth": 9.10,
  "height": 12.34
}
```
