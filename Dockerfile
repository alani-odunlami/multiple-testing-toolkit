# 1. Use an official, lightweight Python runtime as a parent image
FROM python:3.12-slim

# 2. Set environment variables to optimize Python inside a container
# Prevents Python from writing .pyc files; forces unbuffered stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 3. Set the working directory inside the container
WORKDIR /app

# 4. Create a non-root user for security and switch to it
RUN useradd --create-home appuser
USER appuser

# 5. Copy just the dependency file first to leverage Docker layer caching
COPY --chown=appuser:appuser requirements.txt .

# 6. Install dependencies (adds local bin to PATH for the non-root user)
RUN pip install --no-cache-dir --user -r requirements.txt

# 7. Copy the rest of the application source code
COPY --chown=appuser:appuser . .

# 8. Expose the port your app runs on (e.g., 8000 for Django/FastAPI)
EXPOSE 8000

# 9. Define the default command to run your app
# (Update "main.py" to match your project's primary execution file)
CMD ["python", "main.py"]
