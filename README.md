# ifet

# FastAPI Reporting System

## Overview

This project is a FastAPI application designed to manage and report on various tests conducted on projects. It provides a REST API for handling project and test data. The application is containerized using Docker and can be easily started with Docker Compose.

## Getting Started

To get started with the project, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository

2. **Start the Application:**

   Ensure you have Docker and Docker Compose installed. Run the following command to build and start the application:

   ```bash
   docker-compose up

3. **Access the Application:**

   Once the application is running, you can access the API at:

   - **Swagger UI:** `http://localhost:8000/docs`
   - **ReDoc:** `http://localhost:8000/redoc`

   The FastAPI server will be available on port 8000.

## Notes

- Ensure that you have a `.env` file or the necessary environment variables configured in the Docker Compose file for database connections and other settings.
- If you need to stop the application, use `docker-compose down` to stop and remove the containers.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [amr.kasem@yandex.com](mailto:amr.kasem@yandex.com).
