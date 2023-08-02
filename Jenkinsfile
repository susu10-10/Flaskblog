pipeline {
    environment {
        registry = '10.5.10.38:5000/flaskr-webapp'
        IMAGE_URL_WITH_TAG = "${registry}:${env.BUILD_NUMBER}"
    }
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
<<<<<<< HEAD
                // Build the Docker image
                sh "docker build . -t ${IMAGE_URL_WITH_TAG}"
=======
                    // Build the Docker image
                    sh "docker build . -t ${IMAGE_URL_WITH_TAG}"
>>>>>>> d2058ca7780169598542d5b07f81b3ddfbb9e9b4
            }
        }

        stage('Push Docker Image') {
            steps {
<<<<<<< HEAD
                // Push the Docker image to the registry
                sh "docker push ${IMAGE_URL_WITH_TAG}"
=======
                sh ""
                }
>>>>>>> d2058ca7780169598542d5b07f81b3ddfbb9e9b4
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
