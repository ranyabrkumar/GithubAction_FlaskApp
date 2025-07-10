# Flask App CI/CD with GitHub Actions

This project shows how to set up a CI/CD pipeline for a Python Flask application using GitHub Actions.

The goal is to automatically:
- Install dependencies
- Run tests
- Deploy to a staging server when changes are pushed to the `staging` branch
- Deploy to a production server when a release is created from the `main` branch

---

## Branches

- `main`: The stable branch used for production
- `staging`: The development branch used for testing changes before production

---

## What the Workflow Does

The GitHub Actions workflow file is located at:

.github/workflows/pipeline.yml
using : self-hosted runner:
<img width="833" height="186" alt="image" src="https://github.com/user-attachments/assets/c07b8d12-ec7a-49fa-8ff6-50968d407c8c" />


It runs the following steps:

1. **Run Tests**
   - Sets up Python and installs packages from `requirements.txt`
   - Runs tests using `pytest`
   - If any test fails, the workflow stops

3. **Deploy to Staging**
   - Happens automatically when you push to the `staging` branch
   - Connects to your staging server, pulls the code, installs dependencies, and restarts the app

4. **Deploy to Production**
   - Happens when you create a release from the `main` branch
   - Connects to your production server, pulls the code, installs dependencies, and restarts the app
  
  <img width="530" height="516" alt="image" src="https://github.com/user-attachments/assets/c4da2b6e-ac24-4bb5-9b1e-a57f95a3ee24" />


---

## GitHub Secrets You Need

To keep sensitive information safe, store these values in your repository's Secrets:

- `STAGING_SECRET` - Secert of stagging
- `PROD_SECRET`- Secert of production
- `PRODUCTION_SERVER_IP` – IP address of your production server
- `EC2_PRIVATE_KEY` – Private SSH key used to access your production server

Go to your GitHub repo → Settings → Secrets and variables → Actions to add them.
<img width="1183" height="369" alt="image" src="https://github.com/user-attachments/assets/8c29e36b-ae55-44a5-881c-4f966984a643" />
<img width="1169" height="185" alt="image" src="https://github.com/user-attachments/assets/a5315f0a-4154-428b-ad5f-2c059884cf26" />

---

## How to Use the CI/CD Pipeline

### Deploying to Staging

When you're ready to test your changes, push to the `staging` branch:

```bash
git checkout staging
git add .
git commit -m "Test changes"
git push origin staging
```

<img width="1393" height="552" alt="image" src="https://github.com/user-attachments/assets/de5624bb-6291-4a97-9b25-284b19bac92f" />

---

### Deploying to Production
Once the code is tested and stable, go to the main branch, tag a new release, and push:
```bash
git checkout main
git tag v1.0.0
git push origin v1.0.0
```
Then, go to GitHub → Releases → "Draft a new release" and select the tag. Creating the release will trigger the production deployment.

<img width="2114" height="686" alt="image" src="https://github.com/user-attachments/assets/eeacfded-7ee0-499d-8785-ce1dc8042505" />

---

<img width="1299" height="189" alt="image" src="https://github.com/user-attachments/assets/54468841-1fc7-4e6a-b97e-318b7f84b85c" />

<img width="1786" height="887" alt="image" src="https://github.com/user-attachments/assets/e0a567ce-ec5d-4b1c-8f15-dd07e7924b45" />
<img width="2203" height="947" alt="image" src="https://github.com/user-attachments/assets/6a3ae37c-24ff-48a5-b6d4-577b4b1fdbf3" />



