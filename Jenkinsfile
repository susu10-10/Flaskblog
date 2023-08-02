pipeline {
    environment {
        registry = '10.5.10.38:5000/flaskr-webapp'
        IMAGE_URL_WITH_TAG = '${registry}:${env.BUILD_NUMBER}'
    }
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                    // Build the Docker image
                    sh "docker build . -t ${IMAGE_URL_WITH_TAG}"
            }
        }

        stage('Push Docker Image') {
            steps {
                sh ""
                }
            }

        stage("Post") {
            steps {
                echo "Successfully, pushed image to the docker registry"
            }
        }

        // Add more stages for other tasks in your Jenkins pipeline
        // For example, stages for testing and deployment.
    }

    // Optionally, you can add post-build actions or notifications.
    // For example, sending an email on failure or success.
}
